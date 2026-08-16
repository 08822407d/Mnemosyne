# V2-A A0 Sentinel — Package Integrity and Non-Execution Checklist

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-INTEGRITY-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
status: design_and_run_package_checklist
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

Required file count: `7`.

The run-decision candidate is outside the package directory:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001.md
```

## 2. Semantic integrity checklist

Confirm:

- only A0 is selected;
- no A1–A7 semantics are executed or pre-authorized;
- existing validation repository is reused rather than a new repository being created;
- validation-repository master is the controller base, not a write target;
- `tlr-v1-fixture-base` is read-only;
- all existing V1 refs are protected;
- only one controller branch is planned;
- no worker branch or PR is planned;
- exact seven-file output scope is frozen;
- source/package identities are blob-bound;
- model substitution is fail-closed;
- physical connector capability is separated from task authorization;
- no-write evidence is limited to named refs, time window and accessible surfaces;
- A0 PASS does not imply full V2-A execution, production readiness or target adoption;
- fresh Pro adjudication is mandatory after a run.

## 3. Current preparation-task non-execution checklist

For MNEMOSYNE-223 all values must remain:

```yaml
validation_repository_created: false
validation_repository_written: false
validation_repository_branch_created: false
V2_A_controller_or_worker_launched: false
A0_executed: false
A1_to_A7_executed: false
V2_B_or_V2_C_executed: false
connector_or_app_enabled_or_changed: false
external_quota_consumed: false
web_Deep_Research_or_Fable_started: false
private_or_real_target_material_used: false
Mnemosyne_execution_source_modified: false
Meta_Agent_modified: false
real_target_modified: false
Target_Lifecycle_candidate_v0_2_modified: false
lock_or_lease_service_created: false
GitHub_Actions_or_merge_queue_configured: false
automatic_compensation_or_reset_or_force_push: false
```

Any true value invalidates a “prepare only” claim.

## 4. Source identity checklist before PR

Record exact blobs for:

- Owner Option A decision;
- F2 fresh Pro adjudication;
- accepted amendment candidate;
- V2 staged validation design;
- all nine V2 package files;
- current F2 status before MNEMOSYNE-223;
- run-decision candidate;
- all seven A0 sentinel package files;
- updated F2 status;
- MNEMOSYNE-223 result, verification and finalization records.

The source manifest does not recursively hash itself. Its own blob is recorded in the verification/finalization records.

## 5. Repository/branch preflight before publication

Before creating the Mnemosyne PR:

- re-read latest Mnemosyne `master`;
- enumerate all accessible open Mnemosyne PRs;
- confirm no existing MNEMOSYNE-223 branch/PR/result or equivalent sentinel scope;
- verify the canonical branch is not behind `master`;
- inspect exact changed paths;
- verify only Mnemosyne design/status/result paths changed;
- verify validation repository, Meta-Agent and real targets were not written;
- verify `current/human-approved-spec.md` is unchanged;
- verify package file count is seven;
- verify run-decision and package semantics contain no execution authorization;
- create one Ready PR, not Draft, because the preparation scope is complete;
- do not auto-merge.

## 6. G2A invalidation preflight

After this package merges but before asking the Owner to authorize execution, recheck:

- Mnemosyne exact source commit and blobs;
- validation repository master and public visibility;
- fixture ref/commit/tree;
- all protected V1 refs;
- Meta-Agent master;
- controller branch absence;
- open PR absence or non-conflict;
- visible model option availability;
- GitHub connector branch/ref/write capabilities;
- output path and retention decisions.

Any mismatch requires a Pro refresh. Do not ask the Owner to authorize a stale package.

## 7. Post-run retention candidate

If A0 is later authorized and executed:

- keep `v2a-sentinel-001-controller` until fresh Pro adjudication and exact identity preservation;
- do not merge or delete it during the controller run;
- only the responsible post-review route may release the branch;
- no validation-repository archival/deletion is implied.

## 8. Capability and research boundary

```yaml
A0_executor_capability: NEXT_TIER_SUFFICIENT_CANDIDATE
A0_fresh_adjudication_capability: FRONTIER_REQUIRED
Deep_Research: NOT_NEEDED
parallel_Fable_or_frontier_research: NOT_NEEDED_BEFORE_A0
human_authority: G2A_execution_and_any_later_stage_selection
```

The package is invalid if a controller needs frontier design work to complete A0. It must stop and return rather than improvise.
