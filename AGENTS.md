# AGENTS.md

A Claude Code plugin that gives a project a small set of documents and the workflows around them, so an AI agent can work in it in a structured way.

## Documents

- `DESIGN.md` what groundwork is for. Read it before proposing a feature.
- `CONTEXT.md` the glossary. Use its words.
- `docs/adr/` the decisions, one file per topic. Its README maps them by area.
  Read the ones that bear on a change before making it.
- `docs/ideas/` what is wanted and not decided. A new idea goes here without
  asking, in the format its README gives.
- `docs/roadmap/` the committed build order, listed in its README.

Each document says at its top what it holds and never holds. When you are not
sure where something belongs, ask Elias rather than picking. Link a
decision or an entry rather than restating it.

`python scripts/docs_check.py .` checks links, indexes and status lines. Run it after
changing any document.

## Asking

Ask Elias before promoting an idea onto the roadmap, changing an accepted
decision, adding or reordering roadmap entries, and before any push, merge,
pull request or tag. Asking means giving the options with a recommendation and
waiting, not deciding and asking for confirmation afterwards.

When a document has drifted or holds something outside its lane, report it
with the fix you propose, and change it only after Elias says go.

A grill writes nothing to the documents until it ends. Then it sends a summary
of every choice and the changes it makes, and applies them on a branch after
Elias says go.

## Roadmap entries

An entry is built on its own branch, `entry-<slug>`. Grill the details it
leaves open before planning. It is finished when the tests pass, the code is
reviewed, its status reads `done`, the project's README describes what it built, any idea
it built is marked `built`, any choice made on the way is in its decision, and
`python scripts/docs_check.py .` is clean. Then it merges on Elias's go.

## Build and run

```
python tests/test_docs_check.py     the checker's tests
python scripts/docs_check.py .      the checker on these documents
claude plugin validate .            the manifests
claude plugin eval . --scaffold --trust-plugin --allow-tools Write Edit    the evals, which cost money; ask first
```
