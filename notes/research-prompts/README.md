# Research Prompt Registry

> Design, specification, registry and historical redirect surface. This directory is not the operator-facing queue for deciding what research to run next.

## Runnable Fable5 tasks

Operators use:

```text
handoff/fable5-ready/
```

The design/launch conversation must also provide the complete operating procedure directly. Repository navigation is a durable reference, not the only way the user learns the steps.

## Specification versus execution contract

A current Fable task may separate:

```yaml
canonical_specification:
  role: stable_research_question_audit_criteria_report_sections_and_authority_boundaries
active_execution_contract:
  role: current_surface_context_input_binding_cost_and_delivery_rules
ready_entrypoint:
  role: binds_the_two_and_states_current_run_status
```

For the current frontier-clarification Stage-A tasks:

```yaml
A1:
  canonical_specification: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
  active_execution_contract: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
A2:
  canonical_specification: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
  active_execution_contract: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
```

The older surface label inside a canonical specification is not independently runnable when a matching ready entrypoint names a newer execution contract. For A1/A2, the active contract requires ordinary `Fable 5` + `Max`, Advanced Research off, and a full same-context repository gate.

## File states

```yaml
prompt_states:
  DRAFT:
    runnable: false
  READY_SPECIFICATION:
    runnable: only_with_the_active_execution_contract_named_by_handoff/fable5-ready/<TASK_ID>/task.md
  ACTIVE_EXECUTION_CONTRACT:
    runnable: only_when_the_matching_ready_entry_exists_and_activation_gate_is_met
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

After a substantive run is accepted:

1. preserve the exact active execution contract and canonical specification under its research cycle;
2. preserve the report or report receipt under that cycle;
3. update the cycle manifest and current status;
4. remove the matching directory from `handoff/fable5-ready/`;
5. convert stable registry paths to non-runnable completion redirects when needed.

A failed input-binding run is archived under `failed-runs/` and does not count as a completed substantive research task.

## Current operating guidance

```text
notes/research-operations/claude-fable5-repository-bound-static-audit-v0.2.md
```

Historical product-access and delivery analysis remains at:

```text
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
```
