# Artifact Delivery and Direct Generation Guard

> User-approved Mnemosyne behavior guard for artifact delivery. This file is not a standalone execution source; `current/human-approved-spec.md` remains the only execution source. It operationalizes §12 and §13 together with the user's explicit repair decisions for Issues #170 and #171 and the later inline-operator-flow correction.

```yaml
guard_id: MNEMOSYNE-ARTIFACT-DELIVERY-001
created_by_task: MNEMOSYNE-127
amended_by_tasks:
  - MNEMOSYNE-155
  - MNEMOSYNE-185
  - MNEMOSYNE-200
  - MNEMOSYNE-203
status: active_after_MNEMOSYNE_203_merge
applies_to:
  - Mnemosyne_related_ChatGPT_conversations
  - Codex_tasks
  - future_Agent_tasks
execution_source: current/human-approved-spec.md
user_decision_provenance:
  - current_maintenance_conversation_approval_of_MNEMOSYNE_124
  - current_maintenance_conversation_instruction_to_redo_all_post_PR_173_work
  - current_maintenance_conversation_2026_07_25_complete_response_file_requirement
  - current_maintenance_conversation_2026_07_31_inline_operator_flow_requirement
  - current_maintenance_conversation_after_MNEMOSYNE_199_V0_repair_selection
  - MNE_FIRST_THREE_SYSTEMS_OWNER_REVIEW_OR_01_ACAP_027_amendment
amendment_source:
  - notes/proposed-active-guidance-amendments-from-or01-v0.1.md
  - notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
tracked_issues:
  - 170
  - 171
```

## 1. Purpose

Prevent five recurring workflow failures:

1. long, structured transfer content is pasted into chat and loses Markdown/YAML/code-block integrity or degrades browser performance;
2. after such transfer content, a short user correction such as “排版不对” is mistaken for an aesthetic editing request instead of a likely transfer-structure failure;
3. a user-requested low-risk downloadable artifact is promised for a later response instead of being created immediately;
4. a task requires the operator to return another conversation or Work task's complete final response, but the taskbook requests only named result artifacts, forcing the operator to send an extra message solely to obtain a downloadable complete-response copy;
5. a cross-conversation task, Deep Research task, Fable task, Codex task, or new-chat work package is stored correctly in repository files, but the user is forced to browse the repository merely to discover the actual operating procedure.

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

For Deep Research, the complete canonical report and a supported operator export are governed more specifically by `current/deep-research-report-delivery-correction-guard.md`; a standard report export is not a separate second research output or an arbitrary model-generated complete-response file.

### Low-risk downloadable artifact

A file whose content can be determined from the current authorized inputs and whose creation in the chat sandbox or equivalent local artifact surface does not itself change an external system.

Creating a local downloadable file is distinct from committing, uploading, emailing, forwarding, or otherwise writing that file to an external system.

### Operator flow

The complete, user-executable procedure for launching, conducting, stopping, and returning a task on another conversation or product surface.

An operator flow includes, when applicable:

- exact execution surface, visible model/mode/effort, and whether Research or another feature starts enabled or disabled;
- clean-chat, Project, memory, connector, file, and contamination prerequisites;
- exact repository, branch/ref, files, folders, downloadable artifacts, or paths to provide;
- preflight checks and pass/fail criteria;
- the copyable launch instruction or the direct downloadable task artifact that contains it;
- required return artifacts and return destination;
- stop conditions, fallback route, and prohibited actions;
- whether multiple tasks require separate conversations or Projects.

## 3. File-first delivery rule

A downloadable file is the primary delivery format when any of the following is true:

- the user explicitly asks for a downloadable file;
- the artifact is intended for cross-conversation, Codex, or external-tool transfer and is not trivially short;
- Markdown, YAML, code-block, ordering, or multi-section structure must be preserved;
- the full artifact would create a large chat body or a large fenced code block;
- the artifact is meant for backup, archival, or later machine/operator reuse.

When file-first delivery applies, the user-facing response should contain the smallest sufficient visible material while still remaining directly operable:

- purpose and scope;
- the download link or exact transfer pointer;
- the complete current operator flow required to use the artifact;
- every required user action, placed in the operation section required by §12;
- material limitations, stop conditions, or warnings.

Do not duplicate the complete long artifact in the chat body unless the user explicitly requests inline duplication or a higher-priority exception requires it. The long task body may remain file-first; the operator flow may not be reduced to an unexplained repository pointer.

## 3A. Complete-response transfer-file rule

For **non-Deep-Research** tasks, when a Mnemosyne task prompt, taskbook, handoff, review package, or execution instruction requires the operator to return or preserve the executor's **complete final response**, the task designer must explicitly require a separate downloadable complete-response transfer file.

Deep Research is excluded from this general rule and follows `current/deep-research-report-delivery-correction-guard.md`: it has one complete canonical report, and cross-conversation transfer should use a supported operator export of that report rather than an assumed second model-generated complete-response file.

For in-scope non-Deep-Research tasks, the taskbook must specify:

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
7. For Deep Research, do not require a separate arbitrary model-generated `complete-response.md` file. Require the complete canonical report in the product report/final-answer surface and, when transfer is needed, instruct the operator to export that same report in a supported format with an archival filename. A custom additional file is optional only when the current surface explicitly supports and verifies its creation; it may not replace the canonical report or be presented as a second research conclusion.
8. Creating the local complete-response file does not authorize repository write, upload, email, forwarding, or another connected-service action.

## 3B. Same-response operator-flow mirroring rule

When the Agent designs, publishes, recommends, or asks the user to run any task in another conversation or external surface, the same user-visible response must contain a directly usable operator flow. This applies to:

- Pro or Deep Research tasks;
- Fable or other independent frontier-review tasks;
- new ChatGPT conversation startup prompts and handoffs;
- Codex tasks;
- cross-model validation, replay, review, or adjudication tasks;
- any equivalent future external-Agent work package.

Rules:

1. Repository files, `OPERATOR.md`, taskbooks, manifests, and downloadable prompt files remain desirable canonical artifacts, but they are supplements—not substitutes—for the operating procedure in the design/launch response.
2. The user must not be required to browse a repository merely to learn which surface to open, which model/mode to select, which files to attach, what message to send, where to return the result, or when to stop.
3. A statement such as “see `OPERATOR.md`”, “read the task in the repository”, or “follow the files under this path” is insufficient by itself. The response must mirror all material steps and state the exact path or download link only as a reference or backup.
4. For a long research or task body, the response may provide a verified downloadable Markdown file instead of duplicating the body inline. The response must still include the complete operator flow and a concise topic/scope description.
5. When the task requires a connector or repository preflight, include the exact copyable preflight message inline, unless it is too large; in that case provide a verified downloadable operator package and inline the ordered actions, expected receipt, and failure rule.
6. When multiple independent tasks are delivered together, provide a separate numbered operator flow for each and state whether they require separate chats, Projects, files, reports, or contamination firewalls.
7. When execution is not yet authorized or depends on a PR merge, say so at the beginning of the flow. Distinguish “review/merge now” from “run later” and do not make the user infer activation state from repository metadata.
8. If an artifact exists only on an unmerged branch, state that it is not yet the active repository version. When current authorized inputs permit, provide a local downloadable copy so the user is not forced to navigate an unmerged branch.
9. The operator flow in the response and the repository/download artifact must agree. A material discrepancy blocks execution until corrected.
10. The response must preserve all required stop conditions and prohibited actions; brevity may not remove safety, privacy, authority, independence, or integrity gates.

## 3C. Context-sensitive transfer-format repair shortcut

When all of the following are true:

- the immediately preceding Agent response contained content intended for copying or transfer, especially Markdown, YAML, code blocks, task prompts, or a long structured package;
- the user responds with a short phrase equivalent to `排版不对`, `内容排版不对`, `格式坏了`, or `复制过去格式不对`;
- no stronger context indicates a different request;

interpret the leading hypothesis as **transfer-structure damage**, not ordinary aesthetic editing.

Required response:

1. Identify the likely affected artifact or content from the immediate context.
2. Preserve its substantive semantics, section order, identifiers, instructions and code/data structure; do not silently redesign it while repairing presentation.
3. Repair it using a verified downloadable file when the file-first rule applies; otherwise provide one complete, correctly fenced block whose boundaries are unambiguous.
4. Avoid repeating the entire design explanation unless it is needed to resolve an actual ambiguity.
5. State briefly which structural failure was repaired, such as lost fencing, broken indentation, list nesting, line wrapping or YAML/code-block boundary damage.
6. Ask at most one focused clarification when several materially different prior transfer artifacts could reasonably be meant.
7. Do not claim that a repaired file exists until creation and location are verified.
8. If the supplied content may already have lost or changed substantive text, disclose that limitation and request the intact source rather than pretending a formatting repair reconstructs missing semantics.

This is a context-sensitive shortcut, not a global keyword command. If the prior message did not contain transfer content, interpret the user's ordinary formatting request from the actual context.

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
- when the non-Deep-Research complete-response transfer-file rule applies, the required complete-response file was actually created and is distinguishable from the named substantive artifacts;
- when Deep Research transfer is required, the response requests a supported export of the single canonical report rather than claiming an unverified second file exists;
- when the same-response operator-flow rule applies, the response actually contains the complete operating procedure and does not rely only on a repository pointer;
- when a context-sensitive format repair was requested, the repaired artifact preserves the intended semantics and structural boundaries within the verified review scope.

Never invent a sandbox path, repository path, attachment, successful file creation, or successful operator-package delivery.

## 6. Tool-unavailable or failed-generation handling

If no suitable file-generation tool is available, or generation fails:

- state the limitation in the same response;
- do not claim that the file exists;
- do not defer with an unsupported promise of background work;
- provide the smallest safe fallback that preserves structure, or identify one necessary user action;
- avoid repeating a large structured body inline when that would reproduce the original failure;
- still provide the operator flow inline when it can be stated accurately without the failed artifact.

## 7. Inline-output cases

Direct chat output remains appropriate when:

- the content is a short explanation, checklist, summary, or one-step instruction;
- it is not intended for transfer or archival;
- structural preservation is not material;
- the user explicitly asks for inline text and doing so is safe.

File-first is a delivery control, not a requirement to create files for every answer. The operator-flow mirroring rule is also not a requirement to paste a long task body; it requires the user-facing operating procedure to remain visible and executable.

## 8. Deep Research exception

The existing §13 Deep Research exception remains unchanged and is operationalized by `current/deep-research-report-delivery-correction-guard.md`:

- a Deep Research final report must include the full canonical report body in the final report/answer;
- a supported Markdown/Word/PDF export may be provided or requested as an auxiliary representation of the same report when transfer or archival is needed;
- no arbitrary second model-generated complete-response file is required;
- this exception applies to the final Deep Research report, not to a Deep Research prompt, task brief, handoff package, or other transfer artifact, which remains subject to the file-first and operator-flow mirroring rules.

## 9. Authority and safety boundaries

This guard does not:

- make any generated artifact an execution source;
- authorize GitHub/repository writes, emails, uploads, forwarding, quota use, research execution, model switching, or other external actions;
- bypass repository-visibility, privacy, sensitivity, credential, independence, or connector-integrity checks;
- change Meta-Agent authority, no-write policy, or `HO-GUIDANCE-001`;
- authorize background work or future delivery promises;
- close Issue #170 or #171 without behavioral verification;
- make an unmerged task artifact active merely because its operator flow was mirrored in chat;
- permit a format-repair shortcut to alter substantive requirements or restore missing source text without evidence.

## 10. Supersession and historical records

The following post-PR-173 proposal files were produced during a user-reported suspect-reasoning period and are superseded by this reviewed guard after MNEMOSYNE-127 merges:

- `notes/MNEMOSYNE-124-artifact-delivery-repair-plan.md`;
- `current/proposed-section-13-artifact-delivery-operationalization.md`;
- `current/proposed-mnemosyne-125-execution-source-amendment.md`.

Their Git history and merged PRs remain historical evidence. They are not current behavior guidance and must not be used as the active implementation.
