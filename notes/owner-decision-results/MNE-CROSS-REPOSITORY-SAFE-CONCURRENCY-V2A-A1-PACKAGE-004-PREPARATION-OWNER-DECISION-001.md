# V2-A A1 Package 004 — Owner Preparation Authorization 001

```yaml
decision_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004-PREPARATION-OWNER-DECISION-001
task_id: MNEMOSYNE-233
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
decision_status: OWNER_AUTHORIZED_MINIMUM_SOURCE_IDENTITY_AND_HANDOFF_REPAIR_PREPARATION
source_instruction: current_conversation_direct_instruction
source_master_at_authorization: b70acfc8ab190f18fdd987f034963039728ca887
```

The Owner authorized one follow-up Mnemosyne lineage to:

- independently reconstruct the five-part archived review and verify the 37,074-byte source SHA-256;
- record `MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001`;
- preserve packages 001, 002 and 003 unchanged;
- prepare additive run-decision candidate 004 and package 004;
- correct the archive-manifest identity from `7c2af723c395283aca23a5240847e46e6c97e93b` to `6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a`;
- update the current F2 route state;
- prepare corrected handoff package 002, startup prompt 002 and a mandatory post-merge receive-rehearsal contract;
- create one Ready PR;
- add a detailed, durable TODO for later general handoff correctness validation and protocol hardening.

The detailed TODO must preserve these Owner requirements:

1. determine whether a reliable handoff-correctness validation design already exists;
2. if absent, design one; if present, treat observed failures as evidence that the design is unrealistic, defective, or was not correctly loaded/applied;
3. consider exporting prior source/receiver handoff conversations as files for independent Pro and Fable 5 “god-view” analysis;
4. design a flow in which the old conversation prepares the handoff under Pro, the new conversation's first receive reply is returned to the old conversation, and the old conversation can judge correctness with a next-tier model or at most one Pro turn;
5. design the startup flow so the new conversation itself loads the exact project/Agent guidance selected by the old conversation when such guidance is required.

Excluded:

```yaml
A1_G2A: false
A1_execution: false
validation_repository_write: false
validation_branch_creation_or_movement: false
package_001_002_003_in_place_edit: false
A2_to_A7_or_V2_B_or_V2_C: false
Meta_Agent_or_real_target_write: false
global_handoff_guidance_modification_in_this_task: false
conversation_export_or_external_Pro_Fable_run_in_this_task: false
auto_merge_cleanup_or_branch_deletion: false
```

This authorization is task-local and is not future precedent.
