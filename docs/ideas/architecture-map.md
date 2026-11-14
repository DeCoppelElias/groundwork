# Architecture map

Status: idea.

## What it does

Adds an `ARCHITECTURE.md` document that maps the code as it is: its modules,
what each holds, and where the tests live. A finished entry updates that map
instead of the README, and the README is left to the people visiting the
repo.

## Why it is interesting

The workflows decision makes the README the file an entry updates. In a public
repo, though, the README is the project's front page. In one project, the
owner had rewritten it on GitHub for players while an entry added a code
layout section for agents, and the two collided in a merge. A map with its own
lane keeps each document to one reader and gives an agent one place to look
before changing code.

## What it would touch

The documents and workflows decisions, the AGENTS.md template, setting up, and
perhaps the checker.

## Open questions

- Does a project without much code still get the file, with a one-line stub?
- How much detail belongs in it: modules only, or also the interfaces between
  them?
- Can the checker tell when it falls behind, for example a module folder it
  never names?
