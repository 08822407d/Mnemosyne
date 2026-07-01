# DR5 first real target-project dry-run evaluation framework — summary

## 1. Executive summary

DR5 defines first real target-project dry-run success as evidence-backed, authority-bounded, no-target-write validation in a real target context. It warns against treating a polished artifact, fluent model output, synthetic smoke test, or single task completion as proof of real dry-run success.

## 2. Direct recommendation before first real target dry-run

Before any real dry-run, Mnemosyne should require target selection, authority/source-map approval, target runtime truth-source declaration, safe input/user originals storage approval, redaction/external-pointer safety review, no-target-write confirmation, approved run manifest, and a frozen rubric. Missing prerequisites should yield `BLOCKED` rather than an improvised run.

## 3. Evaluation object model

- `synthetic smoke test`: synthetic/maintainer-created materials only; validates basic mechanics, not real target usefulness.
- `tabletop dry-run`: discussion/script exercise; validates roles, rules, and approval chain.
- `real target-project dry-run`: selected real target, approved safe inputs, real no-write validation; produces first real dry-run evidence.
- `target delivery`: actual user-facing delivery package; not automatically repository write approval.
- `target repository write`: higher-authority boundary requiring explicit separate approval.

## 4. Critical blockers

```yaml
critical_blockers:
  - target_not_selected
  - authority_missing
  - no_target_write_not_confirmed
  - unsafe_material_ingested
  - target_repository_written_without_approval
  - synthetic_evidence_reported_as_real_dry_run
  - target_workspace_treated_as_execution_source
  - target_runtime_truth_source_invented
  - user_originals_stored_unsafely
  - missing_run_manifest_approval
```

Critical blockers override score and can make the result `BLOCKED`.

## 5. Scorecard dimensions

```yaml
score_dimensions:
  context_recovery: 15
  authority_source_map: 15
  input_safety: 20
  memory_design_fit: 15
  handoff_delivery_usability: 15
  evidence_provenance: 10
  assumption_discipline: 5
  postmortem_actionability: 5
```

## 6. Result semantics

```yaml
verdicts:
  PASS: no blocker, score >= 90, critical/major minimums met, user confirms usefulness and boundaries
  PASS_WITH_WARNINGS: no blocker, score 75-89, core goals reached with moderate repairs
  REPAIR_RECOMMENDED: no blocker, score 60-74 or multiple major defects
  FAIL: enough evidence to evaluate, but core capability or usability failed
  BLOCKED: blocker prevents legal real-dry-run evaluation
```

PASS does not mean production-ready, target repository write approval, target delivery acceptance, or global Mnemosyne rule update.

## 7. Evidence requirements

Minimum evidence includes approved run manifest, target selection record, authority/source map, truth-source declaration, ingest ledger/materials safety classification, redaction manifest, external pointer safety note, no-target-write proof, memory schema/retrieval examples, handoff package, delivery package inventory, assumption/conflict log, user confirmation record, postmortem, and regression candidates.

## 8. Postmortem and regression schemas

DR5 recommends a factual postmortem that separates target-specific lessons from global lesson candidates and a regression record capturing source event, expected recovery, forbidden claims, deterministic checks, LLM-judge checks, user confirmation checks, result, evidence, failure class, and follow-up task.

## 9. Integration recommendations

Use deterministic checks for boundaries and evidence completeness, LLM-as-judge only for limited qualitative dimensions, and user confirmation for usefulness/risk acceptance. Dry-run findings should feed postmortem, regression candidates, and self-improvement candidate review; they should not directly update execution source.

## 10. Limits and open questions

DR5 is supplemental evidence only. It does not select a target, ingest materials, start a dry-run, approve target repository write, or update execution source. Some score thresholds may need recalibration after actual dry-run evidence.
