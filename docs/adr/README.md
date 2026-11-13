# Decisions

One file per topic, named by the topic, such as `storage.md`. When a choice on
a topic changes or grows, rewrite that topic's file so it states the current
decision. Write a new file only for a new topic. Never number a file, whatever
another skill's format says. Git keeps the history.

A decision belongs here when it is hard to reverse, would surprise someone
reading the code, and came from a real trade-off. Anything else lives in the
code and its tests.

A file holds a title, then in a few sentences the context, the decision and
why. Add the rejected options only when the reason they lost is worth
remembering, and the consequences only when they are not obvious.

The list below groups the topics by area, one line each. It is the map: read
it to find which decisions bear on a piece of work.

## Distribution

- [Distribution](distribution.md) a plugin in its own marketplace, the checker on the PATH and fetched by CI.

## Documents

- [Documents](documents.md) the six documents, their lanes, topic decisions and slug entries.

## Workflows

- [Workflows](workflows.md) AGENTS.md lines first, skills only where an eval shows the need.
- [Evals](evals.md) native evals against a sample project.
