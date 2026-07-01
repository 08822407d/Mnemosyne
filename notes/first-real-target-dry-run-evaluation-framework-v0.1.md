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

Require target selection record, approved run manifest, authority/source map, truth-source declaration, safe input ledger, storage policy, redaction manifest, external pointer review, no-target-write proof, memory schema, handoff package, delivery package inventory, assumption/conflict log, scorecard, user confirmation, postmortem, and regression candidates.

## PASS limitations

PASS does not mean production-ready, target repository write approved, target delivery accepted, or global execution-source update approved.

## Integration recommendations

Use `notes/first-real-target-dry-run-scorecard-v0.1.md` after blockers clear. Feed findings to postmortem, regression candidates, and candidate review layers only; do not directly modify execution source.
