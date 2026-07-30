# Research Prompt Registry

> Design, registry and historical redirect surface. This directory is not the operator-facing queue for deciding what research to run next.

## Where operators find runnable Fable5 tasks

```text
handoff/fable5-ready/
```

Only that queue should be used for manual task discovery. Each ready task includes an operator guide and exact input manifest.

## File states

A prompt under this directory must be understood by its explicit status and current-route record:

```yaml
prompt_states:
  DRAFT:
    runnable: false
  READY:
    runnable: only_if_a_matching_handoff/fable5-ready/<TASK_ID>/_entry_exists
  COMPLETED_REDIRECT:
    runnable: false
    canonical_original: raw/research-reports/cycles/<cycle>/tasks/
  RETIRED:
    runnable: false
  HISTORICAL:
    runnable: false
```

A detailed task file does not become current merely because it remains at an old path or has not been deleted.

## Completion lifecycle

After a run is accepted:

1. preserve the exact original task under its research cycle;
2. preserve the report or report receipt under that cycle;
3. update the cycle manifest and current status;
4. remove the matching directory from `handoff/fable5-ready/`;
5. convert this registry path to a short completion redirect when the stable path should remain discoverable.

Completed redirects must not be copied or run as new tasks.

## Retirement without execution

Remove the task from the ready queue and preserve the retirement reason in a non-runnable research plan or retirement record. Do not leave a retired task mixed with active operator choices.

## Current operating guidance

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```
