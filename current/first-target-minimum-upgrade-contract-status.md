# First-Target Minimum Upgrade Contract — Historical Pilot Status

> Non-execution-source historical status for the first Meta-Agent target-specific upgrade-contract pilot. Current Meta-Agent truth and state are in `08822407d/Meta-Agent`.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-006
last_updated_by_task: MNEMOSYNE-195
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
advisory_pilot_checklist: notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
status: TARGET_SPECIFIC_DESIGN_PILOT_COMPLETED_AND_MIGRATED
historical_disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
selected_target_project: meta-agent
current_target_repository: 08822407d/Meta-Agent
current_target_truth_path: current/approved-spec.md
operational_use_authorized: false
global_template_promotion: false
```

## 1. Historical pilot result

The original Mnemosyne-hosted Meta-Agent v0.1 package demonstrated that a compact file-based target package could start with:

- stable IDs;
- one designated but inactive target truth;
- source and authority separation;
- compact design/schema/policy/delivery versions;
- preserve/transform/recompute/retire decisions;
- migration mapping and rollback;
- bounded next-tier execution and frontier escalation;
- no RAG, MCP, auto-indexing, or auto-writeback requirement.

The design-time checklist result remains:

```yaml
result: PASS_FOR_TARGET_SPECIFIC_DESIGN_USE
operational_use_authorized: false
universal_template_promotion: false
```

## 2. Real migration evidence now exists

The former status said real migration cost and success had not been tested. That statement is superseded.

```yaml
real_repository_migration:
  source_snapshot: 08822407d/Mnemosyne@8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  destination_repository: 08822407d/Meta-Agent
  imported_files: 226
  byte_exact_files: 224
  intentionally_transformed_files: 2
  missing_files: 0
  destination_recovery: PASS
  target_truth_cutover: true
  no_active_dual_writer: PASS
  Mnemosyne_source_retirement: true
```

This supports the value of early stable identity, migration mapping, and rollback. It does not prove that every future target should use the same schema or burden.

## 3. Current authority boundary

The active target-specific contract and current state belong to the dedicated repository. Mnemosyne retains:

- generic candidate design and checklist;
- historical pilot records;
- migration evidence;
- lessons for future target-memory design.

The old Mnemosyne target path is not current target truth or an active writer.

## 4. Remaining evidence gaps

```yaml
not_yet_measured:
  - sustained_operational_review_burden
  - first_real_case_update_cost
  - long_term_drift_and_retrieval_behavior
  - private_material_profile
  - RAG_or_MCP_value
  - automatic_upgrade_or_writeback_safety
```

No global template promotion follows automatically from one successful repository migration.

## 5. Safe next action

```yaml
Mnemosyne:
  - use_the_completed_migration_as_evidence_for_future_target_memory_design
  - revise_the_generic_contract_only_under_a_separate_selected_task
Meta_Agent:
  - continue_target_specific_work_only_in_08822407d_Meta_Agent
operational_activation: false
```
