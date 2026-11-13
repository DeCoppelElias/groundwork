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


def check(root: Path):
    findings = []
    for path in markdown_files(root):
        check_links(root, path, path.read_text(encoding="utf-8"), findings)
    check_design(root, findings)
    check_context(root, findings)
    return findings


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    findings = check(root)
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
