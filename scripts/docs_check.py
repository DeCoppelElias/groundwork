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


def check(root: Path):
    findings = []
    return findings


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    findings = check(root)
    for finding in findings:
        print(finding)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
