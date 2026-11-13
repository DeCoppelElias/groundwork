# groundwork

A Claude Code plugin that gives a project a small set of documents and the
workflows around them, so an AI agent can work in it in a structured way.

This file is the glossary and nothing else: each word the project uses for its
own concepts, defined in a sentence or two, with the words to avoid. No
implementation, no decisions, no code. A general programming term does not
belong here.

## Language

**Document**:
One of the files groundwork sets up: the design, the glossary, a decision, an
idea, a roadmap entry, or AGENTS.md.
_Avoid_: doc page

**Lane**:
What a document holds and never holds, stated at its top.
_Avoid_: scope, section rules

**Decision**:
A file in `docs/adr/` that states the current choice on one topic and why.
_Avoid_: ADR number, record

**Topic**:
The subject a decision covers, which is also its file name.
_Avoid_: area (an area groups topics in the decisions index)

**Idea**:
Something wanted and not decided, with a status of idea, planned or built.
_Avoid_: proposal, backlog item

**Entry**:
One step of the roadmap, a file named by its slug, with a status.
_Avoid_: milestone, phase

**Owner**:
The person who approves, named in AGENTS.md.
_Avoid_: user, maintainer

**Grill**:
A session of questions that settles a design before it is written down.
_Avoid_: interview, review
