# Target-Project Intake Form Filling Guide v0.1

## Positioning

- Non-execution-source support guidance.
- Complements `notes/first-target-project-intake-and-approval-forms-v0.1.md`.
- Does not override `current/human-approved-spec.md`.
- Does not make intake form completion an execution-source rule by itself.
- Use for new concrete target projects where Mnemosyne is expected to design, build, review, or dry-run an external persistent memory system.
- Not required for ordinary Mnemosyne maintenance or minor follow-up within an already selected target unless authority/safety/material/workspace boundaries changed.

## When to use

Use before:

- selecting a new target project for memory-system design;
- preparing a target-specific run manifest;
- creating a target workspace;
- staging/importing target materials;
- starting a real target dry-run;
- drafting a target delivery/handoff package.

Do not use as a substitute for:

- user-approved run manifest;
- target workspace creation approval;
- target material ingestion approval;
- target repository write approval;
- target runtime truth-source declaration.

## Filling principles

- Fill only what is known.
- Mark unknowns explicitly.
- Do not invent missing project history.
- Do not reconstruct lost source conversations as fact.
- Do not ask the user to upload raw materials during initial intake.
- Treat public/unverified repo visibility as public-risk.
- Raw originals and raw requirements default outside Git.
- `target-projects/<target_project_id>/` is a planned/default root, not a created path.
- A target workspace is not Mnemosyne execution source.
- A target workspace is not automatically target runtime truth source.
- no-target-write must be explicit before any dry-run preparation.

## Field guidance

### 1. `target_project_selection`

- Purpose: identify the target, why it is first, and what is out of scope.
- Good answer pattern: name, stable ID candidate, owner/decision authority, first-target rationale, expected value, non-goals, and `raw_material_upload_now: no`.
- Common mistakes: selecting a vague domain instead of a concrete project; treating research reports as final target truth; asking for raw uploads too early.
- Blocking values: missing owner/decision authority, request to upload raw materials immediately, or unclear target identity.
- Example: `target_project_name: Meta-Agent`; `target_project_id_candidate: meta-agent`; `raw_material_upload_now: no`.

### 2. `authority_source_map`

- Purpose: map who decides, which sources may be used, which are forbidden, and how conflicts are resolved.
- Good answer pattern: user/owner authority first, Mnemosyne execution source only for Mnemosyne boundaries, target owner rule or runtime truth source marked declared or unknown.
- Common mistakes: using model memory as authority; reconstructing lost conversations as fact; treating support notes as execution source.
- Blocking values: authority missing, conflicting write permissions, or target runtime truth source invented without owner approval.
- Example: `target_runtime_truth_source: none_declared_yet` with unresolved follow-up before real dry-run.

### 3. `safe_input_policy`

- Purpose: decide what input can be stored or referenced under current repository visibility and sensitivity constraints.
- Good answer pattern: public, synthetic, explicitly redacted, or external-pointer-only categories; raw originals outside Git by default.
- Common mistakes: assuming a public repository can hold private/raw material; omitting redaction manifest or pointer safety review.
- Blocking values: secrets, credentials, private source, customer/confidential materials, unredacted personal data, or raw target materials offered before approval.
- Example: `store_raw_originals_in_repo: no`; `user_originals_storage_default: outside_git_pointer_only`.

### 4. `target_workspace`

- Purpose: plan a future workspace root without creating it prematurely.
- Good answer pattern: proposed root, exception if any, `create_now: false`, and explicit later approval requirement.
- Common mistakes: creating `target-projects/<target_project_id>/` during intake; treating the workspace as execution source.
- Blocking values: workspace creation requested without approved manifest/safety/no-write gates.
- Example: `proposed_root: target-projects/meta-agent/`; `creation_requires_explicit_later_approval: true`.

### 5. `no_target_write_confirmation`

- Purpose: prove dry-run preparation will not write the target repository or target workspace without approval.
- Good answer pattern: target repository write `false`, workspace write `false_until_explicit_approval`, user/operator confirmation fields, and proof method.
- Common mistakes: allowing “minor” writes; confusing Mnemosyne support-file edits with target repository writes.
- Blocking values: target write allowed, unclear target repository, or missing no-write proof plan.
- Example: `target_repository_write_allowed: false`.

### 6. `next_step`

- Purpose: constrain what happens after intake.
- Good answer pattern: ask user to approve/revise/reject draft manifest; do not silently start dry-run.
- Common mistakes: treating intake completion as dry-run approval; asking for raw materials as the next step.
- Blocking values: `proceed_to_real_dry_run_now` or any implicit workspace/material/write action.
- Example: `proceed_to_draft_run_manifest_next: ask_me_first`.

### 7. `unresolved_items_after_this_draft`

- Purpose: preserve unknowns instead of filling them with assumptions.
- Good answer pattern: list unresolved fields, current value, reason, and required owner decision.
- Common mistakes: omitting target runtime truth source because it is uncomfortable; converting assumptions into facts.
- Blocking values: unresolved write authority, material safety, runtime truth source, or owner decision needed before real dry-run.
- Example: `target_runtime_truth_source: none_declared_yet`.

## Minimum viable intake

A minimum viable intake must identify:

```yaml
target_project_name:
target_project_id_candidate:
owner_or_decision_authority:
why_this_target_first:
known_non_goals:
raw_material_upload_now: no
target_repository_write_allowed: false
target_workspace_write_allowed: false_until_explicit_approval
proceed_to_draft_run_manifest_next:
```

## Approval interpretation

- Intake completion can approve target selection for manifest drafting if the user explicitly says so.
- Intake completion does not approve a real dry-run.
- Intake completion does not approve workspace creation.
- Intake completion does not approve target material ingestion.
- Intake completion does not approve target repository write.
- Draft run manifest creation is still not real dry-run execution.

## Example normalization

Use Meta-Agent as a pattern but not a universal template:

```yaml
target_project_type:
  primary: ai_agent_project
  secondary:
    - long_term_research
    - software_development_methodology
  classification_status: hybrid
```

## Quality checklist

- No raw materials requested.
- Owner/authority clear.
- Source priority clear.
- Forbidden sources clear.
- Safe input policy conservative.
- Workspace path planned/not created.
- No-target-write confirmed.
- Runtime truth source either declared, none, or explicitly unresolved.
- Next step does not silently start dry-run.
