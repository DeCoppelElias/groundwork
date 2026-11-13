---
name: setting-up
description: Sets up groundwork's documents in a project that has none yet: DESIGN.md, CONTEXT.md, docs/adr, docs/ideas, docs/roadmap, AGENTS.md, the plugin in project settings and the CI docs check. Use when asked to set up groundwork, start a project's docs, or "set this project up properly".
---

# Setting up

## Before writing anything

1. Look for `DESIGN.md`, `AGENTS.md`, `CONTEXT.md`, `docs/adr/`,
   `docs/ideas/` and `docs/roadmap/`. If any exists, stop. Say which, and that moving an existing project onto groundwork
   is a migration to plan with the owner, not a setup. Never overwrite.
2. Gather the tokens, and ask the owner for what you cannot read:
   - `{{PROJECT}}`: the project's name, from the folder or its manifest.
   - `{{ONE_LINE}}`: what it is, in one sentence. Ask; do not invent it.
   - `{{OWNER}}`: who approves, from `git config user.name`. Confirm it.
     When that is empty or the folder is not a git repository, ask.
   - `{{BUILD_COMMANDS}}`: the build, test and run commands, from the
     project's files (package.json scripts, pom.xml, pyproject.toml, Makefile).
     Show what you found and confirm. Write `None yet.` when there are none.
   - `{{GROUNDWORK_TAG}}`: the plugin's version from
     `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`, prefixed with `v`.
3. Ask whether the project is on GitHub. Only then copy the CI workflow.

## Writing

Copy every file under `${CLAUDE_PLUGIN_ROOT}/skills/setting-up/templates/` to
the same path in the project, filling the tokens. Skip `.github/` unless the
owner said the project is on GitHub. Two files may already exist and are
merged, never replaced. If `CLAUDE.md` exists, add `@AGENTS.md` as its first
line. If `.claude/settings.json` exists, merge the two keys into it.

Then run `groundwork-docs-check` and fix what it reports. Leave the Goals,
Non-goals and Language sections for the owner to fill, and offer to grill
them with `grill-with-docs`.

Do not commit. Show the list of files written and let the owner decide.
