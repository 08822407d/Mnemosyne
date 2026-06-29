# Corrected Deep Research Prompt — DR4 rerun with robust report delivery

execute_in: new Pro Deep Research conversation/task
do_not_execute_in_current_maintainer_thread: true
repository_context: Mnemosyne user-input storage policy
output_primary: full report body in the Deep Research report/chat itself
output_optional_backup: downloadable Markdown file only if the UI actually creates a valid file
output_file_suggested_name: DR4_user_originals_requirements_redaction_governance_report.md

---

## Prompt to paste into Pro Deep Research

You are conducting Deep Research for Mnemosyne.

Write the final report in Chinese, with English technical terms where clearer.

## Critical output-delivery rule

The **full research report text must be present in the final Deep Research report body itself**. Do **not** make the chat/report body only a brief summary plus a download link.

You may additionally create a downloadable Markdown file named:

```text
DR4_user_originals_requirements_redaction_governance_report.md
```

but the downloadable file is only a backup. The final answer must still contain the complete report body.

If the UI cannot produce a valid downloadable file, or if the link would be a transient sandbox link, continue by writing the complete report in the report body. If the report is too long for one message, output it in clearly labeled chunks:

```yaml
package_id: DR4_user_originals_requirements_redaction_governance_report
chunk: N / total
instruction: wait for all chunks before ingestion/review
```

Do not use “brief summary + download link only” as the final answer.

## Research title

**DR4 — 用户原始构想、需求原文、整理版、用户决策、脱敏版与外部指针的治理模式研究**

## Background

Mnemosyne designs external persistent memory systems for target projects. After MNEMOSYNE-057, Mnemosyne has a high-level rule that target-project workspaces may live in its repository under:

```text
target-projects/<target_project_id>/
```

However, the most sensitive unresolved issue is how to handle:

- user original ideas;
- raw requirements;
- restated requirements;
- approved decisions;
- redacted versions;
- synthetic substitutes;
- external pointers;
- sensitive/private project material;
- Git history exposure;
- public/private repository switching.

Current candidate structure includes:

```text
target-projects/<target_project_id>/01-user-input/
  originals/
  restatements/
  decisions/
  redactions/
```

Mnemosyne needs a practical v0.1 policy before the first real target-project dry-run.

## Research questions

Answer directly:

1. How should raw user input, requirements originals, restatements, approved decisions, redactions, and synthetic substitutes be separated?
2. What authority level should each layer have?
3. How do requirements engineering, data governance, privacy engineering, and consulting documentation handle original vs interpreted requirements?
4. What should be stored in Git, what should stay outside Git, and how should external pointers be represented?
5. What are the risks of storing sensitive originals in a repo whose visibility may change?
6. How should Git history exposure affect the storage policy?
7. How should redaction be documented and verified?
8. How should AI-generated restatements be linked back to user-approved decisions without treating the model restatement as the original?
9. What policy should Mnemosyne adopt for public, private, unverified, or changing repository visibility?
10. What minimal policy should be in place before first real target-project dry-run?

## Sources to prioritize

Use current, high-quality sources:

- requirements engineering;
- privacy engineering;
- data governance;
- document retention and redaction;
- Git secret/sensitive data guidance;
- secure software development lifecycle;
- consulting/client documentation practices;
- AI system data handling;
- knowledge management.

Prefer primary sources, official docs, standards, and high-quality engineering/security sources.

## Required output structure

1. Executive summary
2. Direct answer: where should Mnemosyne store user originals / requirements / restatements?
3. Layer model
4. Authority model
5. Storage policy by repository visibility
6. Redaction and synthetic substitute policy
7. External pointer policy
8. Git history exposure analysis
9. User approval workflow
10. Candidate Mnemosyne v0.1 policy
11. Future v0.2 improvements
12. Evidence table with citations
13. Known uncertainty and limits

## Deliverables

### A. Storage decision matrix

Rows:

```text
original user idea
raw requirement
AI restatement
user-approved decision
redacted excerpt
synthetic substitute
external pointer
source map
authority note
```

Columns:

```text
store_in_repo_public
store_in_repo_private
store_if_visibility_unverified
authority_level
redaction_required
approval_required
preferred_path
```

### B. Recommended path policy

Using:

```text
target-projects/<target_project_id>/01-user-input/
  originals/
  restatements/
  decisions/
  redactions/
```

Or propose alternatives.

### C. Redaction manifest schema

```yaml
redaction_manifest:
  source_item_id:
  original_storage_status:
  redacted_file_path:
  redaction_method:
  removed_categories:
  reviewer:
  approved_by_user:
  residual_risk:
```

### D. External pointer schema

```yaml
external_source_pointer:
  source_id:
  location_type:
  location_description:
  owner:
  access_status:
  authority_level:
  sensitivity:
  allowed_use:
  not_stored_in_repo_reason:
```

### E. Candidate updates for Mnemosyne

Separate:

```text
execution_source_candidate
manifest_template_candidate
target_workspace_policy_candidate
open_question
defer_to_v0.2
```

## Constraints

- Do not assume storing originals in Git is safe.
- Do not assume private repo removes all risk.
- Do not ignore Git history exposure.
- Do not treat AI restatements as original requirements.
- Do not propose automatic ingestion for v0.1.
- Clearly separate evidence from recommendations.
- Do not treat this research report as Mnemosyne execution source.
