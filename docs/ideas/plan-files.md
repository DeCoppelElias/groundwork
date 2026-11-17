# Plan files

Status: idea.

## What it does

Gives implementation plans a place in a project. Planning skills write a plan
for an entry before its code, and the documents have no lane for it. A plan is
working material for one entry, not a record, so it would live in one
gitignored folder that the AGENTS.md template names.

## Why it is interesting

In one project an agent was about to save a roadmap entry's plan and found no
lane that fit. A planning skill's default, `docs/superpowers/plans/`, would
have put a new kind of document beside the decisions and ideas, with no
header saying what it holds. Saving it outside the repo hid it from the owner.
The owner asked for a gitignored folder in the repo, so a plan stays readable
during the entry and never becomes a document that drifts.

## What it would touch

The AGENTS.md template, which would name the folder and say it holds plans
only. The setting-up skill, which would add it to `.gitignore`. Possibly the
docs check, which should skip the folder.

## Open questions

- What is the folder called, and is it under `docs/` or at the root?
- Is a plan deleted when its entry merges, or left for the owner?
- Should a plan be committed on the entry branch instead, so a reviewer can
  read it, and dropped before the merge?
