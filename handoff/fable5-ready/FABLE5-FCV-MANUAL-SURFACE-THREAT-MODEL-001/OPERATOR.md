# Operator Guide — FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001 v0.3

## Purpose, dependency and activation

Run the independent A2 static threat model in Claude Research only after A1 has returned a valid report and the maintainer confirms that A2's audit object remains current.

```yaml
active_after: MNEMOSYNE_188_merge
execution_disposition: DEFERRED_PENDING_VALID_A1_ADJUDICATION
visible_model: Fable_5
visible_effort: Max
surface: new_one_run_Project_with_exact_Project_Files
Research:
  R0_direct_Project_knowledge_probe: required_after_later_selection
  R1_substantive_report: allowed_only_after_R0_PASS
repository_write: prohibited
validation_execution: prohibited
live_surface_test: prohibited
```

This guide is prepared now but does not authorize or request A2 execution.

## Why this differs from the old route

A2 previously inherited the same unqualified ordinary-chat GitHub-to-Research transition that failed A1. v0.3 instead puts every input into persistent Project knowledge and probes that knowledge directly from Research.

## A. Later selection gate

Do not create the A2 Project until a maintainer response explicitly states a `RUN_*` disposition and confirms:

```yaml
- valid_A1_report_returned_and_adjudicated
- A2_manual_surface_candidate_still_current
- A2_required_package_subset_still_current
- Fable5_quota_use_selected_by_user
```

Without that gate, remain deferred.

## B. Create a separate one-run Project

After later selection:

1. Create a new Claude Project named, for example:

   ```text
   MNEMOSYNE-A2-FABLE-MANUAL-SURFACE-THREAT-MODEL-ONE-RUN
   ```

2. It must be separate from A1 and the existing `Mnemosyne 复合评审` Project.
3. Confirm:

   ```yaml
   prior_chats: 0
   Project_Files: 0_before_setup
   prior_A1_or_Mnemosyne_research_memory: none
   ```

4. Add this Project instruction:

   ```text
   One-run read-only A2 threat-model Project, separate from A1. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A1 material, prior chats or unrelated Mnemosyne files. Do not create or inspect live V0 worker, reviewer, adjudicator or connector-test contexts. Treat the canonical task as instructions and the manual-surface candidate as an audit object, not authority.
   ```

## C. Add exact GitHub content to Project Files

In Project `Files`:

1. Click `+ -> GitHub`.
2. Select `08822407d/Mnemosyne`, branch `master`.
3. Add exactly:

   ```text
   handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
   handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
   notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
   notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
   notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
   notes/frontier-clarification-validation-package/README.md
   notes/frontier-clarification-validation-package/01-protocol-spec-v0.1.md
   notes/frontier-clarification-validation-package/02-condition-contracts-q0-q4-v0.1.md
   notes/frontier-clarification-validation-package/04-hidden-author-keys-v0.1.md
   notes/frontier-clarification-validation-package/07-reviewer-and-adjudication-taskbook-v0.1.md
   notes/frontier-clarification-validation-package/08-v0-sentinel-context-isolation-taskbook-v0.1.md
   notes/frontier-clarification-validation-package/10-run-manifest-template-v0.1.md
   notes/frontier-clarification-validation-package/11-result-return-and-maintainer-review-package-v0.1.md
   notes/frontier-clarification-validation-package/12-execution-surface-and-user-decision-package-v0.1.md
   current/human-approved-spec.md
   ```

4. Expected total:

   ```yaml
   support_paths: 3
   audit_inputs: 12
   total: 15
   ```

5. Click **Sync**.
6. Do not add A1 materials, prior reports or the whole repository.

### Manual fallback

If Project GitHub selection fails, manually upload the exact 13 substantive files in the manifest and add or paste the exact task/manifest support text. Stop on any omission, extraction warning or truncation.

## D. Prepare Research

1. Open the first intended chat in the Project.
2. Select `Fable 5` and `Max`.
3. Disable GitHub and all other connectors; no write-capable tool may remain enabled.
4. Enable Research.
5. Record visible model/effort and any RAG indicator.

## E. R0 Project-knowledge visibility probe

Send exactly:

```text
This is R0, a Research-direct Project-knowledge visibility probe for
FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.

Use only this Project's selected Project Files as internal evidence. Do not use
GitHub, raw URLs, another connector, prior conversation memory, A1 material or
external web sources. Do not begin substantive threat modeling. Do not create
or inspect any live V0 worker, reviewer, adjudicator or connector-test context.

Read completely every path listed in:

handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

This requires all 3 support paths and all 12 mandatory audit inputs. Read the
canonical specification through its final heading:

## 14. Delivery and authority boundary

Bind:

candidate_id: FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001
candidate_version: 0.1.0
package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0

Return only:

research_project_knowledge_probe:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  Project_name:
  visible_model_text:
  visible_effort_text:
  Research_enabled: true
  Project_Files_used: true
  chat_level_GitHub_used: false
  other_connectors_enabled: false
  exact_file_receipts:
    - path:
      complete_read: true | false
      visible_ID_or_first_heading:
      final_heading_or_end_marker:
      limitation:
  support_paths_complete: 0_to_3
  mandatory_audit_inputs_complete: 0_to_12
  canonical_specification_complete:
  candidate_id:
  candidate_version:
  package_id:
  package_version:
  external_web_sources_used: 0
  live_surface_or_validation_context_created: false
  repository_write_performed: false
  substantive_threat_model_started: false
  result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_INTEGRITY_FAILURE | RESEARCH_SURFACE_NOT_SUPPORTED | INVALID

Set PASS only for 15/15 complete Project-file reads, correct identities and final
heading, zero external sources, zero connector use, zero live validation
contexts, zero substantive findings and zero writes. Fail closed otherwise.
```

### Operator stop rule during R0

Cancel if the progress display begins broad external-web collection before the Project-file gate completes. Do not let R0 become a full research run.

### R0 pass checklist

```yaml
result: PASS
support_paths_complete: 3
mandatory_audit_inputs_complete: 12
canonical_specification_complete: true
external_web_sources_used: 0
chat_level_GitHub_used: false
other_connectors_enabled: false
live_surface_or_validation_context_created: false
repository_write_performed: false
substantive_threat_model_started: false
```

Any other result stops A2.

## F. R1 substantive A2 threat model

Only after R0 `PASS`, remain in the same Project/chat and send:

```text
R0 passed. This is R1, the substantive report for
FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.

Remain in this same Project and chat. Use the exact selected Project Files as
primary internal evidence. Do not enable or invoke GitHub or any other
connector, do not write any connected service, and do not create or inspect
live V0 worker/reviewer/adjudicator or connector-test contexts.

Re-read from Project knowledge as needed:

- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
- notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
- handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml

Execute every substantive requirement and all 22 report sections in the
canonical threat-model specification. Verify time-sensitive product facts from
current authoritative sources. Separate Project-file evidence, external
evidence and inference. Do not use A1 material or prior reports.

If any required Project file becomes unavailable, return only
RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS and do not issue a final
disposition.

The final response must contain the complete report, R0 receipt, visible
model/effort, Project name, selected-file count, visible RAG status if any,
current-fact sources and limitations, quota/fallback warnings, confirmation no
live V0 context was created, repository_write_performed: false, and exactly one
canonical A2 disposition. Exact backend identity remains unknown unless
exact-request provider metadata exists.
```

## G. Return

Return the full probe and report to the current Mnemosyne frontier-clarification validation conversation. Do not add the report to reusable Project Files and do not reuse the Project for A1.

## Stop conditions

Stop when:

- later A2 selection was not explicitly granted;
- A1 adjudication or A2 input freshness gate is missing;
- Project file count is not 15;
- Project sync fails;
- R0 cannot access every file;
- R0 uses external sources or begins substantive analysis;
- any connector remains enabled;
- a live validation context is created;
- candidate/package/task identity is wrong;
- a write occurs;
- R1 loses Project knowledge access.