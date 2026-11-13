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

groundwork depends on mattpocock's skills and superpowers, from other
marketplaces. The marketplace lists both in
`allowCrossMarketplaceDependenciesOn`; without that, an install drops the
dependencies and the plugin fails to load.
