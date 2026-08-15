# MNE-DR-003 Display-Name Allocation Collision — 2026-08

```yaml
incident_id: MNE-RESEARCH-DISPLAY-NAME-COLLISION-001
status: contained
run_display_name: MNE-DR-003 能力归属
conflicting_durable_alias: MNE-DR-003 生命周期验证
canonical_alias_for_stored_capability_research: MNE-DR-004 能力归属
canonical_task_id_unchanged: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
research_result_invalidated: false
```

## What happened

The capability-ownership task was prepared and run using sequence 003 while another active conversation independently prepared and merged the Target Lifecycle V1 package, which durably assigned sequence 003 to `MNE-TARGET-LIFECYCLE-V1-001`.

The research report's original display name remains unchanged as historical run metadata. Long-term repository navigation assigns the capability-ownership research sequence 004.

## Cause

The display-name registry had a read-to-write race: reading `next_unallocated_sequence` did not reserve it. Preparation of a task package and durable registry allocation were separate actions across conversations.

## Containment

- preserve all original run artifacts unchanged;
- keep canonical task IDs distinct;
- allocate `MNE-DR-004 能力归属` for repository navigation;
- advance the next free Mnemosyne sequence to 005;
- do not reinterpret the visible run label as backend identity.

## Follow-up candidate

A future registry repair may add an explicit reservation/commit protocol or require allocation to be durably written before the user is instructed to create the external workspace. This incident does not itself modify the active display-name guard.
