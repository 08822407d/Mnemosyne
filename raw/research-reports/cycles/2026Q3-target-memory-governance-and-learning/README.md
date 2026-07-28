# RC-2026Q3-target-memory-governance-and-learning

> Non-execution-source research cycle. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
cycle_id: RC-2026Q3-target-memory-governance-and-learning
storage_task: MNEMOSYNE-165
storage_PR: 216
storage_merge_commit: a66d92c572f178de52e3b3b238324decf279b7fb
post_merge_storage_repair_task: MNEMOSYNE-166
status: four_topic_reports_received_maintainer_reviewed_stored_and_exact_archive_complete_on_this_revision
research_execution_surface_reported_by_user: Pro_Deep_Research
exact_served_backend: unknown_or_not_attestable
execution_source_modified: false
target_project_action: false
automatic_policy_or_schema_adoption: false
```

## Purpose

This cycle preserves and evaluates four isolated research topics prepared after completion of `PRO-SLICE-01`:

1. whether target-project business conversations should load full, trimmed, or no additional Mnemosyne guidance after project guidance;
2. what learner-state, mastery-evidence, problem-solving and cognitive-coaching capabilities are currently defensible;
3. how multiple business Agents can reuse learner, user, environment and domain memory without creating an uncontrolled global profile or second execution source;
4. how an early target-Agent memory system can later evolve through versioned, reviewable and reversible migrations.

The reports are research evidence and candidate-design inputs. They do not close an open question, modify the execution source, approve a schema, authorize target-project work, or authorize automated sharing, inference, coaching or migration.

## Canonical files

### Exact prompt and report archive

The four exact prompt originals and four accepted report originals are stored byte-for-byte in a deterministic multipart archive:

- `exact-archive/README.md`
- `exact-archive/manifest.json`
- `exact-archive/parts/part-001-of-008.txt`
- `exact-archive/parts/part-002-of-008.txt`
- `exact-archive/parts/part-003-of-008.txt`
- `exact-archive/parts/part-004-of-008.txt`
- `exact-archive/parts/part-005-of-008.txt`
- `exact-archive/parts/part-006-of-008.txt`
- `exact-archive/parts/part-007-of-008.txt`
- `exact-archive/parts/part-008-of-008.txt`

The archive decodes to `tar.bz2`; member paths, byte counts, SHA-256 values and final-LF states are fixed in the manifest. The multipart representation avoids silently normalizing the original exported Markdown while keeping exact artifacts reconstructable from repository content.

PR #216 accidentally omitted parts 7 and 8 even though the manifest declared eight parts. MNEMOSYNE-166 independently regenerated the deterministic archive, matched all manifest-level tar, compressed-archive and Base64 identities, and restored the two missing parts. The repair record is:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`

### Review and synthesis

The canonical derived records are stored under the repository-wide review package, not duplicated under this raw cycle:

- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/03-decision-preparation.md`
- `notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/04-post-merge-storage-integrity-repair.md`
- `current/pro-deep-research-four-topic-batch-status.md`

The source tables inside exported reports vary in portability. Conversation-local citation tokens remain non-portable outside the originating Deep Research conversations. Stable-source mappings and interpretation limits are recorded in the maintainer reviews; no nonexistent cycle-local `source-manifest.md` is implied.

## Report disposition

```yaml
PRO_DR_HO_GUIDANCE_001:
  disposition: ACCEPT_WITH_CORRECTIONS
  policy_closed: false
PRO_DR_LEARNER_COGNITIVE_COACHING_001:
  disposition: ACCEPT_WITH_CORRECTIONS
  product_or_profile_approved: false
PRO_DR_CROSS_AGENT_SHARED_MEMORY_001:
  disposition: ACCEPT_WITH_CORRECTIONS
  automatic_sharing_approved: false
PRO_DR_TARGET_MEMORY_MIGRATION_001:
  disposition: ACCEPT_WITH_CORRECTIONS
  automatic_migration_or_universal_event_sourcing_approved: false
```

## Selected bounded follow-up

The user selected the maintainer-recommended next route after storage:

```yaml
selected_route: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT
selected_by: current_conversation_user_instruction_2026-07-28
current_output: notes/first-target-minimum-upgrade-contract-v0.1.md
current_role: candidate_for_user_review
execution_source_update: false
target_project_selected: false
implementation_authorized: false
```

This selection authorizes preparation of a bounded candidate only. It does not automatically modify the target-project template pack or start a target-project design/build.

## Safe next gate

```yaml
safe_next_gate:
  - review_the_first_target_minimum_upgrade_contract_candidate
  - record_explicit_user_disposition_before_any_template_or_target_project_change
  - preserve_other_conversation_owned_routes
```
