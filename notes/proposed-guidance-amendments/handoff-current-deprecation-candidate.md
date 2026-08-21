# Handoff Current

> Deprecated non-execution-source compatibility pointer. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
handoff_current_status: deprecated_as_global_route_selector
selected_route: none
authorized_handoff_package_source: exact_Owner_supplied_startup_message_only
automatic_route_inference: prohibited
historical_content_preserved_in_git: true
```

This file no longer selects, recommends, or describes a live handoff route.

For every handoff receive:

1. use only the exact package path and identity explicitly supplied by the Owner's startup message;
2. read `commands/receive-mnemosyne-handoff.md`;
3. treat the package, this file, `current/active-context.md`, status files, TODOs and old handoff cards as non-execution-source evidence;
4. do not substitute a similarly named or previously selected package;
5. fail closed when the Owner-supplied package or required identities cannot be verified.

Historical per-route handoff packages and startup prompts remain immutable evidence under their own paths. This compatibility file must not be refreshed into a second global route truth source.
