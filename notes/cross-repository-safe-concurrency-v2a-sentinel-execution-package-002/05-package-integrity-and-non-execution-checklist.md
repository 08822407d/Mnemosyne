# V2-A A0 Sentinel — Package Integrity and Non-Execution Checklist v2

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-INTEGRITY-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
status: preparation_checklist_not_run_authorization
```

## 1. Required package files

```text
README.md
00-controller-receive-and-surface-contract.md
01-package-and-source-manifest.md
02-next-tier-controller-task.md
03-mechanical-checks-and-result-template.md
04-startup-message.md
05-package-integrity-and-non-execution-checklist.md
```

All seven must exist before package 002 is complete.

## 2. Required decision artifact

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002.md
```

The later Owner G2A authorization must name the exact merged blobs of the decision candidate and source manifest.

## 3. Protocol-repair checks

Confirm:

- package 001 remains preserved and is not silently rewritten;
- `V2A-SENTINEL-PROTOCOL-DEFECT-001` is recorded;
- package publication commit is not treated as the execution-window no-write baseline;
- source integrity uses exact load-bearing blob identities;
- execution-window Mnemosyne/Meta-Agent masters are supplied only after package merge by the Owner G2A authorization;
- validation master/fixture/V1 refs remain hard-pinned;
- no dynamic ref can be silently refreshed by the controller;
- a protected-ref mismatch blocks before branch creation;
- no extra Mnemosyne publication step is required between G2A authorization and A0 launch.

## 4. Preserved A0 semantics

Confirm package 002 retains:

- A0 only;
- existing public synthetic validation repository;
- validation `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`;
- read-only `tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6`;
- fixture tree `f1e221ce8aef404579b96adb3ab01319016889db`;
- full historical V1 ref inventory;
- future controller branch `v2a-sentinel-001-controller`;
- no worker branches or PR;
- exact seven-file result write set;
- visible model verbatim receipt and no substitution;
- no retry/repair/hidden continuation;
- fresh Pro post-run adjudication.

## 5. Preparation-task non-execution checklist

All must remain false for MNEMOSYNE-224:

```yaml
validation_repository_written: false
validation_repository_branch_created: false
A0_executed: false
A1_to_A7_executed: false
V2_B_executed: false
V2_C_executed: false
connector_or_app_changed: false
external_quota_consumed: false
web_or_Deep_Research_or_Fable_started: false
private_or_real_target_material_used: false
Meta_Agent_modified: false
real_target_modified: false
execution_source_modified: false
Target_Lifecycle_candidate_v0_2_modified: false
lock_or_lease_service_created: false
GitHub_Actions_or_merge_queue_configured: false
automatic_retry_or_compensation: false
reset_or_force_push: false
```

## 6. PR preflight

Before publication:

- re-read latest Mnemosyne `master`;
- enumerate open Mnemosyne PRs;
- confirm no duplicate MNEMOSYNE-224 branch/PR;
- compare exact changed paths;
- confirm branch not behind master;
- confirm old package 001 files unchanged;
- confirm no validation-repository write;
- confirm controller branch absent;
- confirm package file count is seven;
- confirm decision candidate and manifest identities;
- create one Ready PR, not Draft;
- do not auto-merge.

## 7. Post-merge G2A gate

After package 002 merges, Pro must re-read:

- latest Mnemosyne master;
- exact decision-candidate-002 blob;
- exact manifest-002 blob;
- load-bearing source blobs;
- validation master/fixture/V1 refs;
- controller branch absence;
- Meta-Agent current master;
- repository visibility/permissions;
- open PRs;
- current user-visible model availability.

Then, and only then, present an Owner G2A authorization containing exact execution-window protected refs. **Do not create another Mnemosyne authorization PR after those refs are frozen**, because that would change the very baseline being authorized.

The Owner's natural-language authorization is the authority record for A0 and is copied verbatim into the controller output; durable run evidence is written to the authorized validation branch.

## 8. Historical integrity

Do not alter:

- Fable source/report cycle;
- 30-file research snapshot;
- package 001 files;
- V1 raw controller evidence;
- prior Pro/Owner decisions;
- MNEMOSYNE-223 records describing the discovered pre-repair package.

The repair is additive and explicitly superseding only for the affected pre-run binding scope.
