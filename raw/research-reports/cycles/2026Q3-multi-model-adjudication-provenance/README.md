# 2026Q3 Multi-Model Adjudication and Runtime-Provenance Research

> Non-execution-source research evidence. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
cycle_id: RC-2026Q3-multi-model-adjudication-provenance
storage_task: MNEMOSYNE-145
repository_baseline_before_storage: master@abbcc28385767d44a053e6d0d0c01033c3e02193
canonical_experiment_scope: independent_conversation_pair_only
project_internal_round_included: false
substantive_acceptance: not_performed
execution_source_modified: false
```

## Purpose

This cycle studies how Mnemosyne should conduct multi-model architecture review when the visible product/model label does not fully attest the backend runtime, and how to preserve or restart work after a declared model-quality incident.

The canonical comparison stored by MNEMOSYNE-145 is limited to the later independent-conversation pair:

1. a run labeled `Pro`;
2. a run labeled `5.6sol Thinking`.

The earlier Project-internal pair is deliberately excluded from the canonical archive and checkpoint. It contained a severe wrong-task execution in the Thinking arm and introduces Project-context/orchestration confounders that are not needed for the reliable progress node.

## Exact source identities

| Artifact | Local filename received | Bytes | SHA-256 | Role |
|---|---|---:|---|---|
| Research task | `GPT-Pro-Deep-Research-multi-model-adjudication-runtime-provenance-v2.md` | 21,882 | `e839fe3466c4abdd10e4c3d2784b988875505c2833c2844b7329c3955f6ccad6` | task as executed |
| Independent labeled-Pro report | `DR07-pro_report(1).md` | 70,441 | `22a2c1bf4cf3a02e4b98d9457e0a78957736d2107fdd497324355122742ba9a9` | primary high-signal research candidate |
| Independent labeled-Thinking report | `DR07-thinking_report(2).md` | 63,242 | `135a30f39a1b3a5c725bc1014114cb79ae2f2152b2cb6bc0f0951a4a1b4f35f1` | independent control; repository access incomplete |

The exact large Markdown bodies are identified by these hashes but are not embedded by this storage task. The GitHub connector path used for MNEMOSYNE-145 did not provide a reliable direct large-file upload channel. This limitation is explicit rather than silently replacing exact originals with reconstructed text.

## Canonical interpretation

- The labeled-Pro report is the best complete result because it completed the bounded repository reads and the Mnemosyne-specific application.
- The labeled-Thinking report is high-quality external research and a useful control, but correctly ended with `RESEARCH_INCOMPLETE_REPOSITORY_ACCESS`.
- The two reports agree on 11 of the 12 required determinations.
- Output comparison does not prove either run's actual backend model identity.
- The reports remain non-execution-source evidence. No recommendation is adopted automatically.

## Files in this cycle

- `README.md` — cycle scope and exact identities.
- `independent-run-comparison.md` — fixed-rubric comparative review.
- `manifest.yaml` — machine-readable status and hashes.
- `source-portability-status.md` — citation portability limitation and later verification gate.
