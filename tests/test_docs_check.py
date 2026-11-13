"""Tests for docs_check.py. Run with: python tests/test_docs_check.py"""

import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "docs_check", Path(__file__).resolve().parent.parent / "scripts" / "docs_check.py"
)
docs_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docs_check)

DESIGN = """# Sample design

This file holds the vision, goals and non-goals.

## Vision

A small app.
"""

CONTEXT = """# Sample

A small app.

## Language

**Card**:
One task on the board.
_Avoid_: ticket
"""

ADR = """# Storage

Cards are kept in one JSON file, because the app is single-user.
"""

IDEA = """# Some idea

Status: idea.

## What it does

## Why it is interesting

## What it would touch

## Open questions
"""

ENTRY = """# Board

Status: not started.

Text.
"""


class DocsCheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("DESIGN.md", DESIGN)
        self.write("CONTEXT.md", CONTEXT)
        self.write("docs/adr/storage.md", ADR)
        self.write("docs/adr/README.md", "# Decisions\n\n## Data\n\n- [Storage](storage.md) one JSON file.\n")
        self.write("docs/ideas/some-idea.md", IDEA)
        self.write("docs/ideas/README.md", "# Ideas\n\n- [Some idea](some-idea.md)\n")
        self.write("docs/roadmap/board.md", ENTRY)
        self.write("docs/roadmap/README.md", "# Roadmap\n\n1. [Board](board.md)\n")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def findings(self):
        return docs_check.check(self.root)

    def assertFinding(self, fragment):
        found = self.findings()
        self.assertTrue(any(fragment in f for f in found), f"no finding with {fragment!r} in {found}")

    def test_a_valid_project_is_clean(self):
        self.assertEqual(self.findings(), [])


if __name__ == "__main__":
    unittest.main()
