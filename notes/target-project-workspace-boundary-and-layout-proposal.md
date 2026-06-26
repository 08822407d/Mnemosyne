# Target-Project Workspace Boundary and Layout Proposal

```yaml
proposal_id: MNEMOSYNE-056-target-project-workspace-boundary
status: candidate_design_proposal_not_execution_source
created_by_task: MNEMOSYNE-056
positioning: target-project content stored in Mnemosyne repo is an intentional workspace pattern, not merely a Codex Cloud workaround
execution_source_impact: none_in_this_task
requires_user_approval_before_spec_promotion: true
```

## Problem

Before the first real target-project dry-run, Mnemosyne needs a stable boundary for project-specific content. Current execution-source boundaries already distinguish Mnemosyne as the memory-system meta-agent work repository from a target project's own running truth source, but the repository still needs a proposed layout for target-project work that is designed and archived by Mnemosyne before, during, and after a dry-run.

It is insufficient to treat all target-related material as temporary task artifacts. Target-specific runtime files, delivery preparation, Mnemosyne-generated intermediate design/build/review work, dry-run records, feedback, issue evidence, and scoped examples need a consistent home under the target project's own workspace boundary.

This proposal therefore treats target-project content stored inside the Mnemosyne repository as a first-class, intentional target-project workspace pattern. It should be understood as a normal Mnemosyne design-factory and design-archive pattern, not merely a Codex Cloud workaround or temporary compromise for current attachment/write limitations.

This file is a candidate design proposal only. It does not modify `current/human-approved-spec.md`, does not create a target workspace, and does not authorize a real target-project dry-run.

## Three-layer boundary

Mnemosyne target-project work should use three distinct layers:

```text
1. Mnemosyne global layer
2. Target-project workspace layer inside Mnemosyne repo
3. Target project runtime truth source / external repository, when one exists
```

### 1. Mnemosyne global layer

The Mnemosyne global layer owns methodology, execution source, reusable templates, research summaries, cross-project lessons, capability boundaries, and global process rules. Examples include `current/human-approved-spec.md`, global handoff strategy notes, reusable review instruments, and cross-project self-improvement candidates.

Global-layer files must not silently absorb target-specific assumptions as general policy. Any promotion from project-specific evidence into global Mnemosyne methodology needs candidate review and user approval.

### 2. Target-project workspace layer inside Mnemosyne repo

The target-project workspace layer owns all project-specific design/build/review/dry-run/delivery preparation artifacts while the target is being designed by Mnemosyne. This includes target-scoped user input records that are safe for the repository, source/authority maps, intermediate analysis, candidate schema/workflows, dry-run logs, issue records, delivery package drafts, and project-specific lesson candidates.

This layer is inside the Mnemosyne repository but is not Mnemosyne's execution source. It is a bounded workspace and archive for the target project as handled by Mnemosyne.

### 3. Target project runtime truth source / external repository

The target project runtime truth source owns final operational truth for that target when it exists. This may be an external repository, a user-controlled directory, or a clearly marked target runtime directory. It must not be confused with Mnemosyne's own execution source, and it must not be assumed to exist or be writable before the user approves the target, authority, safe-input boundary, no-target-write setting, and run manifest.

## Proposed root directory

Proposed root:

```text
target-projects/
```

Positioning:

- `target-projects/` is a first-class long-lived workspace root for target projects handled by Mnemosyne.
- It is not a temporary inbox.
- It is not Mnemosyne execution source.
- It is not automatically the external target runtime truth source unless a target-local manifest says so and the user approves it.
- It is subject to repository visibility, sensitivity, privacy, and Git history exposure rules.
- It should not be created for a real target until a target project is selected and safety/authority decisions are approved.

## Target project directory template

Candidate template:

```text
target-projects/<target_project_id>/
  00-project-meta/
    project-manifest.md
    authority-and-source-map.md
    privacy-and-safety.md
    status.md
  01-user-input/
    originals/
    restatements/
    decisions/
    redactions/
    README.md
  02-mnemosyne-design-workbench/
    intake/
    analysis/
    candidate-memory-schema/
    candidate-workflows/
    reviews/
    issue-log/
    unsupported-assumptions.md
  03-delivery-package/
    delivery-manifest.md
    runtime-memory-package/
    handoff-package/
    drift-review-todo.md
  04-dry-runs/
    <dry_run_id>/
      00-run-manifest.md
      01-intake-and-design-draft.md
      02-delivery-and-handoff-draft.md
      03-result-and-postmortem.md
  05-feedback-and-lessons/
    project-feedback/
    mnemosyne-lesson-candidates/
    example-excerpts/
```

Directory intent:

- `00-project-meta/`: target identity, status, authority, source mapping, visibility, sensitivity, and safety decisions.
- `01-user-input/`: target-scoped user originals, restatements, decisions, and redacted substitutes when approved for repository storage.
- `02-mnemosyne-design-workbench/`: Mnemosyne-generated target-specific intake, analysis, schema/workflow candidates, reviews, issue logs, and unsupported assumptions.
- `03-delivery-package/`: delivery manifest, runtime memory package, handoff package, and drift-review TODO prepared for the target.
- `04-dry-runs/`: target-scoped dry-run manifests, drafts, results, and postmortems.
- `05-feedback-and-lessons/`: project feedback, issue evidence, lesson candidates, and example excerpts that may later support Mnemosyne-global improvements.

This task does not create `target-projects/` or any real target-project directory. The layout above is only a proposal in a code block.

## User original / requirement placement policy options

The user has not finalized where original user ideas, raw requirements, and restatements should live. The following is a candidate policy requiring user confirmation before any execution-source promotion or real target-project use.

Recommended policy:

- Put target-specific user input under `target-projects/<target_project_id>/01-user-input/`.
- Use `originals/` only for material that is safe and approved for current repository visibility.
- Use `restatements/` for Mnemosyne-restated requirements and structured interpretations.
- Use `decisions/` for user-approved decisions and authority choices.
- Use `redactions/` for redacted/synthetic substitutes when originals are sensitive.
- If original material is unsafe for the current repository, do not put it in the repo; store only a redacted reference / external pointer approved by the user.

Candidate options for user decision:

1. Adopt the recommended target-scoped placement policy for the first target dry-run.
2. Keep originals outside the repository by default and store only redacted summaries or pointers under `01-user-input/`.
3. Split high-authority user decisions into `00-project-meta/authority-and-source-map.md` while keeping raw/restated requirement material under `01-user-input/`.
4. Defer originals entirely until a privacy/redaction/access-control policy is approved, using synthetic examples for the first dry-run if needed.

## Feedback-to-Mnemosyne lesson boundary

Project feedback and target-specific issue evidence should live inside the target project workspace. Cross-project generalized lessons, methodology improvements, and Mnemosyne self-improvement records should live in the Mnemosyne global layer.

When a Mnemosyne-global lesson cites a concrete project, the citation should use a stable path and explicit labels, including:

- `example_only`
- `target_project_specific`
- `non_execution_source`
- sensitivity / redaction status

Global lessons should not duplicate full target content unless explicitly justified and safe. A target-specific design must not become global Mnemosyne policy merely because it worked for one target. Promotion requires candidate review, scope analysis, sensitivity review, and user approval.

## Authority and safety rules

- `current/human-approved-spec.md` remains Mnemosyne's only execution source.
- Target project workspace files are not Mnemosyne execution source.
- Target project workspace files may contain target-specific authority decisions, but only within that target project scope.
- No target project has been selected yet; no target workspace should be created yet.
- Repository visibility must be reverified before placing any target materials in this repository.
- If the repository is public or unverified, only public, synthetic, or explicitly redacted target material may be placed inside target-project workspaces.
- Removing or moving files later does not remove Git history exposure.
- No target materials should be ingested until the user approves the target, source map, safety status, authority boundary, and run manifest.
- No target repository should be written unless separately approved.

## Candidate promotion path

Future promotion may require:

1. user review of this proposal;
2. decision on user-input/original/restatement placement;
3. decision on whether `target-projects/` becomes the standard root;
4. update to execution source if user approves the high-level principle;
5. update to onboarding/run-manifest templates;
6. migration of future dry-run folder conventions from `notes/target-project-dry-runs/<dry_run_id>/` to target-scoped workspace paths, if approved.

## Immediate recommendation before first target dry-run

Before selecting the first real target, the user should approve or revise this target-project workspace layout. The first target dry-run should use a target-scoped workspace manifest even if no real target files are written.

Do not create a target workspace until a target is selected and safety/authority decisions are approved. Do not treat this proposal as execution source unless and until it is promoted through explicit user approval and an execution-source update.
