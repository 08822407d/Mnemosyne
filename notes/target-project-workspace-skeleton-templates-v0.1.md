# Target-Project Workspace Skeleton Templates v0.1

## Positioning

- Non-execution-source workspace skeleton guidance.
- Used only after target selection, authority/source map, safety/privacy boundary, no-target-write, and run manifest approval.
- This file does not create any target workspace.
- Default target root remains `target-projects/<target_project_id>/`, unless the user approves an exception.

## 1. Target workspace root README banner

```markdown
# <target_project_id> Workspace

- This workspace is target-project-scoped.
- This workspace is not Mnemosyne execution source.
- This workspace is not automatically target runtime truth source.
- Target runtime truth source role requires target-local manifest / owner rule and user approval.
- Do not use this workspace to update Mnemosyne global rules without candidate review and user approval.
```

## 2. `01-user-input/README.md`

```markdown
# 01-user-input

This folder stores target-scoped safe input artifacts, decisions, redactions, and pointers.

Default rule:

- Raw user originals and raw requirements default outside Git.
- `originals/` is pointer/README-only by default.
- AI/human restatements are explanatory interpretation, not original requirements or approved baseline.
- `decisions/` stores user-approved decisions only.
- `redactions/` stores approved redacted excerpts, synthetic substitutes, and redaction manifests.
- External pointers must not contain secrets, credentials, access tokens, signed URLs, private absolute paths, sensitive precise locations, or unapproved personal/confidential data.
```

## 3. `01-user-input/originals/README.md`

```markdown
# originals

Default: external pointers or README only.

Do not store raw originals in Git unless all of the following are true:

- current repository visibility is verified;
- material is safe for that visibility;
- user explicitly approves in-repo storage;
- Git history exposure is acknowledged;
- authority/source map records owner, sensitivity, allowed use, and retention.

Unsafe originals: do not store.
```

## 4. Lesson candidate schema

```yaml
lesson_candidate:
  target_project_id:
  evidence_path:
  sensitivity_status:
  redaction_status:
  authority_scope: target_project_specific
  non_execution_source: true
  global_promotion_status: example_only | candidate_pending_review | user_approved_global_rule
  required_before_global_promotion:
    - candidate_review
    - scope_analysis
    - sensitivity_review
    - user_approval
```
