# Existing code

Status: idea.

## What it does

Gives a project that already has code a way to reach decisions the owner
actually holds. Setting up today assumes nothing has been built yet, so it
writes empty decisions and stops. A project with code has choices already made,
and many of them were never thought through.

The path that worked in one project: survey the code for topics, write each
topic as an idea instead of a decision, then add a run of foundation entries to
the roadmap. Each entry grills one topic, writes its decision, and changes the
code to follow it. New features start once those entries are done.

## Why it is interesting

Writing decisions straight from the code would lock in accidents, and an
owner who says "half of this was never a choice" has nowhere to put that. In
that project, working out this path took most of two sessions, and any
project that adopts groundwork after its first commit will run into the same
problem.

## What it would touch

The setting-up skill, the AGENTS.md template, and probably an eval for a
project with code and no documents.

## Open questions

- Is this a step at the end of setting up, a line in AGENTS.md, or a skill of
  its own? The workflows decision says to try the lightest fix first.
- Who writes the topic list: the agent from a survey, or the owner in a grill?
- Do foundation entries need a marker in the roadmap, or are they ordinary
  entries that happen to come first?
