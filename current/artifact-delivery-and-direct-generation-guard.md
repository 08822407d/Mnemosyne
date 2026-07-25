# Artifact Delivery and Direct Generation Guard

> User-approved Mnemosyne behavior guard for artifact delivery. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source. It operationalizes §12 and §13 together with the user's explicit repair decisions for Issues #170 and #171.

```yaml
guard_id: MNEMOSYNE-ARTIFACT-DELIVERY-001
created_by_task: MNEMOSYNE-127
amended_by_task: MNEMOSYNE-155
status: active_after_MNEMOSYNE_155_merge
applies_to:
  - Mnemosyne_related_ChatGPT_conversations
  - Codex_tasks
  - future_Agent_tasks
execution_source: current/human-approved-spec.md
user_decision_provenance:
  - current_maintenance_conversation_approval_of_MNEMOSYNE_124
  - current_maintenance_conversation_instruction_to_redo_all_post_PR_173_work
  - current_maintenance_conversation_2026_07_25_complete_response_file_requirement
tracked_issues:
  - 170
  - 171
```

## 1. Purpose

Prevent three recurring workflow failures:

1. long, structured transfer content is pasted into chat and loses Markdown/YAML/code-block integrity or degrades browser performance;
2. a user-requested low-risk downloadable artifact is promised for a later response instead of being created immediately;
3. a task requires the operator to return another conversation or Work task's complete final response, but the taskbook requests only named result artifacts, forcing the operator to send an extra message solely to obtain a downloadable complete-response copy.

## 2. Definitions

### Transfer artifact

An artifact intended to be copied, downloaded, preserved, backed up, or supplied to another ChatGPT conversation, Codex task, external AI/tool, or future operator.

Examples include:

- Codex task prompts;
- handoff packages;
- replay/startup prompts;
- review or verification packages;
- prompt packs;
- multi-part structured instructions;
- long Markdown/YAML/code artifacts whose structure must survive transfer.

### Complete-response transfer file

A downloadable file containing the task executor's complete final user-visible response for return to a maintainer conversation, archival, review, or evidence comparison.

It is distinct from named substantive artifacts such as a synthesis, ledger, matrix, report, or patch specification. The complete response may summarize, wrap, link to, or differ from those artifacts and therefore requires its own explicit identity and role when the task asks the operator to return it.

### Low-risk downloadable artifact

A file whose content can be determined from the current authorized inputs and whose creation in the chat sandbox or equivalent local artifact surface does not itself change an external system.

Creating a local downloadable file is distinct from committing, uploading, emailing, forwarding, or otherwise writing that file to an external system.

## 3. File-first delivery rule

A downloadable file is the primary delivery format when any of the following is true:

- the user explicitly asks for a downloadable file;
- the artifact is intended for cross-conversation, Codex, or external-tool transfer and is not trivially short;
- Markdown, YAML, code-block, ordering, or multi-section structure must be preserved;
- the full artifact would create a large chat body or a large fenced code block;
- the artifact is meant for backup, archival, or later machine/operator reuse.

When file-first delivery applies, the user-facing response should contain only the smallest sufficient visible material:

- purpose and scope;
- the download link;
- concise usage instructions;
- every required user action, placed in the operation section required by §12;
- material limitations or warnings.

Do not duplicate the complete long artifact in the chat body unless the user explicitly requests inline duplication or a higher-priority exception requires it.

## 3A. Complete-response transfer-file rule

When a Mnemosyne task prompt, taskbook, handoff, review package, or execution instruction requires the operator to return or preserve the executor's **complete final response**, the task designer must explicitly require a separate downloadable complete-response transfer file.

The taskbook must specify:

```yaml
complete_response_transfer_file:
  required: true
  suggested_filename: <TASK_ID>-complete-response.md
  content_scope: complete_final_user_visible_response
  create_in_same_final_response: true
  role: auxiliary_transfer_and_archival_copy
```

Rules:

1. The complete-response file must be generated automatically in the same final response as the named task artifacts. The operator must not need to send a second prompt solely to ask the executor to export its already-issued response.
2. The file must preserve the complete user-visible final response as faithfully as the surface permits, including headings, lists, tables, YAML/code blocks, status metadata, warnings, file links or transfer pointers, and final status lines.
3. The taskbook's required-output list and closeout checklist must name this file explicitly. A general request such as “return the complete response” is insufficient when the operator is expected to transfer it as a file.
4. Named substantive artifacts do not substitute for the complete-response file. If the complete response and a synthesis/report differ, preserve both and record their separate byte/hash identities and roles. If they are byte-identical, the task may disclose the identity relation, but the required complete-response filename must still be delivered unless the operator explicitly waives it.
5. Do not require a complete-response file when the maintainer needs only the named artifacts and does not require the full reply. This rule is conditional, not a requirement to export every answer.
6. If the surface cannot generate or preserve the file, the original final response must disclose the limitation and identify the single minimal operator action needed. It must not claim that the file exists.
7. For Deep Research, the canonical full report remains in the final report/answer under the §13 exception. When cross-conversation return of the full response is required, the taskbook should additionally require a downloadable complete-response copy as an auxiliary transfer artifact; it may not replace the inline canonical report.
8. Creating the local complete-response file does not authorize repository write, upload, email, forwarding, or another connected-service action.

## 4. Same-response generation rule

When the user explicitly requests a file artifact, generate it in the same response if:

- its content is sufficiently determined by current authorized inputs;
- no unresolved user decision is needed to determine the content;
- no sensitive-data handling decision is pending;
- creating the local downloadable file requires no new external side effect or external authorization;
- an available tool can create the requested file safely.

Do not respond only with “I will generate the file” or equivalent future-tense language when the artifact can be created now.

If the user also requests an external action—such as committing the file, uploading it, sending it, or writing it to another repository—separate the two operations:

1. create the safe local downloadable artifact now when possible;
2. apply the independent authorization gate to the external action.

An external-action gate does not by itself justify delaying safe local artifact creation.

## 5. Verification before claiming delivery

Before stating that a file was created or delivered, verify as far as the available artifact tool allows that:

- the file creation call succeeded;
- the expected filename and format are correct;
- the file exists at the returned location;
- the response contains a working artifact link or the exact available transfer pointer;
- the full long body was not unnecessarily duplicated in chat;
- when the complete-response transfer-file rule applies, the required complete-response file was actually created and is distinguishable from the named substantive artifacts.

Never invent a sandbox path, repository path, attachment, or successful file creation.

## 6. Tool-unavailable or failed-generation handling

If no suitable file-generation tool is available, or generation fails:

- state the limitation in the same response;
- do not claim that the file exists;
- do not defer with an unsupported promise of background work;
- provide the smallest safe fallback that preserves structure, or identify one necessary user action;
- avoid repeating a large structured body inline when that would reproduce the original failure.

## 7. Inline-output cases

Direct chat output remains appropriate when:

- the content is a short explanation, checklist, summary, or one-step instruction;
- it is not intended for transfer or archival;
- structural preservation is not material;
- the user explicitly asks for inline text and doing so is safe.

File-first is a delivery control, not a requirement to create files for every answer.

## 8. Deep Research exception

The existing §13 Deep Research exception remains unchanged:

- a Deep Research final report must include the full canonical report body in the final report/answer;
- a downloadable export may be provided only as an auxiliary copy;
- this exception applies to the final Deep Research report, not to a Deep Research prompt, task brief, handoff package, or other transfer artifact, which remains subject to the file-first rule.

## 9. Authority and safety boundaries

This guard does not:

- make any generated artifact an execution source;
- authorize GitHub/repository writes, emails, uploads, forwarding, or other external actions;
- bypass repository-visibility, privacy, sensitivity, or credential checks;
- change Meta-Agent authority, no-write policy, or `HO-GUIDANCE-001`;
- authorize background work or future delivery promises;
- close Issue #170 or #171 without behavioral verification.

## 10. Supersession and historical records

The following post-PR-173 proposal files were produced during a user-reported suspect-reasoning period and are superseded by this reviewed guard after MNEMOSYNE-127 merges:

- `notes/MNEMOSYNE-124-artifact-delivery-repair-plan.md`;
- `current/proposed-section-13-artifact-delivery-operationalization.md`;
- `current/proposed-mnemosyne-125-execution-source-amendment.md`.

Their Git history and merged PRs remain historical evidence. They are not current behavior guidance and must not be used as the active implementation.
