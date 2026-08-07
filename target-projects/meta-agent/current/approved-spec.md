---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-APPROVED-SPEC-001
artifact_role: retired_historical_target_truth_redirect
status: superseded_by_dedicated_repository_cutover
authority_level: historical_redirect_only
target_runtime_truth_source_designated: false
target_runtime_truth_source_effective: false
effective_for_operational_use: false
target_truth_source: false
owner: user
last_updated_by_task: MNEMOSYNE-META-AGENT-SOURCE-RETIREMENT-001

superseded_by:
  repository: 08822407d/Meta-Agent
  branch: master
  path: current/approved-spec.md
  cutover_PR: 3
  cutover_merge_commit: eb71ed350e7cf1783d73580466a3656fad2a3b69

historical_original:
  repository: 08822407d/Mnemosyne
  commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  path: target-projects/meta-agent/current/approved-spec.md

rollback:
  historical_snapshot_reactivation_requires_explicit_Owner_decision: true
  automatic_reactivation: prohibited
---

# Meta-Agent v0.1 Historical Target-Truth Redirect

This Mnemosyne path is retired and is **not** Meta-Agent target truth, current state, or an active write target.

The sole current Meta-Agent target-truth location is:

```text
Repository: 08822407d/Meta-Agent
Branch: master
Path: current/approved-spec.md
Cutover PR: 08822407d/Meta-Agent#3
Cutover merge: eb71ed350e7cf1783d73580466a3656fad2a3b69
```

The complete pre-cutover content remains recoverable from the immutable historical snapshot:

```text
08822407d/Mnemosyne@8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb:
target-projects/meta-agent/current/approved-spec.md
```

That snapshot may regain authority only through a separate, explicit Owner-approved rollback. Its presence in Git history does not create a second truth source or writer.

Repository cutover does not equal operational activation. The dedicated-repository target truth remains ineffective for operational use unless the Owner separately authorizes an exact operational scope.
