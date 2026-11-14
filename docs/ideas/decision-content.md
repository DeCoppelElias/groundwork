# Decision content

Status: idea.

## What it does

Makes the decisions README say plainly what a decision file holds: the
decision as the project stands now and why, plus rejected options worth
remembering. It never describes how the project used to be or how the choice
was reached, because Git keeps that.

## Why it is interesting

The template asks for "the context, the decision and why". In one project an
agent read context as history and wrote a decision that opened with the two
systems the repo used to have. The owner had to explain the rule by hand and
add it to that project's README. The grill skill's ADR format asks for context
too, so the same reading will keep coming back.

## What it would touch

The decisions README template, its copies in the sample eval and this repo,
and perhaps an eval that checks a written decision for past-tense history.

## Open questions

- Is one sentence in the template enough, or does it need a short example of
  a good and a bad decision?
- Should the checker flag history in a decision, or is that beyond a regex?
