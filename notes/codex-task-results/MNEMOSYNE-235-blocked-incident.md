# MNEMOSYNE-235 — Blocked Publication Incident

```yaml
task_id: MNEMOSYNE-235
disposition: BLOCKED_CLOSED_NO_RETRY
repository: 08822407d/Mnemosyne
base: e726dea818dca9418181775d0e7dcd62eb6c464a
reachable_content_commit_created: false
pull_request_created: false
G2A_issued: false
A1_executed: false
```

The source ZIP and manifest were correct. During pre-commit tree staging, an executor manually changed the uppercase task-ID filename component `G2A-COMPOSITE-CLOSURE-001` to a lowercase/mixed-case directory-style spelling in one transient tree entry. The run detected the mismatch and stopped before commit/ref movement.

The canonical recovery branch was created at the original base and remains empty. Unreferenced objects may exist; their SHAs were not preserved. `ref_not_moved` does not mean `zero_repository_side_effect`. No cleanup or reuse is authorized.
