# Taskboard design

This file holds what Taskboard is for: its vision, its goals and what it
will not do. It never holds how the code is built, which belongs in
`docs/adr/`, and it never links a decision or names a file in the code. It
changes when the direction changes, not when a decision does, and it stays
under 150 lines.

## Vision

A single-user task board in the browser.

Cards are saved to localStorage under the key `board`, as one JSON value, on
every change, because a single user on one browser needs nothing more and
IndexedDB would add an async layer for no gain.

## Goals

- Cards move between three columns.
- Nothing is lost on reload.

## Non-goals

- No accounts or sharing.
