# Storage

The board lives in the browser, for one user. It is saved to localStorage as
one JSON value, rewritten on every change. IndexedDB was rejected: its async
API and schema are more than a single user's board needs.
