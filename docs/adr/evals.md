# Evals

Workflows are tested with `claude plugin eval` against a small made-up
project in `evals/_sample/`, which each case's scaffold copies into the empty
run workspace. Each case grades the outcome and the steps, and compares runs
with and without the plugin.

Eval runs load no CLAUDE.md, so every prompt starts by pointing at AGENTS.md,
the way CLAUDE.md does in real use. The line is in both arms, so it does not
favour the plugin. Cases use Write and Edit only, because a Bash grant needs an
OS sandbox that native Windows lacks. `claude plugin eval` needs git 2.31 or
later.

A suite run uses one run per case and no baseline arm, to keep the cost near
a dollar. The baseline adds little here, because the sample already carries
AGENTS.md, so both arms would see the same instructions.
