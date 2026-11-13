#!/usr/bin/env python3
"""Checks a groundwork project's documents where a regex can tell.

Usage:
    groundwork-docs-check [ROOT]
    python docs_check.py [ROOT]

ROOT defaults to the current directory. Whether a document says something it
should not, beyond what a pattern sees, is a judgement for the agent and the
owner. Exit code is 1 while findings remain.
"""

import re
import sys
from pathlib import Path


FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
DOCS_PATH = re.compile(r"`(docs/[\w./-]+\.md)`")


def markdown_files(root):
    yield from sorted(root.glob("*.md"))
    docs = root / "docs"
    if docs.is_dir():
        for path in sorted(docs.rglob("*.md")):
            if "superpowers" not in path.relative_to(root).parts:
                yield path


def blank_out(pattern, text):
    """Replace matches with spaces, keeping newlines so line numbers survive."""
    return pattern.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def prose_of(text):
    return blank_out(INLINE_CODE, blank_out(FENCE, text))


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def rel_of(root, path):
    return path.relative_to(root).as_posix()


def check_links(root, path, text, findings):
    rel = rel_of(root, path)
    for m in LINK.finditer(prose_of(text)):
        target = m.group(1).split("#")[0]
        if not target or re.match(r"^[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            findings.append(f"{rel}:{line_of(text, m.start())}: broken link {target}")
    for m in DOCS_PATH.finditer(blank_out(FENCE, text)):
        if not (root / m.group(1)).exists():
            findings.append(f"{rel}:{line_of(text, m.start())}: missing path {m.group(1)}")


DESIGN_MAX_LINES = 150


def line_count(text):
    return text.count("\n") + (0 if text.endswith("\n") or not text else 1)


def check_no_code(rel, text, findings):
    m = FENCE.search(text)
    if m:
        findings.append(f"{rel}:{line_of(text, m.start())}: holds a code block; code belongs in the code")


def check_design(root, findings):
    path = root / "DESIGN.md"
    if not path.exists():
        findings.append("DESIGN.md is missing")
        return
    text = path.read_text(encoding="utf-8")
    lines = line_count(text)
    if lines > DESIGN_MAX_LINES:
        findings.append(
            f"DESIGN.md: {lines} lines, the cap is {DESIGN_MAX_LINES}; detail belongs in docs/adr/"
        )
    check_no_code("DESIGN.md", text, findings)
    prose = prose_of(text)
    for m in LINK.finditer(prose):
        if "docs/adr/" in m.group(1):
            findings.append(f"DESIGN.md:{line_of(text, m.start())}: links a decision; DESIGN.md stays above them")
    for m in DOCS_PATH.finditer(blank_out(FENCE, text)):
        if m.group(1).startswith("docs/adr/"):
            findings.append(f"DESIGN.md:{line_of(text, m.start())}: links a decision; DESIGN.md stays above them")


def check_context(root, findings):
    path = root / "CONTEXT.md"
    if path.exists():
        check_no_code("CONTEXT.md", path.read_text(encoding="utf-8"), findings)


SLUG_FILE = re.compile(r"^[a-z][a-z0-9-]*\.md$")


def folder_index(root, name, findings):
    """The folder's README text, or None when the folder does not exist."""
    folder = root / "docs" / name
    if not folder.is_dir():
        return None
    readme = folder / "README.md"
    if not readme.exists():
        findings.append(f"docs/{name}/README.md is missing")
        return ""
    return readme.read_text(encoding="utf-8")


def entries(root, name):
    for path in sorted((root / "docs" / name).glob("*.md")):
        if path.name != "README.md":
            yield path, f"docs/{name}/{path.name}", path.read_text(encoding="utf-8")


def check_slug_and_index(path, rel, index, name, findings):
    if not SLUG_FILE.match(path.name):
        findings.append(f"{rel}: name it by its topic in lowercase, such as the-day.md, never by number")
    if f"({path.name})" not in index:
        findings.append(f"{rel} is not in docs/{name}/README.md")


def check_adrs(root, findings):
    index = folder_index(root, "adr", findings)
    if index is None:
        return
    for path, rel, text in entries(root, "adr"):
        check_slug_and_index(path, rel, index, "adr", findings)
        if not text.startswith("# "):
            findings.append(f"{rel}:1: no title heading")


IDEA_STATUSES = {"idea", "planned", "built"}
IDEA_SECTIONS = ["What it does", "Why it is interesting", "What it would touch", "Open questions"]
STATUS_LINE = re.compile(r"^Status: (.+?)\.?$", re.MULTILINE)


def check_ideas(root, findings):
    index = folder_index(root, "ideas", findings)
    if index is None:
        return
    for path, rel, text in entries(root, "ideas"):
        check_slug_and_index(path, rel, index, "ideas", findings)
        status = STATUS_LINE.search(text)
        word = status.group(1).split()[0].rstrip(".,") if status else None
        if word not in IDEA_STATUSES:
            findings.append(f"{rel}: status must start with one of {sorted(IDEA_STATUSES)}")
        elif word == "built" and "../adr/" not in status.group(1):
            findings.append(f"{rel}: built but links no decision in its status line")
        elif word == "planned" and "../roadmap/" not in status.group(1):
            findings.append(f"{rel}: planned but links no roadmap entry in its status line")
        for section in IDEA_SECTIONS:
            if not re.search(rf"^## {section}\s*$", text, re.MULTILINE):
                findings.append(f"{rel}: missing section {section}")


ROADMAP_STATUSES = {"not started", "in progress", "done"}
ENTRY_NUMBER = re.compile(r"\bentry\s+\d+\b", re.IGNORECASE)


def check_roadmap(root, findings):
    index = folder_index(root, "roadmap", findings)
    if index is None:
        return
    for path, rel, text in entries(root, "roadmap"):
        check_slug_and_index(path, rel, index, "roadmap", findings)
        status = STATUS_LINE.search(text)
        if not status:
            findings.append(f"{rel}: no status line")
        elif status.group(1) not in ROADMAP_STATUSES:
            findings.append(f"{rel}: status {status.group(1)!r}, expected one of {sorted(ROADMAP_STATUSES)}")


def check_entry_numbers(root, path, text, findings):
    for m in ENTRY_NUMBER.finditer(prose_of(text)):
        findings.append(
            f"{rel_of(root, path)}:{line_of(text, m.start())}: names a roadmap entry by number; link it by slug"
        )


def check(root: Path):
    findings = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        check_links(root, path, text, findings)
        check_entry_numbers(root, path, text, findings)
    check_design(root, findings)
    check_context(root, findings)
    check_adrs(root, findings)
    check_ideas(root, findings)
    check_roadmap(root, findings)
    return findings


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    findings = check(root)
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
