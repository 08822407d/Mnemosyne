# First Real Target Dry-run Evaluation Framework v0.1

## Positioning

Non-execution-source support instrument derived from DR5. It guides evaluation only; it does not select a target, ingest materials, authorize workspace creation, start a dry-run, approve target repository write, or update execution source.

## Object model

| Object | Purpose | Real target required | Target materials | Target write |
|---|---|---:|---:|---:|
| synthetic smoke test | Validate basic mechanics with synthetic inputs | no | no | no |
| tabletop dry-run | Discussion/script exercise for rules and approvals | optional | no raw originals | no |
| real target-project dry-run | Evidence-backed no-write validation in real target context | yes | only approved safe inputs | no |
| target delivery | User-facing delivery package | yes | approved | separate |
| target repository write | Persistent target write/commit/PR | yes | approved | explicit separate approval |

## Surface-specific no-write evidence contract

A real target-project dry-run defaults to no persistent write on the target repository and target runtime store. It does not automatically claim that every repository, local sandbox, or Mnemosyne evidence surface was unchanged.

The result must reference the reusable `no_write_evidence` and, when used, `no_write_evidence_exception` objects in `notes/object-templates-and-id-rules.md`.

Required evidence semantics:

```yaml
required_no_write_evidence:
  root_fields:
    - checked_at
    - proof_actor_or_process
  per_claim_surface_fields:
    - surface
    - repository_or_target
    - prohibited_write_scope
    - allowed_nonpersistent_outputs
    - pinned_pre_ref
    - pinned_post_ref
    - mechanical_method
    - mechanical_evidence_refs_or_commands_API_results
    - changed_paths
    - scope_match
    - result
    - limitations
  accepted_results:
    - pass
    - pass_with_approved_exception
```

Acceptance rules:

- prose self-report, tool-intent narration, `target_write: false`, or a method label without bound mechanical evidence is insufficient;
- `pass` requires exact scope match and mechanical evidence tied to pinned refs;
- `pass_with_approved_exception` requires a complete approved exception containing approval reference/time, approver, exact run/scope, unavailable-proof reason, substitute evidence refs, confidence, independent-verification status, and `not_future_precedent: true`;
- a complete approved exception is not blocked merely because the default proof was unavailable; missing, unapproved, incomplete, or scope-mismatched exception data remains fail-closed;
- `no_write_evidence_scope_mismatch` is a critical blocker;
- synthetic smoke test, tabletop exercise, real no-write run, target delivery, target repository write, and any separately authorized Mnemosyne evidence write remain separate actions and claims.

## Evaluation dimensions

| Dimension | Weight | Primary evaluator |
|---|---:|---|
| context recovery | 15 | deterministic + user |
| authority/source map | 15 | deterministic + user |
| input safety | 20 | deterministic + user |
| memory design fit | 15 | LLM judge limited + user |
| handoff/delivery usability | 15 | LLM judge limited + user |
| evidence/provenance | 10 | deterministic |
| assumption discipline | 5 | deterministic + LLM judge limited |
| postmortem/actionability | 5 | deterministic + LLM judge limited |

## Deterministic / LLM judge / user confirmation split

- Deterministic checks: approvals, manifests, source maps, material classification, redaction/pointer safety, no-target-write proof, synthetic/real evidence separation, evidence completeness.
- LLM judge: limited qualitative review of readability, schema fit, handoff usability, delivery-package coverage, and postmortem actionability.
- User confirmation: target selection, authority, usefulness, risk acceptance, and any later promotion beyond target-specific lessons.

## Evidence requirements

Require target selection record, approved run manifest, authority/source map, truth-source declaration, safe input ledger, storage policy, redaction manifest, external pointer review, surface-specific no-write evidence conforming to the reusable mechanical contract, memory schema, handoff package, delivery package inventory, assumption/conflict log, scorecard, user confirmation, postmortem, and regression candidates.

## PASS limitations

PASS does not mean production-ready, target repository write approved, target delivery accepted, or global execution-source update approved.

## Integration recommendations

Use `notes/first-real-target-dry-run-scorecard-v0.1.md` after blockers clear. Feed findings to postmortem, regression candidates, and candidate review layers only; do not directly modify execution source.
