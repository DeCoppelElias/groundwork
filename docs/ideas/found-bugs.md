# Found bugs

Status: idea.

## What it does

Gives bugs a place in the documents. A review of an entry branch often finds
problems the branch did not cause, and today they come back mixed in with the
review's feedback, with nowhere to go once they are set apart. Ideas hold what
is wanted, and a bug is not wanted, so either bugs get their own home or the
ideas folder widens to hold them.

## Why it is interesting

In one project a review of an entry returned eight findings, and half of them
predated the branch. The owner read them as feedback on the entry until they
were sorted by hand. That project tracked bugs as tests in a `KnownBug`
category, expected to fail, which means every run of the suite has to exclude
them and a full run is always red. The owner disliked that and wanted a
tracking file instead, with a test written only when a bug gets fixed.

## What it would touch

The AGENTS.md template, where the roadmap entries section would say that a
review covers what the branch changed and where older findings go. Possibly a
new folder or file with its own format, and the docs check if it gets an index.

## Open questions

- Is it a bugs folder with one file per bug, a single bugs list, or
  a wider ideas folder with a kind on each idea?
- Does a bug get a status line, such as `open` and `fixed`, and does a fixed
  bug stay listed?
- Is a failing test written when a bug is found, or only when it is fixed?
- Who may add a bug without asking, and may a quick fix go into the entry that
  found it?
