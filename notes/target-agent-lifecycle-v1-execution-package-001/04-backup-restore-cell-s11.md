# V1 Backup and Restore Cell — S11

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
cell_id: TLR-V1-CELL-S11-001
status: prepared_not_executed
selected_scenario: S11
real_backup_configuration: prohibited
```

## 1. Cell purpose

This cell tests only the synthetic backup semantics in candidate v0.2:

- the primary target is the sole current truth before loss;
- backup A and backup B are source-identified, non-authoritative snapshots;
- backups do not evolve independently;
- one backup may fail without destroying both copies;
- the surviving backup can restore the required target state;
- the restored target is mechanically related to the exact recorded source;
- no parent/meta repository is used as a recovery copy.

It does not configure any real backup provider, account, credential, synchronization job or real target retention policy.

## 2. Required inputs

Read only:

- candidate v0.2 backup section;
- validation v0.2 S11 contract;
- frozen package README and files `01`, `02`, `03`, `04`;
- exact Owner V1 authorization;
- execution-package README;
- controller/fixture receipts;
- exact fixture commit and Alpha source identity;
- this cell contract.

Do not read Meta-Agent or a real target beyond the controller's named no-write-ref checks.

## 3. Task contract

```yaml
task_id: TLR-V1-S11-001
scenario_id: S11
branch: tlr-v1-s11-backup-restore
base: fixture_commit
authority_owner: synthetic-alpha-owner
primary_writer: S11_backup_restore_worker
allowed_write_roots:
  - targets/agent-alpha/
  - backups-fixture/backup-a/
  - backups-fixture/backup-b/
  - backups-fixture/restore-work/
  - run-evidence/S11/
prohibited_write_roots:
  - libraries/
  - shared/
  - repository-governance/
  - targets/agent-beta/
```

The exact source state is Alpha at the pinned fixture commit before any S11 write.

## 4. Source identity receipt

Before snapshot creation record:

```yaml
S11_source_receipt:
  source_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  source_branch: tlr-v1-fixture-base
  source_commit:
  source_tree:
  source_target_root: targets/agent-alpha/
  source_target_tree_or_content_identity:
  authority_owner: synthetic-alpha-owner
  required_restore_records:
    - authority.yaml
    - current.md
    - requirements/
    - src/
    - tests/
    - dependencies.yaml
  prohibited_independent_writers:
    - backup-a
    - backup-b
```

If a mechanically comparable subtree identity cannot be obtained, record deterministic file/blob inventory and content hashes sufficient to prove equality. A narrative “looks the same” comparison is not enough.

## 5. Snapshot creation

Create backup A and B as separate synthetic snapshot directories.

Each snapshot contains:

- the approved Alpha content scope;
- a snapshot manifest naming the exact source repository, commit, target root and integrity identity;
- `independent_editing_allowed: false`;
- creation commit and each file blob identity;
- no current-truth or authority claim.

Required manifest:

```yaml
backup_snapshot:
  snapshot_id:
  target_id: agent-alpha
  source_repository:
  source_commit:
  source_target_root:
  source_integrity_identity:
  backup_location:
  content_scope: []
  snapshot_commit:
  snapshot_content_identity:
  independent_editing_allowed: false
  authority_owner: none_backup_is_non_authoritative
  restore_test_ref:
```

The two snapshots must be independently addressable within the synthetic fixture. This tests semantics, not real provider independence.

## 6. Simulated failures and restore

Perform the frozen sequence while preserving each attempt:

1. pin the source receipt;
2. create backup A and backup B;
3. verify both against the source identity;
4. simulate primary loss on the S11 branch by removing or moving the Alpha primary into a clearly non-current test state;
5. simulate backup A failure by making it unavailable for restore without altering backup B;
6. select backup B as the restore source;
7. restore Alpha into the exact primary target root;
8. re-establish the original Alpha authority record from the snapshot; do not make backup B the authority owner;
9. compare restored content to the recorded source identity;
10. record all deletions, moves, failures and restore commits.

A failed attempt must remain in Git history and the incident ledger. Do not rewrite the branch to make the failure disappear.

## 7. Required restore proof

```yaml
backup_restore_result:
  scenario_id: S11
  source_repository:
  source_commit:
  source_target_identity:
  snapshots:
    - snapshot_id: backup-a
      location:
      source_identity:
      snapshot_identity:
      independent_editing_allowed: false
    - snapshot_id: backup-b
      location:
      source_identity:
      snapshot_identity:
      independent_editing_allowed: false
  simulated_failures:
    - primary_loss
    - backup_a_unavailable
  restore_source: backup-b
  restored_target_root: targets/agent-alpha/
  restored_commit:
  restored_target_identity:
  required_records_recovered: []
  authority_after_restore: synthetic-alpha-owner
  backup_promoted_to_authority: false
  mismatches: []
  disposition:
```

A pass requires exact equality for the approved source scope and recovery of every required record.

## 8. Mechanical checks

At minimum run:

- M2 one canonical task branch;
- M3 declared versus actual write set;
- M5 authority preservation before and after restore;
- M6 no parent/meta recovery copy;
- M9 source/snapshot/restore identity and one-backup-failure survival;
- M11 exact input/output/attempt/commit/blob identity.

Also verify:

- no snapshot commit becomes an independent development lineage;
- no post-snapshot mutation is made inside a backup and then treated as source truth;
- Beta, CommonLib, shared schema and governance paths remain unchanged.

## 9. Failure classes

S11 fails when:

- source commit/tree cannot be established;
- a snapshot lacks source identity;
- backup A and B both disappear under one simulated failure;
- backup content diverges from the source before restore;
- backup B is promoted to authority/current truth rather than used as restore material;
- restored content differs from the approved source scope;
- required authority/current/requirements/source/tests/dependency records are missing;
- a parent/meta location is used as backup;
- write scope or output identity is violated.

## 10. Cell result

```yaml
backup_restore_cell_result:
  cell_id: TLR-V1-CELL-S11-001
  task_id: TLR-V1-S11-001
  branch:
  source_receipt_ref:
  source_commit:
  source_identity:
  snapshot_refs: []
  snapshot_commits: []
  simulated_failure_refs: []
  restore_result_ref:
  restored_commit:
  restored_identity:
  required_records_recovered: []
  declared_vs_actual_write_set:
  mechanical_checks: {}
  critical_failures: []
  incidents_and_retries: []
  provisional_disposition:
```

## 11. Stop rules

Stop when source identity, authority, content scope or exact restore comparison is missing; when a real backup/service would be needed; when an action would touch a real repository; when a backup would need independent edits; or when candidate/package semantics would need revision.