# Handoff Current

> Deprecated non-execution-source compatibility pointer. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
latest_updated_by_task: MNEMOSYNE-240
handoff_current_status: deprecated_as_global_route_selector
selected_route: none
authorized_handoff_package_source: exact_Owner_supplied_startup_message_only
automatic_route_inference: prohibited
historical_content_preserved_in_git: true
```

This file no longer selects, recommends or describes a live handoff route.

For every receive:

1. use only the exact package path and identity supplied by the Owner's startup message;
2. read `commands/receive-mnemosyne-handoff.md`;
3. treat this file, status files, active-context files, TODOs and historical handoff cards as non-execution-source evidence;
4. never substitute a nearby or previously selected package;
5. fail closed when the Owner-supplied package or its load-bearing identities cannot be verified.

Historical route packages and startup prompts remain immutable evidence at their own paths. This compatibility file must not become a second global route truth source.
