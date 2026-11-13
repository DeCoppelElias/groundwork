# groundwork

A Claude Code plugin that gives a project a small set of documents and the
workflows around them, so an AI agent can work in it in a structured way.

What it sets up:

- `DESIGN.md` for the vision, goals and non-goals.
- `CONTEXT.md` for the project's glossary.
- `docs/adr/` for decisions, one file per topic, rewritten in place.
- `docs/ideas/` for what is wanted and not decided.
- `docs/roadmap/` for the committed build order.
- `AGENTS.md` for how agents work in the project and when they ask.

It also ships `groundwork-docs-check`, which checks that the documents link up
and stay within their rules, and only those workflow skills a fresh agent
still needs.

It builds on [superpowers](https://github.com/obra/superpowers) and
[mattpocock/skills](https://github.com/mattpocock/skills).

## Install

```
claude plugin marketplace add DeCoppelElias/groundwork
claude plugin install groundwork@groundwork
```

groundwork works best alongside superpowers and mattpocock's skills, whose
grills it relies on. Install them the same way if you do not have them.

In a new project, ask Claude to set it up with groundwork.

MIT licensed.
