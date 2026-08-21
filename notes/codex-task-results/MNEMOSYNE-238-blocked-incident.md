# MNEMOSYNE-238 — Blocked Connector Publication Incident

```yaml
task_id: MNEMOSYNE-238
disposition: BLOCKED_CLOSED_NO_RETRY
architecture: CONNECTOR_GIT_DATA_BASE64_BLOBS_SINGLE_TREE
base: e726dea818dca9418181775d0e7dcd62eb6c464a
planned_branch: mnemosyne-238-f2-g2a-and-handoff-audit-closeout
reachable_commit_created: false
branch_created_or_moved: false
PR_created: false
G2A_issued: false
A1_executed: false
validation_repository_written: false
cleanup_performed: false
```

The GitHub connector preflight passed. The task began exact Base64 `create_blob` calls and compared every returned Git blob SHA to the frozen external manifest.

| seq | path | returned SHA | manifest comparison |
|---:|---|---|---|
| 1 | `current/fable5-cross-repository-safe-concurrency-research-status.md` | `5131a72b59ae75c7c3335e9bb27df655443d065d` | PASS |
| 2 | `handoff/handoff-current.md` | `693a7ec272f4074b82e5a4c548ac8c7f7fbc3281` | PASS |
| 3 | `notes/codex-task-results/MNE-235-236-PRO-RECOVERY-OBJECT-SIDE-EFFECT-RECEIPT-001.md` | `5e2c71e79d68779d3f849bc49de01ac0cfe0be42` | PASS |
| 4 | `notes/codex-task-results/MNEMOSYNE-235-blocked-incident.md` | `30247cb6027cb173efb6213425f68466d00e4908` | PASS |
| 5 | `notes/codex-task-results/MNEMOSYNE-236-blocked-incident.md` | `a357d0a46fecf2030dd744e14ff49fa905e589d8` | PASS |
| 6 | `notes/codex-task-results/MNEMOSYNE-237-blocked-incidents.md` | `2794e596bffb62a1cd4309facab477a43b908bc7` | PASS |
| 7 | `notes/codex-task-results/MNEMOSYNE-238-pr-finalization-contract.md` | `daba9018b12d1e2762dfbe66ccaf62d9d3dbf77f` | PASS |
| 8 | `notes/codex-task-results/MNEMOSYNE-238-result-contract.md` | `f83566854fe1786b3b5eadc56b60c83acf3cb1d1` | PASS |
| 9 | `notes/codex-task-results/MNEMOSYNE-238-verification-contract.md` | `322921d5f7f258f310cc7a7e283fd82887845e79` | PASS |
| 10 | `notes/proposed-guidance-amendments/handoff-current-deprecation-candidate.md` | `61aee2772af6f1b5fcf15371c12b67139e8180f7` | PASS |
| 11 | `notes/proposed-status-amendments/MNE-DR-006-REGISTRY-AMENDMENT-001.yaml` | `90165d1cbc491964a8a38d7bfdbfd8a1e3f06c45` | PASS |

At sequence 12, for `notes/proposed-status-amendments/MNE-F2-STATUS-AMENDMENT-AFTER-PRO-ADJUDICATION-001.yaml`, the manifest required Git blob SHA `c7af566921aa909c1a2a2e03ed63aa4b30de1135`; GitHub returned `6b4816d0baafc85787d0083f075b5d2c5afabcfd`. Readback isolated a one-token transcription defect in the sent content:

```diff
-- separate Owner decision whether to issue A1 controller G2A
+- separate Owner decision wheth to issue A1 controller G2A
```

Classification: manual tool-argument transcription mismatch during model-generated Base64 transport. The local payload/manifest remained correct. The mismatch was detected before tree, commit, ref or PR creation and permanently closed task 238.

The twelve returned blobs are unreferenced object-side effects. They are disclosed and must not be reused or cleaned up by MNEMOSYNE-239.
