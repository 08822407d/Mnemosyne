# WORK-ULTRA-FABLE-GF5-STAGE-A-001 Maintainer Receipt

> Mechanical receipt and bounded maintainer interpretation only. This record is not execution source, architecture adoption, GF-STEP-5 adjudication, or implementation authorization.

```yaml
receipt_id: WORK-ULTRA-FABLE-GF5-STAGE-A-001-MAINTAINER-RECEIPT-001
storage_task: MNEMOSYNE-152
received_at: 2026-07-23
receipt_status: RECEIVED_COMPLETE_HIGH_SIGNAL
task_contract: PASS_WITH_MINOR_CLOSEOUT_CAVEAT
source_integrity: PASS_WITH_DISCLOSED_RECOVERABLE_STORAGE_ANOMALIES
comparison_firewall: PASS
substantive_status: ACCEPTED_FOR_STAGE_B_TASK_DESIGN
GF_STEP_5_read_or_adjudicated: false
architecture_adoption: not_performed
execution_source_modified: false
```

## 1. Artifact receipt

The maintainer received the exact task file, complete response, and six downloadable artifacts. Exact byte, SHA-256, and expected Git blob identities are in `manifest.yaml`.

The complete response and `stage-a-synthesis.md` are byte-for-byte identical. They are preserved at separate paths because one is the delivered chat response and the other is the named frozen synthesis artifact.

## 2. Mechanical checks

The received set supports the following mechanical statements:

- N1 contains 64 unique criteria and the six delta-category counts sum to 64.
- The current assessment contains 17 consecutive findings, `CURA-001` through `CURA-017`.
- The Greenfield assessment contains 15 primary findings and 25 3RV overlay mappings.
- The synthesis uses the required 16 H2 headings.
- The final status line is exactly `WORK_ULTRA_GF5_STAGE_A_COMPLETE`.
- Both YAML artifacts parse successfully.
- All eight stored source artifacts end with LF.

The Work output did not embed the final byte/hash identities for the synthesis and ledger because they were frozen after report generation. The maintainer computed and records them here:

```yaml
stage_a_synthesis:
  bytes: 47607
  sha256: 2f0b6f471117da64e592bac7abd2530ad7c7309afd31d5a078641a04db99a0fc
  git_blob_sha_expected: 1d79d754685eaff56e04eadda17376596860b4af

source_and_exposure_ledger:
  bytes: 29287
  sha256: 15aba7dcf3523678318a4d727715d3fe36535f6e14b0c51e1105af8e4e5f4f1c
  git_blob_sha_expected: 358162911e816ba76116b226e319fb40c17b7332
```

## 3. Bounded substantive interpretation

Stage A successfully produced a pre-reveal comparison basis:

```yaml
current_design:
  verdict: PASS_WITH_WARNINGS
  findings:
    P0: 0
    P1: 6
    P2: 10
    P3: 1

repaired_greenfield:
  verdict: FAIL_as_complete_64_criterion_candidate
  coverage:
    PASS: 31
    PASS_WITH_WARNINGS: 13
    FAIL: 20
  findings:
    P0: 0
    P1: 13
    P2: 2
```

These verdicts are scoped document-assessment outcomes. They do not establish that the current design is implemented, that the Greenfield architecture should be rejected, or that either design is globally superior.

The strongest candidate direction for later adjudication is to retain the current execution source and current-specific hard contracts while testing bounded adoption of Greenfield's typed authority, state, lineage, conflict, and failure-routing mechanisms.

## 4. Independence and firewall

The report states that:

- it ran in a fresh default-memory project;
- no prior Mnemosyne chats were moved into the project;
- complete account-level memory isolation was not mechanically guaranteed;
- the evidence firewall was applied;
- forbidden GF-STEP-5 content was not accessed;
- GitHub writes and external web research were zero.

This is a same-provider Work Ultra review with unknown backend identity, not heterogeneous-provider attestation. The pre-reveal track isolation materially improves the evidentiary value but does not make the tracks fully independent because they share N1 and execution-source compatibility constraints.

## 5. Closeout caveats

1. N0 self-reports 40 criteria, while its mechanical headings total 45. The frozen N0 was preserved; N1 uses the actual count.
2. The two multipart reconstruction anomalies are recoverable and produced the predeclared source identities after removing only exact storage-boundary redundancy.
3. Stage A is static document assessment, not repository-wide implementation audit or empirical target validation.
4. Platform freshness, repository visibility, connected-app completeness, PDF visuals, and historical validation reproducibility remain separate dependencies.

## 6. Next gate

After this exact storage PR is human-merged, a separately bounded Stage B may:

- reveal and read GF-STEP-5;
- compare its findings against the frozen Stage A artifacts;
- adjudicate agreement, conflict, omissions, unique findings, triage priority, research dependencies, and user-decision parameters;
- produce candidate decisions only.

Stage B must remain read-only and must not implement repairs or answer user parameters without later maintainer and user adjudication.
