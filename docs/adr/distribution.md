# Distribution

groundwork is a Claude Code plugin in its own marketplace, plus a
`setting-up` skill that writes a project's documents once. A template
repository was rejected because a fix would never reach projects made from it,
and synced copies were rejected because every project would carry a copy to
update. The plugin keeps skills and the checker in one place.

The checker is on the agent's PATH through the plugin's `bin/`, with an sh
launcher for Bash and a `.cmd` launcher because PowerShell cannot run the sh
one. A project's CI fetches the checker at a pinned tag instead, since CI has
no plugins.

groundwork declares no plugin dependencies, and the README recommends
superpowers and mattpocock's skills instead. An eval run loads only the plugin
under test, and a plugin whose dependencies are missing does not load, so
declared dependencies would leave groundwork untestable. It calls none of
their skills, so nothing breaks without them.
