# groundwork

A Claude Code plugin that gives a project a small set of documents and the
workflows around them, so an AI agent can work in it in a structured way.

What it sets up:

- `DESIGN.md` for the vision, goals and non-goals.
- `CONTEXT.md` for the project's glossary.
- `docs/adr/` for decisions, one file per topic, rewritten in place.
- `docs/ideas/` for what is wanted and not decided.
- `docs/roadmap/` for the committed build order.
- `AGENTS.md` for how agents work in the project and when they ask, with
  `CLAUDE.md` pointing at it.
- `.claude/settings.json`, which turns the plugin on for everyone who opens
  the project.
- A GitHub Actions workflow that runs the checker, if the project is on GitHub.

Setup refuses a project that already has `DESIGN.md`, `CONTEXT.md`,
`AGENTS.md` or one of the `docs/` folders, since moving one onto groundwork is
a migration rather than a setup. An existing
`CLAUDE.md` or `.claude/settings.json` is merged into, never replaced.

It also ships `groundwork-docs-check`, which checks that the documents link up
and stay within their rules. The workflows themselves live in `AGENTS.md`;
the one skill, `setting-up`, writes the documents.

It builds on [superpowers](https://github.com/obra/superpowers) and
[mattpocock/skills](https://github.com/mattpocock/skills).

## Install

```
claude plugin marketplace add DeCoppelElias/groundwork
claude plugin install groundwork@groundwork
```

The checker needs Python 3 on the PATH, as `python3`, `python` or, on
Windows, `py`.

groundwork works best alongside superpowers and mattpocock's skills, whose
grills it relies on:

```
claude plugin marketplace add obra/superpowers
claude plugin install superpowers@superpowers-dev
claude plugin marketplace add mattpocock/skills
claude plugin install mattpocock-skills@mattpocock
```

In a new project, ask Claude to set it up with groundwork.

MIT licensed.
