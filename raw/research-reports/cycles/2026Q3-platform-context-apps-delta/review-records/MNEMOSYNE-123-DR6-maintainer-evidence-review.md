# MNEMOSYNE-123 — DR6 Maintainer Evidence Review

```yaml
reviewed_report_id: RPT-2026Q3-PLATFORM-DELTA-0001
cycle_id: RC-2026Q3-platform-context-apps-delta
reviewer: GPT_maintenance_conversation
review_type: substantive_research_ingestion_and_repository_mapping_review
verdict: ACCEPT_WITH_CORRECTIONS
evidence_role: supplemental_current_research_evidence
execution_source_modified: false
```

## 1. Review conclusion

DR6 is valuable and sufficiently source-rich to enter the current research evidence layer. Its central platform claims are consistent with independently sampled official OpenAI documentation current on 2026-07-15.

The report is not accepted verbatim as a repository-state authority. It is accepted with corrections, confidence classes and portability limitations.

## 2. Independently rechecked load-bearing facts

The maintainer review sampled current official documentation and confirmed:

- new Projects can choose default or project-only memory;
- existing Projects remain default and cannot be converted in place;
- project-only chats can use same-Project conversations but not outside-Project conversations;
- non-Enterprise default-memory Projects may reference outside-Project conversations;
- connected apps are selectable in Project chats;
- GitHub repository access and sync selection are separate;
- Deep Research uses connected-app read actions only;
- synced app data can interact with Memory;
- disconnecting an app does not erase existing conversations that used its data;
- Plugin Directory and underlying-app controls are separate;
- Chat, Work and Codex have distinct current product positioning.

Portable source URLs are recorded in `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/source-manifest.md`.

## 3. Repository mapping correction

DR6 incorrectly maps Issue #171 to the `HO-GUIDANCE-001` target-business-conversation guidance question.

Correct mapping:

```yaml
issue_170: long_artifact_file_first_delivery_failure
issue_171: low_risk_requested_artifact_not_generated_immediately
HO_GUIDANCE_001: target_project_business_conversation_additional_Mnemosyne_guidance_scope
```

This correction is applied only in summaries and derived views. The original report remains unchanged for provenance.

## 4. Research-run limitations

```yaml
connected_apps_used_by_report: none_in_this_chat_environment
repository_paths_explicitly_listed_as_read:
  - README.md
  - Issue_170
  - Issue_171
citation_portability: limited_opaque_Deep_Research_turn_markers
live_logged_in_UI_validation: not_performed
enterprise_audit_schema: not_available_in_public_detail
```

Consequences:

- external official-platform findings can be used as current evidence;
- exact repository path/status mappings require this maintainer review;
- citation tokens in the original are not treated as durable GitHub links;
- cross-platform comparisons remain supplemental;
- no execution-source update is implied.

## 5. Finding disposition

### Accepted as current platform evidence

- Project memory and cleanroom boundaries;
- app/plugin/auth/sync/approval/task-authority separation;
- GitHub auth versus sync distinction;
- Deep Research read-only connected-app behavior;
- synced-app Memory persistence risk;
- surface-specific availability and context differences;
- provenance should record operator-observed UI facts and environment;
- connector/search results are not completeness proofs.

### Accepted as candidate guidance only

- new Project-only cleanroom default;
- layered no-write evidence taxonomy;
- surface selection playbooks;
- trimmed Mnemosyne operator appendix for target-project business conversations;
- file-first and immediate low-risk artifact-generation repair package.

### Not promoted

- execution-source changes;
- automatic issue closure;
- automatic resolution of `HO-GUIDANCE-001`;
- universal guarantee about GitHub branch/ref coverage;
- universal guarantee that a named surface is read-only or writable;
- cross-platform feature claims without future direct source re-check.

## 6. Relationship to existing rules

- §13 already supports file-first long-transfer delivery.
- §15 keeps handoff and guidance loading separate.
- §17 requires dependency-aware staged research/prompt work.
- §18 separates platform permission from current task authority.
- §19 requires mechanical proof or explicit run-scoped exception.

DR6 mainly supports clearer operationalization, provenance and enforcement rather than wholesale replacement of these principles.

## 7. Recommended next task

Recommended next task after this ingestion PR is merged:

```yaml
task_candidate: MNEMOSYNE-124
name: artifact_delivery_and_direct_low_risk_generation_repair
scope:
  - resolve_Issue_170
  - resolve_Issue_171
  - strengthen_file_first_trigger_conditions
  - require_same_response_generation_when_no_extra_authorization_is_needed
  - add_a_small_deterministic_response_check
  - keep_Deep_Research_full_report_body_exception
execution_source_update: requires_explicit_current_user_approval
```

The provenance/no-write taxonomy and surface playbooks should follow in later staged tasks so that the immediate user-facing workflow defect is repaired first.
