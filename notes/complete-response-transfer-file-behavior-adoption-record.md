# Complete-Response Transfer-File Behavior Adoption Record

> User-approved behavior-guidance amendment. This record is not execution source; `current/human-approved-spec.md` remains the only execution source.

```yaml
decision_id: MNEMOSYNE-COMPLETE-RESPONSE-TRANSFER-FILE-001
implementation_task: MNEMOSYNE-155
decision_date: 2026-07-25
decision_source: current_Mnemosyne_maintenance_conversation
status: approved_pending_PR_206_merge
canonical_PR: 206
canonical_PR_URL: https://github.com/08822407d/Mnemosyne/pull/206
canonical_branch: mnemosyne-155-archive-pro-slice-specs-and-complete-response-guard
base_commit: 1e1334ad4dce36c2c47ffcfef3e90c9fd843815c
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

## Implementation

MNEMOSYNE-155, through PR #206:

1. amends `current/artifact-delivery-and-direct-generation-guard.md` with the complete-response transfer-file rule;
2. updates `commands/load-mnemosyne-guidance.md` so task designers apply the rule during future cross-conversation task generation;
3. preserves the v1/v2 patch-specification lineage that demonstrated the operator burden and the corrected desired delivery pattern.

The rule becomes active on `master` only after PR #206 is human-merged. PR creation does not activate it on the default branch.

## Boundary

This decision does not:

- require files for every ordinary reply;
- authorize external writes or forwarding;
- change the Deep Research inline-report requirement;
- make a complete-response copy an execution source;
- authorize background generation or unsupported delivery claims;
- merge PR #206 or enable auto-merge;
- authorize `PRO-SLICE-01` Phase A or Phase B implementation.