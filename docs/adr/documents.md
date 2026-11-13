# Documents

A project gets DESIGN.md, CONTEXT.md, `docs/adr/`, `docs/ideas/`,
`docs/roadmap/` and AGENTS.md, and each states at its top what it holds and
never holds. DESIGN.md holds vision, goals and non-goals only, under 150
lines, and links no decision, because a design that restated decisions grew
into a second, drifting copy of them.

Decisions are one file per topic, named by the topic and rewritten in place
when the choice changes, in mattpocock's short format with its three-part bar:
hard to reverse, surprising, a real trade-off. Numbered records were rejected
because a reader had to replay a chain of superseded files to learn the
current choice. Git keeps the history.

Roadmap entries are files named by slug, with the order only in the roadmap's
README, so inserting an entry renumbers nothing. Nothing names an entry by
number.

The checker enforces the parts a pattern can see: links, indexes, status
lines, file names, the design's length, and no code in the design or glossary.
