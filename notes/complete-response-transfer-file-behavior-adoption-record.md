# Complete-Response Transfer-File Behavior Adoption Record

> User-approved behavior-guidance amendment. This record is not execution source; `current/human-approved-spec.md` remains the only execution source.

```yaml
decision_id: MNEMOSYNE-COMPLETE-RESPONSE-TRANSFER-FILE-001
implementation_task: MNEMOSYNE-155
post_merge_verification_task: MNEMOSYNE-156
decision_date: 2026-07-25
decision_source: current_Mnemosyne_maintenance_conversation
status: active_on_master
canonical_PR: 206
canonical_PR_URL: https://github.com/08822407d/Mnemosyne/pull/206
canonical_branch: mnemosyne-155-archive-pro-slice-specs-and-complete-response-guard
base_commit: 1e1334ad4dce36c2c47ffcfef3e90c9fd843815c
merge_commit: accaa83324418068ed5b1c32390139eb9ffe0d48
merged_at: 2026-07-26T02:42:24Z
post_merge_master: accaa83324418068ed5b1c32390139eb9ffe0d48
master_identical_to_merge_commit: true
active_guard: current/artifact-delivery-and-direct-generation-guard.md
guidance_loader: commands/load-mnemosyne-guidance.md
execution_source_modified: false
auto_merge: false
```

## User-observed failure

Recent Work and separate Pro tasks often required the operator to return both named artifacts and the executor's complete final response to the maintenance conversation. The taskbooks requested the named result files but did not explicitly require a downloadable copy of the complete response.

As a result, the operator repeatedly had to send an additional message asking the source conversation to export a response it had already issued.

## Adopted rule

When a task designer requires the complete final response to be returned or preserved:

- the taskbook must explicitly name a separate `<TASK_ID>-complete-response.md` or stable equivalent;
- the executor must generate it automatically in the same final response as the named artifacts;
- named synthesis/report/ledger files do not silently substitute for it;
- if the complete response and a substantive artifact differ, preserve and identify both;
- if they are byte-identical, disclose the relation but still deliver the required complete-response filename unless the operator waives it;
- the operator should not need a second export request.

The rule is conditional. Tasks that require only named artifacts do not need to export every reply.

For Deep Research, the canonical full report remains inline. A complete-response file is only an auxiliary transfer copy and cannot replace the full report body.

## Implementation and activation

MNEMOSYNE-155, through merged PR #206:

1. amended `current/artifact-delivery-and-direct-generation-guard.md` with the complete-response transfer-file rule;
2. updated `commands/load-mnemosyne-guidance.md` so task designers apply the rule during future cross-conversation task generation;
3. preserved the v1/v2 patch-specification lineage that demonstrated the operator burden and corrected desired delivery pattern.

MNEMOSYNE-156 verified that PR #206 merged as `accaa83324418068ed5b1c32390139eb9ffe0d48` and that current `master` was identical to that merge commit. The rule is therefore active for subsequent Mnemosyne task design.

## Boundary

This decision does not:

- require files for every ordinary reply;
- authorize external writes or forwarding;
- change the Deep Research inline-report requirement;
- make a complete-response copy an execution source;
- authorize background generation or unsupported delivery claims;
- authorize `PRO-SLICE-01` Phase A or Phase B implementation;
- treat a prior task's authorization as future precedent.