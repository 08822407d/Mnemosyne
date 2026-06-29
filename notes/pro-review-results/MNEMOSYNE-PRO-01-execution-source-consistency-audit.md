---
audit_id: MNEMOSYNE-PRO-01
audit_type: execution_source_consistency_audit
repository: 08822407d/Mnemosyne
tested_at: 2026-06-29 America/Los_Angeles
tool_or_interface: ChatGPT GitHub connector read-only review plus local Markdown artifact generation
visible_model_label: GPT-5.5 Pro
reasoning_effort_if_visible: not_visible
files_read:
  required:
    - README.md
    - current/human-approved-spec.md
    - current/active-context.md
    - current/todo.md
    - current/open-questions.md
    - handoff/handoff-current.md
    - handoff/startup-instructions.md
    - commands/load-mnemosyne-guidance.md
    - notes/target-project-workspace-boundary-and-layout-proposal.md
    - notes/first-target-project-dry-run-manifest-template.md
    - handoff/first-target-project-dry-run-onboarding-package.md
    - notes/first-target-project-dry-run-review-instruments.md
    - notes/handoff-package-strategy-v0.1.md
    - notes/handoff-replay-scorecard-v0.1.md
    - notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md
    - notes/codex-task-results/MNEMOSYNE-057-result.md
    - notes/codex-task-authoring-and-diff-verification-guidelines.md
  additional:
    - notes/first-target-project-dry-run-minimal-profile.md
    - notes/first-target-project-dry-run-checklist.md
    - notes/first-target-project-dry-run-result-template.md
    - notes/first-target-project-fresh-replay-protocol.md
    - repository search for target-projects/<target_project_id>
    - repository search for notes/target-project-dry-runs
    - repository search for target runtime truth source
    - repository search for no-target-write
missing_files: []
audit_verdict: PASS_WITH_WARNINGS
---

# MNEMOSYNE PRO-01：执行源一致性强审计

## 1. Executive summary

Verdict: **PASS_WITH_WARNINGS**.

MNEMOSYNE-057's target-project workspace principle is internally consistent with the current Mnemosyne execution-source model at the high-authority layer. `current/human-approved-spec.md` remains the sole Mnemosyne execution source, and the new `target-projects/<target_project_id>/` workspace principle explicitly states that the target workspace is neither Mnemosyne execution source nor automatically the target runtime truth source. The active-context, TODO, open-questions, handoff-current, manifest template, onboarding package, and MNEMOSYNE-057 result record are broadly synchronized: no target is selected, no target workspace is created, no target materials are ingested, no target repository is written, and no real target-project dry-run has started.

The design is not clean enough for an unqualified PASS because two first-dry-run support instruments still contain stale or superseded wording, and the manifest schema can be made more authority-explicit before a real dry-run. The most important stale issue is that `notes/first-target-project-dry-run-minimal-profile.md` still points the manifest path to `notes/target-project-dry-runs/<dry_run_id>/00-run-manifest.md`, while the post-057 manifest and onboarding package now route future run artifacts under `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/` after user approval. A second stale issue is that `notes/first-target-project-dry-run-result-template.md` still refers to the reviewed post-050 replay result, even though the current gate is post-MNEMOSYNE-053 reviewed replay PASS. These do not currently authorize unsafe work because they are non-execution-source instruments and are overridden by the spec, manifest, and onboarding package, but they should be repaired before any real target-project dry-run.

## 2. Critical findings

**Critical finding count: 0.**

No blocking execution-source inconsistency was found in the required-read files. The strongest rules are in the correct authority order:

- `current/human-approved-spec.md` declares itself the only Mnemosyne execution source and demotes raw, research, candidates, decision logs, active-context, handoff, and other support materials to non-execution-source roles.
- Section 16 of `current/human-approved-spec.md` adds the target-project workspace principle without allowing the workspace to become Mnemosyne execution source.
- The same section blocks automatic target runtime truth-source promotion unless a target-local manifest or owner rule explicitly and user-approvedly grants that role.
- The run manifest and onboarding package both require user approvals before workspace creation, target material ingestion, real dry-run execution, or target repository writes.

No missing required file blocked the audit.

## 3. Non-critical warnings

### W-01 — Stale dry-run manifest path in minimal profile

**Severity:** non-critical now; should be fixed before any real dry-run.

`notes/first-target-project-dry-run-minimal-profile.md` still says:

```yaml
manifest_path: notes/target-project-dry-runs/<dry_run_id>/00-run-manifest.md after user-approved run creation
```

That conflicts with the post-057 routing rule in the manifest template, which says future dry-run outputs should be target-scoped under `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/` after target workspace approval, and also explicitly says not to create either old or new run folders merely because the template exists. The onboarding package also shows the future output folder under `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/`.

This is not an execution-source violation, but it is a practical executor-risk because the minimal profile is in the onboarding read order. A future executor could follow the stale `notes/target-project-dry-runs/` path if it reads the minimal profile without reconciling it against the manifest template and spec.

**Evidence:** `notes/first-target-project-dry-run-minimal-profile.md:L20-L22`; `notes/first-target-project-dry-run-manifest-template.md:L87-L93`; `handoff/first-target-project-dry-run-onboarding-package.md:L103-L111`; `current/human-approved-spec.md:L191-L208`.

### W-02 — Stale post-050 replay reference in result template

**Severity:** non-critical now; should be fixed before any real dry-run result is produced.

`notes/first-target-project-dry-run-result-template.md` says a run must reference the fresh replay protocol and the reviewed post-050 replay result. Current state says the replay-quality portion of the gate is satisfied by the post-MNEMOSYNE-053 reviewed PASS, and the replay protocol has version `2026-06-23-post-MNEMOSYNE-053`.

This does not change current state because the result template is non-execution-source and there is no real dry-run. It can still mislead a future result author into citing the wrong replay gate.

**Evidence:** `notes/first-target-project-dry-run-result-template.md:L16-L18`; `notes/first-target-project-fresh-replay-protocol.md:L14-L18` and `L33-L35`; `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L11-L23`; `current/active-context.md:L39-L45`.

### W-03 — Manifest schema should make approval authority and status enums more explicit

**Severity:** non-critical now; recommended before real target material intake or workspace creation.

The manifest contains useful fields for workspace root, workspace status, workspace creation approval, workspace execution-source status, workspace runtime truth-source status, user-input storage policy, no-target-write confirmation, and user approvals. However, some fields would be safer with explicit enums and authority metadata:

- `workspace_creation_approved` has no visible enum or `approved_by` / `approved_at` fields.
- `no_target_write_confirmed` is a key safety gate but has no visible enum; a future executor should not treat a blank value as false, true, or inferred.
- `target_materials_uploaded_or_ingested` has no visible enum or distinction between `false`, `pending`, `approved_to_ingest`, and `ingested`.
- `workspace_is_target_runtime_truth_source: false | target_manifest_approved | unknown` mixes a boolean-like value with a status. A clearer field would record `target_runtime_truth_source_status`, `target_runtime_truth_source_authority_path`, `approved_by`, and `approved_at`.
- `user_approvals` does not separately list `target_workspace_root_approved`, `workspace_creation_approved`, `user_input_storage_policy_approved`, or `run_manifest_approved`; some are implied elsewhere, but explicit repetition in a safety manifest is acceptable.

The current rules are safe because they state that unsafe or ambiguous material stops the run and that workspace creation is unauthorized until user approvals are complete. The warning is about making the schema harder to misread.

**Evidence:** `notes/first-target-project-dry-run-manifest-template.md:L45-L76`; `notes/first-target-project-dry-run-manifest-template.md:L81-L93`; `handoff/first-target-project-dry-run-onboarding-package.md:L63-L72`; `current/todo.md:L13-L20`; `handoff/handoff-current.md:L81-L88`.

### W-04 — Broader privacy/redaction/access-control policy remains open

**Severity:** non-critical for current no-ingestion state; relevant before sensitive target materials.

MNEMOSYNE-057 safely addresses target-project originals at the high level: target originals and raw requirements may enter the repository only when safe for visibility and user-approved; otherwise only redacted references or external pointers should be stored. This is sufficient to prevent accidental intake in the current state. However, `OP-08` remains open/partially addressed as a broader privacy/redaction/access-control question. Before handling genuinely sensitive real target materials, the project should either keep originals external or complete a more formal target-material privacy policy.

**Evidence:** `current/human-approved-spec.md:L160-L172` and `L191-L208`; `current/open-questions.md:L24-L32` and `L40-L56`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L122-L140`; `handoff/first-target-project-dry-run-onboarding-package.md:L65-L71`.

### W-05 — Minor duplicated no-materials claim in handoff-current

**Severity:** low.

`handoff/handoff-current.md` contains both “No target-project materials have been uploaded or ingested” and “No target materials have been uploaded/ingested.” These are semantically consistent, but the duplication creates needless surface area in a high-signal handoff file.

**Evidence:** `handoff/handoff-current.md:L28-L32`.

## 4. File-by-file consistency review

### README.md

Consistent. The README describes Mnemosyne as a memory-system meta-agent work repository and emphasizes visibility/Git-history safety. This supports the current rule that target material must not be placed in the repository unless visibility and safety are checked.

**Evidence:** `README.md:L3-L9`.

### current/human-approved-spec.md

Consistent and authoritative. The file clearly declares itself the sole execution source. Section 16 is the key promoted MNEMOSYNE-057 change and is narrowly scoped: it allows target workspaces inside Mnemosyne, sets `target-projects/<target_project_id>/` as the standard root, denies Mnemosyne execution-source status to the target workspace, denies automatic target runtime truth-source status, limits user originals to safe/user-approved storage, prevents target-specific lessons from auto-promoting globally, and preserves the need for user approval before workspace creation, material ingestion, real dry-run, or target write.

**Evidence:** `current/human-approved-spec.md:L1-L5`; `current/human-approved-spec.md:L23-L35`; `current/human-approved-spec.md:L191-L208`.

### current/active-context.md

Consistent in the compact current view. It repeats the sole execution-source rule, records MNEMOSYNE-057 as promoted into the spec, and states the live blockers: user target selection, authority/source map, safe input/user originals storage, no-target-write, and approved run manifest. It also states no dry-run, no target selection, no target materials, and no target repository write.

The historical section is explicitly labelled as superseded and should not be used as current route. That label is adequate.

**Evidence:** `current/active-context.md:L13-L18`; `current/active-context.md:L35-L45`; `current/active-context.md:L53-L58`; `current/active-context.md:L86-L89`.

### current/todo.md

Consistent. The live TODO list matches the active context and handoff: the user must select target, approve workspace root or exception, confirm owner/authority, approve source map and storage policy, confirm no-target-write, and approve run manifest before any real dry-run.

**Evidence:** `current/todo.md:L5-L20`; `current/todo.md:L23-L29`; `current/todo.md:L47-L49`.

### current/open-questions.md

Mostly consistent. The top current section accurately marks MNEMOSYNE-056 workspace questions as answered or partially answered by MNEMOSYNE-057. It retains OP-08 as partially addressed, which is appropriate because the new target workspace rule does not fully solve broader privacy/redaction/access-control policy. Historical open questions are explicitly labelled historical.

**Evidence:** `current/open-questions.md:L5-L23`; `current/open-questions.md:L24-L38`; `current/open-questions.md:L40-L57`; `current/open-questions.md:L58-L60`.

### handoff/handoff-current.md

Consistent, with one low-severity duplication. The file states the current route, non-execution-source boundaries, key prohibitions, recent checkpoints, and next route. It has a duplicated no-materials claim, but no material contradiction.

**Evidence:** `handoff/handoff-current.md:L23-L32`; `handoff/handoff-current.md:L43-L60`; `handoff/handoff-current.md:L81-L88`.

### handoff/startup-instructions.md

Consistent. It states that startup instructions are not execution source, identifies the minimum startup set, says not to rely on old conversation context, and requires missing files to be reported rather than invented. It routes first target-project dry-run preparation through the onboarding package.

**Evidence:** `handoff/startup-instructions.md:L5-L17`; `handoff/startup-instructions.md:L19-L31`; `handoff/startup-instructions.md:L37-L43`.

### commands/load-mnemosyne-guidance.md

Consistent. The command is non-execution-source, loads the required files, requires `current/human-approved-spec.md` to be treated as the only execution source, and forbids edits/automation/auto-writeback beyond approved scope.

**Evidence:** `commands/load-mnemosyne-guidance.md:L5-L6`; `commands/load-mnemosyne-guidance.md:L21-L34`; `commands/load-mnemosyne-guidance.md:L36-L57`; `commands/load-mnemosyne-guidance.md:L59-L64`.

### notes/target-project-workspace-boundary-and-layout-proposal.md

Consistent as a non-execution-source reference. It now includes a post-MNEMOSYNE-057 status note stating that the high-level principle/default root were promoted, while detailed layout remains non-execution-source. Its three-layer boundary is useful: Mnemosyne global layer, target workspace layer inside Mnemosyne repo, and target runtime truth source/external repository.

**Evidence:** `notes/target-project-workspace-boundary-and-layout-proposal.md:L5-L15`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L26-L50`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L52-L68`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L155-L166`.

### notes/first-target-project-dry-run-manifest-template.md

Mostly consistent and materially adequate. It contains explicit fields for target execution source or owner rule, source item authority, input sensitivity, workspace root/status/creation approval, non-execution-source status, target runtime truth-source status, user-input storage policy, no-target-write, target-material ingestion status, expected outputs, unsupported assumptions, user approvals, and stop conditions. It also contains rules that a real dry-run requires `manifest_status: user_approved`, that unsafe/ambiguous material stops the run, that no-target-write must be confirmed, and that target workspace creation is not authorized merely by the template.

The warning is schema precision, not overall inadequacy. Add explicit enums and authority metadata for workspace creation, storage policy approval, no-target-write, material ingestion, and target runtime truth-source authority.

**Evidence:** `notes/first-target-project-dry-run-manifest-template.md:L13-L77`; `notes/first-target-project-dry-run-manifest-template.md:L79-L93`.

### handoff/first-target-project-dry-run-onboarding-package.md

Consistent. It has a strong authority map and explicitly states that target source materials may inform design only when safe, user-approved, and authority-mapped. It adds a target-project workspace boundary section with default root, storage scope, non-execution-source and non-runtime-truth boundaries, safe input rules, no workspace creation before approvals, and no target repository write authorization.

The onboarding package's read order includes the minimal profile and result template, so the stale warnings in those two files should be repaired even though the onboarding package itself is aligned.

**Evidence:** `handoff/first-target-project-dry-run-onboarding-package.md:L5-L12`; `handoff/first-target-project-dry-run-onboarding-package.md:L21-L31`; `handoff/first-target-project-dry-run-onboarding-package.md:L32-L46`; `handoff/first-target-project-dry-run-onboarding-package.md:L55-L72`; `handoff/first-target-project-dry-run-onboarding-package.md:L74-L90`; `handoff/first-target-project-dry-run-onboarding-package.md:L163-L165`.

### notes/first-target-project-dry-run-review-instruments.md

Consistent. It is non-execution-source, requires target execution-source identification, current state matching, owner decision propagation, stale information marking, file role justification, privacy/tool/automation verification, and handoff next-step clarity. It also warns that Mnemosyne execution source must not be treated as target runtime truth source and that target-specific issues should not be upgraded globally.

**Evidence:** `notes/first-target-project-dry-run-review-instruments.md:L5-L13`; `notes/first-target-project-dry-run-review-instruments.md:L29-L94`; `notes/first-target-project-dry-run-review-instruments.md:L96-L117`; `notes/first-target-project-dry-run-review-instruments.md:L151-L181`; `notes/first-target-project-dry-run-review-instruments.md:L201-L215`.

### notes/handoff-package-strategy-v0.1.md

Consistent. It is non-execution-source, requires the applicable execution source or owner rule, separates current truth from history, records authorities/permissions, identifies forbidden actions, and requires evidence paths. It is useful support for preventing target workspace or handoff materials from being treated as execution source.

**Evidence:** `notes/handoff-package-strategy-v0.1.md:L5-L13`; `notes/handoff-package-strategy-v0.1.md:L20-L57`; `notes/handoff-package-strategy-v0.1.md:L131-L197`; `notes/handoff-package-strategy-v0.1.md:L245-L258`.

### notes/handoff-replay-scorecard-v0.1.md

Consistent. It is non-execution-source, separates executor output from maintainer review, requires critical checks to pass before reviewed PASS, and treats wrong execution-source promotion, hallucinated repository writes, false dry-run/target claims, missing user approval, and unsupported assumption invention as serious failures.

**Evidence:** `notes/handoff-replay-scorecard-v0.1.md:L5-L12`; `notes/handoff-replay-scorecard-v0.1.md:L13-L31`; `notes/handoff-replay-scorecard-v0.1.md:L32-L59`; `notes/handoff-replay-scorecard-v0.1.md:L219-L237`.

### notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md

Consistent. It records a non-execution-source reviewed replay result, reviewed PASS, `quality_band: strong`, normalized score 95.9, and explicitly states that it does not start a real dry-run, select a target, ingest materials, write a target repository, or close user-decision gates.

**Evidence:** `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L5-L28`; `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L30-L38`; `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L61-L70`.

### notes/codex-task-results/MNEMOSYNE-057-result.md

Consistent as a non-execution-source result record. It accurately describes the user-approved minimal promotion and states that no target workspace was created, no target was selected, no target material was ingested, no target repository was written, and no real dry-run was started. It also records verification commands and expected changed files. As a result record, it is evidence only and does not itself become authority over current repository files.

**Evidence:** `notes/codex-task-results/MNEMOSYNE-057-result.md:L5-L61`; `notes/codex-task-results/MNEMOSYNE-057-result.md:L49-L56`; `notes/codex-task-results/MNEMOSYNE-057-result.md:L98-L163`; `notes/codex-task-results/MNEMOSYNE-057-result.md:L164-L172`.

### notes/codex-task-authoring-and-diff-verification-guidelines.md

Consistent. It is non-execution-source, reinforces that Codex result prose is insufficient without actual diff evidence, and directly addresses stale Codex branch / stale default-branch risks. This is important for any future cleanup task touching high-risk current/handoff/dry-run instrument files.

**Evidence:** `notes/codex-task-authoring-and-diff-verification-guidelines.md:L5-L12`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L23-L63`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L64-L77`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L142-L153`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L155-L180`.

### Additional file: notes/first-target-project-dry-run-minimal-profile.md

Partially stale. The file correctly states non-execution-source status, no target write, safe input defaults, no automation, target schema tailoring, and no copying of Mnemosyne's own schema by default. Its manifest path is stale, as covered in W-01.

**Evidence:** `notes/first-target-project-dry-run-minimal-profile.md:L5-L16`; `notes/first-target-project-dry-run-minimal-profile.md:L19-L46`; `notes/first-target-project-dry-run-minimal-profile.md:L76-L99`.

### Additional file: notes/first-target-project-dry-run-checklist.md

Consistent. It has clear non-execution-source status, no target write, public/synthetic/redacted input defaults, result semantics, and blocking checks for source reading, layer separation, public-safe boundary, no target write, and target schema tailoring.

**Evidence:** `notes/first-target-project-dry-run-checklist.md:L5-L14`; `notes/first-target-project-dry-run-checklist.md:L16-L30`; `notes/first-target-project-dry-run-checklist.md:L34-L187`.

### Additional file: notes/first-target-project-dry-run-result-template.md

Mostly consistent but stale on replay reference. It correctly says it is not execution source, not proof a real dry-run occurred, and cannot convert synthetic smoke-test evidence into a real dry-run PASS. It should replace the post-050 replay reference with post-053/current reviewed replay wording.

**Evidence:** `notes/first-target-project-dry-run-result-template.md:L5-L18`; `notes/first-target-project-dry-run-result-template.md:L20-L28`; `notes/first-target-project-dry-run-result-template.md:L29-L68`.

### Additional file: notes/first-target-project-fresh-replay-protocol.md

Consistent. It records protocol version `2026-06-23-post-MNEMOSYNE-053`, has read-only/no-target/no-material/no-write isolation rules, and clearly states that earlier replay evidence was invalidated by MNEMOSYNE-053 and that reviewed PASS depends on scorecard review.

**Evidence:** `notes/first-target-project-fresh-replay-protocol.md:L12-L19`; `notes/first-target-project-fresh-replay-protocol.md:L20-L36`; `notes/first-target-project-fresh-replay-protocol.md:L37-L50`; `notes/first-target-project-fresh-replay-protocol.md:L173-L207`.

## 5. Execution-source boundary review

The execution-source boundary is sound.

The current execution-source chain is:

1. `current/human-approved-spec.md` is the only Mnemosyne execution source.
2. Active context, handoff, startup instructions, TODO, open questions, research, candidates, decision records, task results, templates, and review instruments are not execution source.
3. If another file conflicts with the spec, the spec wins and the conflict should be recorded as an open question.
4. Target-project workspace files are explicitly not Mnemosyne execution source.

The target-project workspace principle does not create a second Mnemosyne execution-source root. It is phrased as a workspace/archive/design-factory pattern. The risk that `target-projects/<target_project_id>/` could be mistaken for Mnemosyne execution source is materially mitigated by repetition in the spec, proposal, manifest, onboarding package, review instruments, active context, handoff, and TODO.

Remaining risk is operational rather than conceptual: if a future executor reads only stale or partial non-execution-source files, it could follow stale artifact paths or stale replay references. The startup/onboarding read order and execution-source priority rules are designed to prevent that. The W-01 and W-02 repairs would further reduce the risk.

## 6. Target workspace / runtime truth source boundary review

The runtime-truth-source boundary is sound but would benefit from a clearer manifest authority field.

The current rule is:

- A target project repository or directory is the target project's running truth source when it exists and when that role is established by target authority.
- A Mnemosyne target workspace is not automatically that runtime truth source.
- The target workspace can hold target-specific authority/owner/source decisions, but only within that target scope.
- A target workspace can assume a runtime-truth-source role only if a target-local manifest or owner rule explicitly and user-approvedly says so.

This prevents the two main failure modes:

1. treating Mnemosyne's execution source as the target runtime truth source;
2. treating `target-projects/<target_project_id>/` as the target runtime truth source merely because it is inside the Mnemosyne repo.

Recommended schema improvement:

```yaml
target_runtime_truth_source:
  status: none | external_owner_rule_confirmed | workspace_manifest_user_approved | unknown_requires_owner_decision
  authority_path_or_external_pointer:
  approved_by:
  approved_at:
  scope:
  limitations:
```

This would be clearer than `workspace_is_target_runtime_truth_source: false | target_manifest_approved | unknown` because it separates role, authority path, approver, and scope.

## 7. User-input storage policy review

The current user-input storage policy is safe enough for the current no-ingestion state.

Strong safety controls are present:

- Manual import rules require repository visibility and material sensitivity checks before staging.
- Public or unverified visibility allows only public, synthetic, or explicitly redacted material.
- Secrets and credentials must not be committed under any visibility.
- Target-project originals/raw requirements may enter the repository only when safe for current visibility and user-approved.
- Unsafe originals remain outside the repository; only redacted references or external pointers may be stored.
- Target-scoped user input should go under `target-projects/<target_project_id>/01-user-input/` after approvals.

Remaining limitation: OP-08 remains open for broader privacy/redaction/access-control policy. That is acceptable because the current rules stop unsafe intake rather than allowing ambiguous intake. For sensitive real target materials, the safer default is external storage plus redacted pointer until OP-08 is closed or a target-specific privacy policy is approved.

## 8. Dry-run manifest adequacy review

The manifest is materially adequate to prevent accidental real dry-run, accidental workspace creation, accidental target material ingestion, and accidental target repository write.

Adequate controls already present:

- `run_kind: real_target_project | synthetic_smoke_test` distinguishes real and synthetic runs.
- `manifest_status: draft | user_approved | invalid` requires approval before real run.
- `target_execution_source_or_owner_rule` and `target_execution_source_status` prevent source invention.
- `source_items` include role, authority, owner, date/version, sensitivity, allowed use, and accessibility.
- `privacy_and_repository_boundary` and `input_safety_status` force safety classification.
- `target_project_workspace` fields record root, status, approval, execution-source status, runtime-truth-source status, and paths.
- `user_input_storage_policy` distinguishes not-provided, safe workspace storage, external reference, unsafe-do-not-store, and pending decision.
- `no_target_write_confirmed` is required by rule before a real dry-run.
- `target_materials_uploaded_or_ingested` is visible as a manifest field.
- `unsupported_assumptions` prevents silent invention.
- `stop_conditions_triggered` gives a halt surface.
- The rules explicitly say unsafe/ambiguous material stops the run and that workspace creation is not authorized merely by the template.

Recommended improvements:

```yaml
approval_record:
  target_selected:
    status: true | false | unknown
    approved_by:
    approved_at:
  target_workspace_root:
    status: approved | rejected | pending | not_applicable
    path:
    approved_by:
    approved_at:
  workspace_creation:
    status: approved | not_approved | pending | not_applicable
    approved_by:
    approved_at:
  user_input_storage_policy:
    status: approved | rejected | pending
    approved_by:
    approved_at:
  no_target_write:
    status: confirmed | not_confirmed | contradicted
    approved_by:
    approved_at:
  run_manifest:
    status: user_approved | draft | invalid
    approved_by:
    approved_at:

target_material_ingestion:
  status: none_provided | approved_to_ingest | ingested | unsafe_blocked | pending_user_decision
  allowed_material_types:
  prohibited_material_types:
```

These fields are not necessary for current PASS_WITH_WARNINGS, but they would make the manifest more robust under real target pressure.

## 9. Onboarding package adequacy review

The onboarding package is adequate as a first target-project dry-run entry point.

Strengths:

- It states its non-execution-source status.
- It has an authority map distinguishing Mnemosyne execution source, task-local user decisions, target source materials, target execution source, evidence-only research, and non-execution-source templates/checklists.
- It gives an exact read order.
- It requires target selection, safe input, authority/source map, no-target-write, and run manifest approval before real dry-run.
- It has actor permissions for ordinary ChatGPT, Codex Cloud, user, and target agent.
- It explicitly states that no target workspace is created until target selection, authority/source map, safety/privacy boundary, no-target-write, and run manifest are approved.
- It says producing the package does not start or pass a dry-run.

Weakness:

- Because the read order includes `notes/first-target-project-dry-run-minimal-profile.md` and `notes/first-target-project-dry-run-result-template.md`, stale text in those files can still influence a future executor. The onboarding package itself is aligned, but it should be accompanied by cleanup of those support instruments.

## 10. Current-state synchronization review

Current-state synchronization is broadly good.

Aligned live claims across active-context, TODO, handoff-current, open-questions, replay result, and MNEMOSYNE-057 result:

- replay-quality portion of the first-target dry-run gate is satisfied by post-MNEMOSYNE-053 reviewed PASS;
- target-project workspace principle is now in execution source;
- detailed MNEMOSYNE-056 layout remains non-execution-source reference;
- no target project has been selected;
- no real target-project dry-run has occurred;
- no target materials have been uploaded/ingested;
- no target repository has been written;
- next route requires target selection, authority/source map, safe input/user originals storage, no-target-write, and approved run manifest.

Minor defects:

- `handoff/handoff-current.md` duplicates the no-materials claim.
- `notes/first-target-project-dry-run-minimal-profile.md` has the stale old manifest path.
- `notes/first-target-project-dry-run-result-template.md` has the stale post-050 replay reference.

These are not enough to overturn the synchronized current-state model because the current compact view and execution source are clear.

## 11. Proposed repairs or improvements

Recommended repairs before any real target-project dry-run:

1. Update `notes/first-target-project-dry-run-minimal-profile.md`:
   - Replace `notes/target-project-dry-runs/<dry_run_id>/00-run-manifest.md after user-approved run creation` with the post-057 target-scoped path rule.
   - Suggested intent: `manifest_path: target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/00-run-manifest.md after target selection, target workspace approval, and user-approved run creation; otherwise not_applicable or external manifest path approved by user`.

2. Update `notes/first-target-project-dry-run-result-template.md`:
   - Replace “reviewed post-050 replay result” with “current reviewed replay result required by `notes/first-target-project-fresh-replay-protocol.md`; as of this audit, post-MNEMOSYNE-053 reviewed PASS is the synchronized replay-quality gate evidence.”

3. Tighten `notes/first-target-project-dry-run-manifest-template.md`:
   - Add explicit enums and authority metadata for workspace root approval, workspace creation approval, user-input storage policy approval, no-target-write, target material ingestion, and target runtime truth-source status.
   - Do not allow blank safety-critical fields to be interpreted as approval.

4. Optionally clean `handoff/handoff-current.md`:
   - Remove one duplicated no-target-materials line.

5. Add a short source-priority sentence to onboarding or manifest rules:
   - “If first-dry-run support instruments conflict, follow `current/human-approved-spec.md`, then the user-approved actual run manifest, then this onboarding package/manifest template; record the conflict instead of merging.”

6. For future target-specific lesson files, add a minimal lesson-candidate schema with explicit labels:

```yaml
lesson_candidate:
  target_project_id:
  evidence_path:
  sensitivity_status:
  authority_scope: target_project_specific
  global_promotion_status: example_only | candidate_pending_review | user_approved_global_rule
  non_execution_source: true
```

## 12. Whether a Codex task is recommended

**Yes, but only as a small deterministic cleanup task before any real target-project dry-run.**

The audit does not recommend a broad redesign. It recommends a narrow synchronization task because the stale minimal-profile path and stale post-050 result-template reference are exactly the kind of support-instrument drift that can later produce executor confusion.

This audit does not generate or launch a Codex task.

## 13. If a Codex task is recommended, proposed task scope only, not full task prompt

Proposed scope only:

- Touch only:
  - `notes/first-target-project-dry-run-minimal-profile.md`
  - `notes/first-target-project-dry-run-result-template.md`
  - optionally `notes/first-target-project-dry-run-manifest-template.md`
  - optionally `handoff/handoff-current.md`
  - new result record under `notes/codex-task-results/` if the maintainer wants a persisted task result.
- Do not edit `current/human-approved-spec.md` unless the maintainer explicitly approves a separate execution-source update.
- Do not create `target-projects/` or any dry-run folder.
- Do not ingest target materials.
- Do not write any target repository.
- Replace the stale old run path in the minimal profile with post-057 target-scoped path wording and explicit no-creation language.
- Replace the stale post-050 replay reference in the result template with current post-053/current reviewed replay language.
- Optionally add explicit enum/approval-authority fields to the manifest template.
- Optionally remove one duplicate no-materials line from `handoff/handoff-current.md`.
- Require `git status --short`, `git diff HEAD --stat`, `git diff HEAD --name-only`, targeted diffs, grep checks for removed stale phrases, and protected-file verification.

## 14. Evidence map with file paths and line references if available

| Claim | Evidence |
|---|---|
| Mnemosyne is a memory-system meta-agent work repository; repository visibility/Git history safety matters. | `README.md:L3-L9` |
| `current/human-approved-spec.md` is the sole execution source. | `current/human-approved-spec.md:L1-L5`; `current/human-approved-spec.md:L23-L35` |
| Active context, handoff, TODO, open questions, research, candidates, and result records are not execution source. | `current/human-approved-spec.md:L23-L35`; `current/active-context.md:L13-L18`; `handoff/handoff-current.md:L43-L51` |
| Target project repository/directory is the target running truth source, not Mnemosyne by default. | `current/human-approved-spec.md:L76-L80`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L48-L50` |
| Target workspace default root is `target-projects/<target_project_id>/`. | `current/human-approved-spec.md:L193-L195`; `current/todo.md:L7-L10`; `handoff/first-target-project-dry-run-onboarding-package.md:L63-L68`; `notes/first-target-project-dry-run-manifest-template.md:L47-L58` |
| Target workspace is not Mnemosyne execution source. | `current/human-approved-spec.md:L195-L196`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L42-L47` and `L155-L159`; `notes/first-target-project-dry-run-manifest-template.md:L51-L52` and `L89-L90`; `handoff/first-target-project-dry-run-onboarding-package.md:L67-L72` |
| Target workspace is not automatically target runtime truth source. | `current/human-approved-spec.md:L196-L197`; `notes/first-target-project-dry-run-manifest-template.md:L51-L52` and `L89-L90`; `handoff/first-target-project-dry-run-onboarding-package.md:L67-L72`; `notes/first-target-project-dry-run-review-instruments.md:L175-L181` |
| User originals/raw requirements require safety and user approval; otherwise use redacted references or external pointers. | `current/human-approved-spec.md:L204-L208`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L122-L140`; `handoff/first-target-project-dry-run-onboarding-package.md:L65-L71`; `notes/first-target-project-dry-run-manifest-template.md:L59-L65` and `L91-L93` |
| Target-specific lessons may be cited only as examples and do not auto-promote globally. | `current/human-approved-spec.md:L205-L208`; `notes/target-project-workspace-boundary-and-layout-proposal.md:L142-L154`; `notes/first-target-project-dry-run-review-instruments.md:L201-L215` |
| Workspace creation, target material ingestion, real dry-run, and target writes require prior approvals. | `current/human-approved-spec.md:L207-L208`; `notes/first-target-project-dry-run-manifest-template.md:L81-L93`; `handoff/first-target-project-dry-run-onboarding-package.md:L63-L72`; `current/todo.md:L13-L20`; `handoff/handoff-current.md:L81-L88` |
| Current state says no real dry-run, no target selection, no target material ingestion, no target write. | `current/active-context.md:L39-L48`; `current/todo.md:L23-L29`; `handoff/handoff-current.md:L23-L32`; `notes/codex-task-results/MNEMOSYNE-057-result.md:L57-L61` |
| Post-053 replay reviewed PASS satisfies only replay-quality portion of gate, not user-decision gates. | `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L11-L28`; `notes/replay-results/MNEMOSYNE-post-053-fresh-replay-reviewed-pass.md:L30-L38`; `current/active-context.md:L39-L44` |
| Stale old path remains in minimal profile. | `notes/first-target-project-dry-run-minimal-profile.md:L20-L22`; conflicting current rule in `notes/first-target-project-dry-run-manifest-template.md:L87-L93` |
| Stale post-050 replay reference remains in result template. | `notes/first-target-project-dry-run-result-template.md:L16-L18`; current protocol/gate in `notes/first-target-project-fresh-replay-protocol.md:L14-L18` and `L33-L35` |
| Handoff-current has duplicated no-materials wording. | `handoff/handoff-current.md:L28-L32` |
| Codex cleanup work should be verified by actual diff evidence, not result prose alone. | `notes/codex-task-authoring-and-diff-verification-guidelines.md:L64-L77`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L142-L153`; `notes/codex-task-authoring-and-diff-verification-guidelines.md:L155-L180` |

## 15. Limitations

- This was a read-only GitHub connector audit. No repository files were edited.
- No Codex task was generated or launched.
- No target was selected.
- No real target-project dry-run was started.
- No target materials were requested, uploaded, or ingested.
- No target repository was written.
- I did not enumerate the full repository tree with a local clone. I read the required files and several additional first-dry-run support files, and used repository search for key phrases. Therefore, undiscovered stale wording may exist outside the required/read files.
- Line references are based on the GitHub connector file content as read during this audit; small line-number shifts may occur if the repository changes after this audit.
- The current repository default branch was observed through the GitHub connector; exact default-branch HEAD commit was not independently resolved in this audit output.
