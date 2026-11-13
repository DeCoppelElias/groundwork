# groundwork design

This file holds what groundwork is for: its vision, its goals and what it
will not do. It never holds how the code is built, which belongs in
`docs/adr/`, and it never links a decision or names a file in the code. It
changes when the direction changes, not when a decision does, and it stays
under 150 lines.

## Vision

A Claude Code plugin that gives a project a small set of documents and the
workflows around them, so an AI agent can work in it in a structured way.

Each document has one job and says so at its top. An agent reading a project
set up with groundwork knows where a vision, a word, a decision, an idea or the
build order lives, and asks the owner when something fits none of them.

## Goals

- General. It assumes no language, framework or build tool.
- One place to change. A fix to the layout, the checker or a workflow reaches
  every project through the plugin, not through copies to update by hand.
- Nothing drifts unseen. What a pattern can catch, the checker catches in the
  editor and in CI. What it cannot, the documents' own rules let an agent see.
- Only what earns its place. A workflow becomes a skill only when an agent
  without one gets it wrong.

## Non-goals

- No tooling for one project or one stack, such as comment checks.
- No writing rules. Those belong to the owner, not the kit.
- No grilling skill of its own. It uses the grills it builds on.
