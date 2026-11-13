#!/bin/sh
# The sample, plus the drag-and-drop entry built on its own branch.
set -e
sh "$(dirname "$0")/../_scaffold.sh"
git checkout -q -b entry-drag-and-drop
mkdir -p src
cat > src/drag.js <<'JS'
// Moves a card to another column when it is dropped there.
export function dropCard(board, cardId, toColumn) {
  const card = board.cards.find((c) => c.id === cardId);
  if (!card || !board.columns.includes(toColumn)) return board;
  return { ...board, cards: board.cards.map((c) => (c.id === cardId ? { ...c, column: toColumn } : c)) };
}
JS
cat > src/drag.test.js <<'JS'
import { dropCard } from "./drag.js";
import { test, expect } from "vitest";

test("a dropped card moves to the target column", () => {
  const board = { columns: ["todo", "doing", "done"], cards: [{ id: 1, column: "todo" }] };
  expect(dropCard(board, 1, "doing").cards[0].column).toBe("doing");
});
JS
git add -A
git -c user.name=eval -c user.email=eval@example.com commit -q -m "feat: cards move between columns by dragging"
