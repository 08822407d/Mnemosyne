# Meta-Agent Initial Persistent Memory System — Candidate Design v0.1

> Mnemosyne candidate design for a deliberately modest, file-based, human-reviewed Meta-Agent memory system after dedicated-repository migration. It is not Meta-Agent target truth, does not authorize implementation or activation, and must be reviewed against the migrated target package before adoption.

```yaml
design_id: MNEMOSYNE-META-AGENT-INITIAL-MEMORY-SYSTEM-CANDIDATE-001
created_by_task: MNEMOSYNE-191
version: 0.1.0
status: candidate_not_adopted_not_implemented
source_repository: 08822407d/Mnemosyne
source_baseline: 9e60fef75c524fc2e8acf227e84eaa820f08bc59
target_project: Meta_Agent
candidate_destination_repository: 08822407d/Meta-Agent
material_profile: public_synthetic_redacted_or_safe_pointer_only
RAG_required: false
MCP_required: false
automatic_writeback: false
automatic_methodology_promotion: false
operational_activation: false
```

## 1. Design basis

This design is constrained by the current Owner-accepted Meta-Agent baseline:

- exactly one declared target truth source;
- target truth remains inactive until a separate Owner activation decision;
- authority, current state, methodology, evidence, candidates and handoff remain distinguishable;
- public Git excludes private originals by default;
- project feedback cannot automatically rewrite general methodology;
- stable identity, versioning, migration mapping, validation and rollback are required;
- fresh sessions must recover without hidden prior-conversation assumptions;
- v0.1 assumes no RAG, MCP, auto-indexing, auto-writeback, autonomous self-modification or runtime multi-Agent coordination.

The accepted independent-wave evidence reinforces:

- one authority core;
- derived views as non-authoritative and rebuildable;
- source/influence boundaries;
- negative and contradictory evidence as first-class;
- risk-proportional assurance;
- human terminal judgment.

## 2. Problem statement

Meta-Agent already has a repository-backed memory/governance baseline, but it has grown beyond the original seven-file package and now includes:

- substantial research evidence;
- current state and handoff;
- migration records;
- candidates and pending work;
- repeated repository-task receipts;
- model/tool/surface facts with varying freshness;
- future need to design Agents for different projects without contaminating global methodology.

The initial memory system must make this material recoverable and governable without pretending that:

- Meta-Agent is mature;
- common domains are already known;
- user behavioral patterns are already validated;
- retrieval automation is already necessary;
- one successful case creates a universal method;
- public Git is an appropriate private-memory store.

## 3. Goals and non-goals

### 3.1 Goals

```yaml
goals:
  - preserve_one_authority_core
  - allow_fresh_session_recovery
  - distinguish_truth_state_method_evidence_candidate_and_inference
  - keep_source_and_owner_provenance
  - prevent_stale_navigation_and_candidate_resurrection
  - support_case_feedback_evaluation_and_method_promotion_without_auto_generalization
  - support_repository_migration_and_rollback
  - minimize_context_and_human_review_burden
  - grow_from_real_use_evidence
  - remain_usable_without_RAG_or_special_runtime
```

### 3.2 Non-goals

```yaml
non_goals:
  - persistent_hidden_user_profile
  - cognitive_or_psychological_inference_store
  - automatic_cross_project_memory_sharing
  - autonomous_methodology_learning
  - private_chat_or_voice_archive_in_public_Git
  - vector_database_or_embedding_pipeline
  - automatic_summarization_as_truth
  - universal_agent_design_ontology
  - complete_provider_capability_observatory
  - production_runtime_or_service
```

## 4. Design principles

1. **One truth, many memory roles.** Only the designated target truth governs accepted Meta-Agent design/governance; all other memory is role-labelled.
2. **Source before summary.** Every load-bearing summary or decision cites source artifacts and immutable refs where practical.
3. **Current state is disposable navigation.** It may be regenerated and must never override truth or history.
4. **Candidates stay quarantined.** File placement or model confidence cannot promote a candidate.
5. **Negative evidence persists.** Failed, blocked, stale, superseded and contradictory records remain discoverable enough to prevent resurrection.
6. **Freshness is explicit.** Time-sensitive platform/capability/state records carry observation time, source and supersession.
7. **Minimal context by profile.** Sessions load the smallest role-correct packet needed for the task.
8. **Derived views are rebuildable.** Indexes, summaries and normalized views are non-authoritative.
9. **Public-safe by default.** Private originals remain outside Git unless a future storage profile is separately approved.
10. **Use before overfitting.** Unknown domain and behavior patterns remain unknown until evidence accumulates.
11. **Review burden is a first-class metric.** A memory artifact that costs more to maintain than it saves should be simplified or retired.
12. **Migration is part of memory design.** Every durable object has lineage, supersession and rollback semantics.

## 5. Memory-plane architecture

```text
Owner decisions and sole target truth
                 |
                 v
      Authority / policy memory
                 |
                 v
   Current state and handoff memory
                 |
        +--------+---------+
        |                  |
        v                  v
Methodology memory   Case/evaluation memory
        |                  |
        +--------+---------+
                 v
       Candidate and research evidence
                 |
                 v
   Decision/version/migration history
                 |
                 v
   Rebuildable navigation and retrieval views
```

These are logical roles, not separate services or databases.

## 6. Proposed memory layers

### 6.1 Canonical target-truth layer

```yaml
layer_id: MA-MEM-LAYER-TRUTH
current_source: target-projects/meta-agent/current/approved-spec.md
candidate_destination: current/approved-spec.md
authority: sole_target_truth_after_separate_cutover_and_existing_activation_rules
write_gate: explicit_owner_authorized_target_change
memory_tier: hot
```

No other file may become truth by being newer, larger, under `current/`, or easier to retrieve.

### 6.2 Authority and source layer

```yaml
layer_id: MA-MEM-LAYER-AUTHORITY
current_source: target-projects/meta-agent/authority/source-and-owner-map.md
candidate_destination: authority/source-and-owner-map.md
contents:
  - owner_and_final_authority
  - source_classes_and_precedence
  - material_classes
  - repository_action_context
  - role_change_rules
memory_tier: hot
```

### 6.3 Meta-Agent-owned behavior-guidance layer

```yaml
layer_id: MA-MEM-LAYER-BEHAVIOR
current_source: temporary_Mnemosyne_compatibility_guard_plus_reviewed_Mnemosyne_behavior_semantics
candidate_destination:
  - current/meta-agent-behavior-guidance.md
  - commands/load-meta-agent-guidance.md
authority: owner_accepted_process_and_repository_safety_support_not_target_truth_by_itself
memory_tier: hot
```

It must preserve route isolation and repository safety while excluding Mnemosyne maintenance state.

### 6.4 Current-state layer

```yaml
layer_id: MA-MEM-LAYER-CURRENT
current_source: target-projects/meta-agent/current/active-context.md
candidate_destination: current/active-context.md
authority: navigation_only
memory_tier: hot
recompute_or_transform_on_migration: true
```

Required fields should include:

```yaml
current_state_minimum:
  repository_and_ref:
  route:
  phase:
  target_truth_path_and_effect:
  completed: []
  in_progress: []
  pending: []
  blocked: []
  deferred: []
  stale_or_superseded: []
  active_branch_or_PR_runtime_check:
  safe_next_action:
  last_verified_at:
```

Never encode a future PR number as a permanent prerequisite. Require runtime revalidation after merges.

### 6.5 Handoff layer

```yaml
layer_id: MA-MEM-LAYER-HANDOFF
current_source: target-projects/meta-agent/handoff/handoff-current.md
candidate_destination: handoff/handoff-current.md
authority: navigation_only
memory_tier: hot
regenerate_current_handoff_on_migration: true
```

A handoff contains reading order, boundaries, unresolved items and exactly one safe next action. It is not execution source.

### 6.6 Methodology layer

```yaml
layer_id: MA-MEM-LAYER-METHOD
current_source: target-projects/meta-agent/methodology/core-methodology.md
candidate_destination: methodology/core-methodology.md
authority: approved_method_support_only_when_referenced_by_target_truth
memory_tier: warm
```

Methods require stable IDs and cannot override target requirements or Owner decisions.

### 6.7 Case, feedback and evaluation layer

```yaml
layer_id: MA-MEM-LAYER-CASE
current_source: target-projects/meta-agent/cases/case-and-feedback-ledger.md
candidate_destination: cases/case-and-feedback-ledger.md
authority: scoped_evidence_and_candidate_only
memory_tier: warm
```

Initial volume remains low enough for one ledger. Split into per-case files only after measured size, contention or retrieval burden justifies it.

Future `MA-EVAL-*` objects may be issued after an approved schema revision and first bounded evaluation task.

### 6.8 Research-evidence layer

```yaml
layer_id: MA-MEM-LAYER-RESEARCH
current_source: target-projects/meta-agent/research/
candidate_destination: research/
authority: reviewed_non_execution_evidence
memory_tier: warm_and_cold
```

Default session loading should use manifests, identities, formal reviews and candidate ledgers. Raw long reports load on demand.

### 6.9 Candidate/incubator layer

```yaml
layer_id: MA-MEM-LAYER-CANDIDATE
current_source:
  - target-projects/meta-agent/candidates/
  - target-projects/meta-agent/decision-support/
candidate_destination:
  - candidates/
  - decision-support/
authority: candidate_or_decision_support_only
memory_tier: warm
```

A candidate must record acceptance gate, evidence, affected IDs, owner decision status and retirement/supersession.

### 6.10 Decision, version, migration and rollback layer

```yaml
layer_id: MA-MEM-LAYER-HISTORY
current_source: target-projects/meta-agent/history/decision-version-and-migration-log.md
candidate_destination: history/decision-version-and-migration-log.md
authority: reviewed_history_and_lineage
memory_tier: warm
```

Add target-specific migration records under `migration/` when their size or operational use makes a single log unwieldy, while keeping stable MA-MIG identity and a canonical index.

### 6.11 Migration-control layer

```yaml
layer_id: MA-MEM-LAYER-MIGRATION
current_source: target-projects/meta-agent/migration/
candidate_destination: migration/
authority: mapping_receipt_validation_and_rollback_support
memory_tier: warm_and_cold
```

It includes source manifests, destination mappings, copy validation, cutover decision, tombstone and rollback evidence.

### 6.12 Derived navigation and retrieval layer

```yaml
layer_id: MA-MEM-LAYER-DERIVED
candidate_destination:
  - memory/artifact-role-registry.yaml
  - memory/load-profiles.yaml
  - memory/indexes/active-memory-index.yaml
authority: non_authoritative_rebuildable
memory_tier: hot_as_navigation_only
```

Derived indexes always carry the source repository ref and may be discarded/rebuilt.

## 7. Candidate destination layout

```text
README.md
current/
  approved-spec.md
  active-context.md
  meta-agent-behavior-guidance.md
authority/
  source-and-owner-map.md
methodology/
  core-methodology.md
cases/
  case-and-feedback-ledger.md
history/
  decision-version-and-migration-log.md
handoff/
  handoff-current.md
  receipts/
research/
candidates/
decision-support/
migration/
memory/
  artifact-role-registry.yaml
  memory-object-envelope-v0.1.md
  retention-promotion-and-supersession-policy.md
  load-profiles.yaml
  indexes/
    active-memory-index.yaml
  validation/
    README.md
commands/
  load-meta-agent-guidance.md
notes/
  task-results/
```

This is a candidate layout. Exact mapping remains an Owner decision. Existing source IDs and roles must be preserved even if paths change.

## 8. Artifact-role registry

The registry should classify durable paths without making the registry authoritative over the artifacts themselves.

```yaml
artifact_role_entry:
  registry_entry_id:
  canonical_path:
  artifact_id:
  role:
  authority_class:
  status:
  memory_tier: hot | warm | cold
  owner:
  source_refs: []
  read_profiles: []
  write_gate:
  target_truth_effect:
  sensitivity_profile:
  freshness_rule:
  supersession_rule:
  retention_rule:
  derived_from: []
  validation_refs: []
```

Registry generation should be deterministic from reviewed front matter plus an explicit exceptions file. It must not infer authority solely from path.

## 9. Memory-object envelope for new records

Do not retroactively rewrite every existing file merely for schema uniformity. Apply the envelope prospectively and migrate legacy objects incrementally.

```yaml
memory_object:
  object_id:
  object_type:
  artifact_role:
  authority_class:
  status:
  scope:
  target_project: meta-agent
  created_at:
  last_updated_at:
  last_reviewed_at:
  source_refs: []
  evidence_refs: []
  owner_decision_ref:
  supersedes: []
  superseded_by: []
  freshness:
    time_sensitive: false
    observed_at:
    valid_until_or_review_trigger:
  sensitivity:
    class: public | synthetic | redacted | safe_pointer | private_outside_git
    storage_route:
  target_truth_effect: none | candidate | requires_authorized_change
  promotion_gate:
  retention:
  validation_refs: []
  limitations: []
```

## 10. Hot, warm and cold memory tiers

### 10.1 Hot memory

Loaded by most fresh sessions:

```yaml
hot:
  - current/approved-spec.md
  - authority/source-and-owner-map.md
  - current/meta-agent-behavior-guidance.md
  - current/active-context.md
  - handoff/handoff-current.md
  - memory/load-profiles.yaml
  - memory/indexes/active-memory-index.yaml
```

The index is navigation only. Missing canonical hot files is a blocking error.

### 10.2 Warm memory

Loaded by task profile:

```yaml
warm:
  - methodology/core-methodology.md
  - cases/case-and-feedback-ledger.md
  - history/decision-version-and-migration-log.md
  - active_candidates
  - research_manifests_reviews_and_candidate_ledgers
  - current_migration_records
  - future_capability_claim_registry
```

### 10.3 Cold memory

Loaded only for audit, dispute, migration or detailed research review:

```yaml
cold:
  - raw_long_research_reports
  - closed_task_receipts
  - historical_handoffs
  - superseded_candidates
  - failed_transport_or_incident_evidence
  - old_migration_parts
```

Cold material remains source-bound and discoverable but does not consume every session's context.

## 11. Deterministic load profiles

```yaml
load_profiles:
  MA_LOAD_CORE:
    purpose: recover_truth_authority_and_behavior
    required:
      - current/approved-spec.md
      - authority/source-and-owner-map.md
      - current/meta-agent-behavior-guidance.md

  MA_LOAD_CURRENT:
    purpose: resume_current_work
    extends: MA_LOAD_CORE
    required:
      - current/active-context.md
      - handoff/handoff-current.md

  MA_LOAD_DESIGN:
    purpose: design_or_review_an_Agent_or_workflow
    extends: MA_LOAD_CURRENT
    conditional:
      - methodology/core-methodology.md
      - relevant_candidates
      - relevant_case_and_research_reviews

  MA_LOAD_CASE:
    purpose: run_or_review_a_scoped_case
    extends: MA_LOAD_CORE
    required:
      - cases/case-and-feedback-ledger.md
    conditional:
      - relevant_method_refs
      - case_specific_evidence

  MA_LOAD_RESEARCH:
    purpose: evaluate_or_integrate_research
    extends: MA_LOAD_CORE
    required:
      - research_manifest
      - formal_reviews
    on_demand:
      - raw_reports

  MA_LOAD_MIGRATION:
    purpose: migrate_or_recover_repository_state
    extends: MA_LOAD_CURRENT
    required:
      - history/decision-version-and-migration-log.md
      - migration/current_manifest_and_mapping
      - rollback_record
```

Each load returns a receipt with repository/ref, loaded paths, missing paths, limitations and write authority.

## 12. Freshness and stale-state control

The PR #255 receive result exposed a recurring problem: current navigation retained pre-merge claims after merge.

Required controls:

```yaml
freshness_controls:
  current_state_records:
    require:
      - as_of_repository_ref
      - last_verified_at
      - runtime_open_PR_or_branch_check_when_relevant

  pending_PR_claims:
    rule: never_treat_cached_pending_state_as_runtime_fact_after_merge

  post_merge_closeout:
    required_for:
      - active_context
      - handoff
      - task_result_navigation

  historical_timepoint_records:
    rule: preserve_original_add_supersession_pointer

  product_and_capability_facts:
    require:
      - source
      - observed_at
      - freshness_or_recheck_trigger
```

The active-memory index should flag:

- references to closed or missing branches;
- `pending` records whose PR is merged/closed;
- current files pointing to superseded safe next actions;
- destination refs that do not exist;
- conflicting active writers.

## 13. Evidence, candidate and promotion lifecycle

```text
raw or reviewed evidence
  -> scoped observation
  -> competing explanations
  -> target-specific lesson
  -> candidate requirement/method/schema/policy change
  -> impact and generalizability review
  -> acceptance criteria and regression/semantic review
  -> Owner decision
  -> authorized update and version/migration record
  -> current state and handoff synchronization
```

Statuses should include:

```yaml
lifecycle_status:
  - raw
  - reviewed_evidence
  - target_specific_observation
  - candidate
  - needs_more_evidence
  - accepted
  - rejected
  - narrowed
  - deprecated
  - retired
  - superseded
  - reopened
```

No numeric promotion threshold is fixed before real case calibration.

## 14. Case and feedback memory

The existing ledger remains the initial canonical case/feedback memory.

### 14.1 First-use rules

- start with public/synthetic or explicitly redacted cases;
- define success and failure before preferred output review where practical;
- record producer claims separately from verifier findings;
- preserve blocked and failed cases;
- record model/tool/surface limitations;
- do not generalize user preference or one case automatically.

### 14.2 Conversation-trace review

Full conversations may be valuable for post-hoc frontier review, but public Git should store only:

```yaml
conversation_review_record:
  case_ref:
  external_private_or_redacted_trace_ref:
  material_authorization_ref:
  reviewer_model_surface:
  observed_patterns: []
  alternative_explanations: []
  target_specific_lessons: []
  candidate_general_lessons: []
  privacy_and_bias_limitations: []
  owner_decision_ref:
```

Raw private conversations remain outside Git unless separately approved.

## 15. User and behavioral memory boundary

Meta-Agent should not construct a hidden general user profile.

Allowed:

- explicit Owner decisions;
- user-confirmed preferences with scope and revision right;
- case-specific observations;
- opt-in, bounded, purpose-specific operational preferences;
- redacted/safe-pointer evidence under approved storage.

Prohibited by default:

- inferred psychological traits;
- global cognitive or learner profiles;
- sensitive behavioral prediction;
- cross-project preference propagation without confirmation;
- treating interaction frequency as consent;
- public storage of raw personal traces.

Candidate preference record:

```yaml
confirmed_preference:
  preference_id:
  statement:
  scope:
  confirmed_by_user:
  confirmed_at:
  source_ref:
  validity_or_review_trigger:
  sensitive: false
  cross_project_use_authorized: false
  supersedes: []
```

## 16. Capability and tool memory

A future minimal capability-claim registry may be useful, but should remain evidence-bound and small.

```yaml
capability_claim:
  claim_id:
  actor_or_surface:
  capability:
  evidence_type:
  observed_at:
  repository_or_task_scope:
  confidence_with_rationale:
  limitations:
  freshness_or_recheck_trigger:
  fallback:
  target_authority_effect: none
```

Do not infer write capability from repository visibility or persistent permission. Do not infer hidden backend identity from UI labels, style or speed.

## 17. Retention, supersession and anti-resurrection

```yaml
retention_defaults:
  target_truth_and_owner_decisions: preserve
  approved_methods: preserve_with_supersession
  current_state: replace_but_keep_reviewable_history_or_commit_lineage
  handoff: regenerate_current_preserve_material_historical_receipts
  case_feedback_evidence: preserve_including_negative_results
  research_originals_and_identity: preserve
  candidates: preserve_minimum_status_after_reject_or_retire
  derived_indexes: recompute
  ephemeral_scratch: retire_unless_promoted
  secrets_or_unauthorized_private_material: do_not_store
```

Retired objects retain tombstones containing stable ID, status, successor and reopening gate.

## 18. Derived index design

Candidate `memory/indexes/active-memory-index.yaml`:

```yaml
active_memory_index:
  generated_from_repository:
  generated_from_commit:
  generated_at:
  generator_version:
  target_truth:
  current_state:
  current_handoff:
  behavior_guidance:
  active_methods: []
  active_cases: []
  active_candidates: []
  current_migration:
  current_open_decisions: []
  current_blockers: []
  stale_or_conflicting_refs: []
  validation_result:
  authoritative: false
```

It must be reproducible and never manually edited as a second state source.

## 19. Validation and observability

Minimum validation families:

1. exact path/ID/front-matter checks;
2. unique truth-source check;
3. role and authority separation;
4. fresh-session recovery;
5. stale-state detection;
6. case-feedback no-auto-promotion;
7. private-material and hidden-profile rejection;
8. negative-evidence preservation;
9. derived-index deterministic rebuild;
10. migration mapping and no-dual-writer;
11. rollback and tombstone;
12. review burden and context load measurement.

Observe:

```yaml
metrics:
  fresh_session_recovery_time:
  required_file_count_by_profile:
  missing_or_stale_ref_rate:
  user_correction_count:
  reviewer_rework_time:
  false_promotion_or_role_confusion_count:
  retrieval_miss_count:
  derived_index_rebuild_repeatability:
  case_to_method_promotion_lead_time:
```

No universal thresholds are assumed before baseline measurement.

## 20. RAG and automation trigger

RAG, embeddings or auto-indexing should be considered only when measured evidence shows that deterministic files/load profiles are insufficient.

Possible triggers:

- repeated failure to locate relevant evidence despite correct load profile;
- sustained growth in case/research volume;
- unacceptable fresh-session navigation time;
- recurring cross-file queries that cannot be handled by deterministic indexes;
- demonstrated value in a public/synthetic evaluation.

Required before adoption:

```yaml
RAG_gate:
  source_binding: required
  index_non_authoritative: true
  rebuildability: required
  retrieval_and_generator_tests: separate
  prompt_injection_and_data_boundary_test: required
  private_material_profile: separate_owner_decision
  manual_fallback: required
  rollback: required
```

## 21. Staged adoption plan

### Stage M0 — migration-preserving baseline

Migrate the existing package, target-owned behavior guidance, mapping and rollback. Do not add nonessential memory schema.

### Stage M1 — memory foundation

After destination-only recovery passes, propose:

- artifact-role registry;
- prospective memory-object envelope;
- load profiles;
- freshness/supersession policy;
- deterministic active-memory index.

### Stage M2 — first synthetic cases

Run a small public/synthetic case lifecycle and verify feedback/evaluation/promotion boundaries.

### Stage M3 — bounded real use

Only after operational scope and material policy are approved. Collect review burden, corrections, retrieval misses and outcome evidence.

### Stage M4 — evidence-driven expansion

Consider capability registry, per-case split, private store, RAG, MCP or automation only when measured need and risk gates justify them.

## 22. Migration alignment recommendation

```yaml
recommended_for_migration_shadow_PR:
  - existing_Meta_Agent_target_tree_after_reviewed_mapping
  - Meta_Agent_owned_behavior_guidance_candidate
  - load_meta_agent_guidance_command
  - migration_manifest_mapping_validation_and_rollback
  - source_history_pointers

recommended_for_separate_post_migration_memory_PR:
  - artifact_role_registry
  - memory_object_envelope
  - load_profiles
  - freshness_retention_and_supersession_policy
  - active_memory_index
  - validation_scaffolding

reason:
  - separate_copy_and_cutover_from_memory_schema_expansion
  - reduce_review_surface
  - preserve_clear_rollback
  - allow_destination_only_recovery_before_new_design_adoption
```

The Meta-Agent route may recommend a different split after exact manifest and mapping review, but must record the authority and rollback implications.

## 23. Acceptance criteria for this design candidate

This design is ready for a target adoption decision only when:

```yaml
candidate_acceptance:
  migrated_target_paths_and_roles_verified: true
  target_owned_behavior_guidance_defined: true
  memory_components_mapped_to_current_artifacts: true
  no_second_truth_source: true
  no_private_material_route_assumed: true
  no_hidden_user_profile: true
  no_auto_promotion: true
  load_profiles_and_fresh_session_tests_defined: true
  stale_state_and_supersession_tests_defined: true
  rollback_and_no_dual_writer_defined: true
  Owner_decision_package_complete: true
```

## 24. Open questions preserved

```yaml
open_questions:
  - exact_destination_root_layout
  - whether_memory_foundation_is_included_in_shadow_PR_or_separate_PR
  - first_authorized_case_scope
  - future_MA_EVAL_schema
  - capability_claim_registry_minimum
  - private_material_store_and_access_method
  - measured_RAG_need
  - acceptable_review_and_context_burden
  - operational_activation_scope
```

These are not silently defaulted by this design.

## 25. Boundaries

This design does not:

- modify Meta-Agent target truth or methodology;
- issue new `MA-*` stable IDs;
- authorize migration, destination initialization, target PR or cutover;
- authorize real cases, private material, operational use or pilot;
- require RAG, MCP, database, runtime service or automation;
- make Mnemosyne a second Meta-Agent truth source;
- guarantee behavior quality without post-migration validation and real-use evidence.
