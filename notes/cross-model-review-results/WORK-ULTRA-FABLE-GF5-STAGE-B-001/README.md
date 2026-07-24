# WORK-ULTRA-FABLE-GF5-STAGE-B-001

> Exact non-execution-source preservation of the completed Stage B GF-STEP-5 reveal and cross-adjudication. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
task_id: WORK-ULTRA-FABLE-GF5-STAGE-B-001
storage_task: MNEMOSYNE-153
stage: B
status_claim: WORK_ULTRA_GF5_STAGE_B_COMPLETE
maintainer_receipt: RECEIVED_COMPLETE_HIGH_SIGNAL
PR_203_precondition: passed
GF_STEP_5_exact_report_verified: true
GF_STEP_5_inventory_verified: true
architecture_adoption_performed: false
implementation_performed: false
```

## Contents

- `manifest.yaml` — exact identities for the task, complete response, seven Stage B artifacts, and archive representation.
- `maintainer-receipt.md` — mechanical receipt and bounded interpretation for subsequent Pro maintainer adjudication.
- `closeout-and-execution-continuity-record.md` — final-response/synthesis difference and recovered-execution limitation.
- `archive-parts/WORK-ULTRA-FABLE-GF5-STAGE-B-001.tar.bz2.base64.part-0001.txt` through `part-0010.txt` — deterministic exact archive of nine source artifacts.

The archive contains:

1. `WORK-ULTRA-FABLE-GF5-STAGE-B-001-task.md`;
2. `WORK-ULTRA-GF5-STAGE-B-001-complete-chat-response.md`;
3. `WORK-ULTRA-GF5-STAGE-B-001-gf5-inventory.yaml`;
4. `WORK-ULTRA-GF5-STAGE-B-001-stage-a-gf5-crosswalk.yaml`;
5. `WORK-ULTRA-GF5-STAGE-B-001-triage-ledger.md`;
6. `WORK-ULTRA-GF5-STAGE-B-001-component-disposition.md`;
7. `WORK-ULTRA-GF5-STAGE-B-001-user-and-research-decision-package.md`;
8. `WORK-ULTRA-GF5-STAGE-B-001-stage-b-synthesis.md`;
9. `WORK-ULTRA-GF5-STAGE-B-001-source-and-exposure-ledger.yaml`.

## Reconstruction

From this directory:

```bash
cat archive-parts/WORK-ULTRA-FABLE-GF5-STAGE-B-001.tar.bz2.base64.part-* \
  | tr -d '\n' \
  | base64 --decode \
  | bzip2 --decompress \
  > WORK-ULTRA-FABLE-GF5-STAGE-B-001.tar

sha256sum WORK-ULTRA-FABLE-GF5-STAGE-B-001.tar
tar -xf WORK-ULTRA-FABLE-GF5-STAGE-B-001.tar
```

Expected archive identities:

```yaml
tar:
  bytes: 276480
  sha256: 2430ff422371230097dbaf9395b283b82327760c540c783eba90ea1738565216
bzip2_before_Base64:
  bytes: 41047
  sha256: e116698ff2f852c987aca3828d6659a8c05d52ca7d7f74819b396d86d1a15301
base64_characters: 54732
ordered_parts: 10
```

Verify every extracted member against `manifest.yaml`.

## Response/synthesis relation

The complete chat response and complete Stage B synthesis are **not** byte-identical:

```yaml
complete_chat_response:
  bytes: 27766
  sha256: 46c1d447404fa80ecd60180de70806987394eb9675a6048f51968af41e808f4d
stage_b_synthesis:
  bytes: 39031
  sha256: 8c63cde3ceeae209af0f123fd6b271db79c47bf804beef11b13ba776a859493e
difference_bytes: 11265
```

Both are retained because the response is the delivered chat original while the synthesis contains the complete named adjudication report.

## Mechanical result summary

```yaml
GF_STEP_5_inventory_items: 52
relations:
  INDEPENDENTLY_CORROBORATED: 31
  PARTIALLY_CORROBORATED: 17
  FABLE_ONLY_SUPPORTED: 4
Stage_A_findings_rechecked:
  current: 17
  greenfield: 15
original_triage_items: 10
new_consolidated_candidates: 7
components: 14
research_candidates: 6
blocking_user_decisions: 5
```

These counts are evidence summaries, not architecture adoption.

## Authority boundary

The artifacts do not:

- modify or replace the execution source;
- adopt either architecture as a whole or any individual component;
- authorize implementation, research, target-project work, or parameter answers;
- make qualitative 0–4 triage scores a calibrated quantitative instrument;
- prove hidden backend identity or heterogeneous-provider review;
- merge or auto-merge any PR.
