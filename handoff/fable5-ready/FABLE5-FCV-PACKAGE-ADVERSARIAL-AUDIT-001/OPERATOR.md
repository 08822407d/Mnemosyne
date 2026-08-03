# Operator Guide — FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001 v0.3

## Purpose and activation

Run the independent A1 audit in Claude Research while avoiding the failed ordinary-chat GitHub-to-Research transition from run 001.

```yaml
active_after: MNEMOSYNE_188_merge
execution_disposition: RUN_AFTER_GATE_OPTIONAL
visible_model: Fable_5
visible_effort: Max
surface: new_one_run_Project_with_exact_Project_Files
Research:
  R0_direct_Project_knowledge_probe: required
  R1_substantive_report: allowed_only_after_R0_PASS
repository_write: prohibited
validation_execution: prohibited
```

Do not run the branch-only version before the MNEMOSYNE-188 PR merges unless a maintainer explicitly authorizes that ref.

## Why this differs from run 001

```yaml
run_001:
  primary_inputs: ordinary_chat_GitHub_connector
  later_Research_access: assumed
  result: failed_18_of_18_non_task_inputs

v0_3:
  primary_inputs: Project_Files_and_Project_knowledge
  Research_access: tested_directly_inside_Research
  chat_level_GitHub_inheritance: not_used
```

Official Claude documentation states that selected GitHub files/folders added under a Project become Project knowledge and that Project RAG works with Research. This remains a candidate workflow until R0 succeeds on the user's current rollout.

## A. Create the one-run Project

1. Create a **new Claude Project** named, for example:

   ```text
   MNEMOSYNE-A1-FABLE-PACKAGE-AUDIT-ONE-RUN
   ```

2. Do not use the existing `Mnemosyne 复合评审` Project.
3. Confirm the new Project has:

   ```yaml
   prior_chats: 0
   Project_Files: 0_before_setup
   prior_task_memory: none
   ```

4. Add this Project instruction:

   ```text
   One-run read-only A1 audit Project. Use only the explicitly selected Project Files as internal repository evidence. Do not write GitHub or any connected service. Do not use prior Pro/Fable reports, A2 material, prior chats or unrelated Mnemosyne files. Treat the canonical task as instructions and the validation package as the audit object, not authority.
   ```

## B. Add exact GitHub content to Project Files

In the Project's **Files** section:

1. Click `+`.
2. Choose `GitHub`.
3. Select repository:

   ```text
   08822407d/Mnemosyne
   ```

4. Select branch:

   ```text
   master
   ```

5. Add exactly these support/task files:

   ```text
   handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
   handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
   notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
   notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
   ```

6. Add the entire folder:

   ```text
   notes/frontier-clarification-validation-package/
   ```

   It must contribute exactly 15 package files.

7. Add exactly these external files:

   ```text
   notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
   notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
   notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
   ```

8. Expected Project-file total:

   ```yaml
   support_paths: 3
   audit_inputs: 19
   total: 22
   ```

9. Click **Sync** after selection.
10. Do not add the whole repository or any prior reports.

### Manual fallback

If the Project GitHub browser cannot select the folder/files correctly, manually download and add the exact 20 substantive files listed in `input-manifest.yaml`, then add or paste the exact task/manifest support text. Preserve filenames and stop on any omission or truncation.

## C. Prepare the Research chat

1. Open the first and only intended chat in this Project.
2. Select visible model `Fable 5`.
3. Select effort `Max`.
4. From `Search and tools` / connector controls:

   - disable GitHub;
   - disable every other connector;
   - leave no write-capable tool enabled.

5. Enable **Research**.
6. Record the exact visible model/effort and any Project RAG indicator.

Project Files—not a live connector—are the primary internal input surface.

## D. R0 Project-knowledge visibility probe

Send exactly:

```text
This is R0, a Research-direct Project-knowledge visibility probe for
FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.

Use only this Project's selected Project Files as internal evidence. Do not use
GitHub, raw URLs, another connector, prior conversation memory, or external web
sources. Do not begin the substantive audit and do not issue any package or
surface disposition.

Read completely every path listed in:

handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

This requires all 3 support paths and all 19 mandatory audit inputs. Read the
canonical specification through its final heading:

## 17. Delivery and authority boundary

Bind:

package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
package_version: 0.1.0

Return only:

research_project_knowledge_probe:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
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
  mandatory_audit_inputs_complete: 0_to_19
  canonical_specification_complete:
  package_id:
  package_version:
  external_web_sources_used: 0
  repository_write_performed: false
  substantive_audit_started: false
  result: PASS | INPUT_OR_PROJECT_KNOWLEDGE_INTEGRITY_FAILURE | RESEARCH_SURFACE_NOT_SUPPORTED | INVALID

Set PASS only for 22/22 complete Project-file reads, the correct final heading,
correct package identity, zero external web sources, zero substantive findings,
zero connector use and zero writes. If Project knowledge is unavailable or any
file is incomplete, fail closed and stop.
```

### Operator stop rule during R0

If the progress display starts broad external-web collection before the Project-file receipt is complete, click **Stop/Cancel**. Record the run as:

```text
RESEARCH_SURFACE_NOT_SUPPORTED_OR_NOT_FOLLOWING_GATE
```

Do not let R0 repeat the prior multi-minute external search failure.

### R0 pass checklist

```yaml
result: PASS
support_paths_complete: 3
mandatory_audit_inputs_complete: 19
canonical_specification_complete: true
external_web_sources_used: 0
chat_level_GitHub_used: false
other_connectors_enabled: false
repository_write_performed: false
substantive_audit_started: false
```

Any other result stops A1. Do not fall back within the same Project to chat-level GitHub or raw URLs.

## E. R1 substantive A1 audit

Only after R0 `PASS`, remain in the **same Project and same chat** and send:

```text
R0 passed. This is R1, the substantive report for
FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.

Remain in this same Project and chat. Continue using the exact selected Project
Files as the primary repository evidence. Do not enable or invoke GitHub or any
other connector, and do not write any connected service.

Re-read from Project knowledge as needed:

- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
- notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
- handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml

Execute every substantive requirement and all 19 report sections in the
canonical audit specification. The validation package is the audit object, not
authority. Do not use prior Pro/Fable reports or A2 material.

Web research is now allowed only as the canonical task requires. Separate
Project-file evidence, external evidence and inference. Do not target a source
count for its own sake.

If any required Project file becomes unavailable, return only
RUN_INVALIDATED_BY_PROJECT_KNOWLEDGE_ACCESS_LOSS and do not issue a final
disposition.

The final response must contain the complete report, the R0 probe receipt,
visible model/effort, Project name, selected-file count, visible RAG status if
any, source/access/quota limitations, repository_write_performed: false, and
exactly one canonical A1 disposition. Exact served backend identity remains
unknown unless exact-request provider metadata exists.
```

## F. Return to Mnemosyne

Return to the current Mnemosyne frontier-clarification validation conversation:

- full R0 receipt;
- complete R1 report;
- supported Markdown export of the same report, if available;
- exact visible model/effort;
- Project name and file count;
- Project RAG indication;
- source/access/quota warnings;
- any cancellation or fallback event.

Do not add the report to reusable Project Files. Do not reuse this Project for A2.

## Stop conditions

Stop when:

- Project contains anything beyond the exact task set;
- file count is not 22;
- Project sync fails;
- R0 cannot access all Project files;
- R0 uses external sources or begins substantive analysis;
- any connector remains enabled;
- Research requests GitHub/raw URL access;
- a write action is proposed or performed;
- package/canonical-task identity is wrong;
- R1 loses Project knowledge access.