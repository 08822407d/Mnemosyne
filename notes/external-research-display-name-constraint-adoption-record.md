# External Research Short Display-Name Constraint — Adoption Record

```yaml
record_id: MNEMOSYNE-EXTERNAL-RESEARCH-DISPLAY-NAME-ADOPTION-001
created_by_task: MNEMOSYNE-189
source_issue: 250
owner_instruction: current_conversation_formally_implement_the_new_constraint
status: adopted_on_human_merge_of_MNEMOSYNE_189_PR
execution_source_modified: false
guard: current/external-research-display-name-guard.md
registry: notes/registries/project-research-display-name-registry-v0.1.md
```

## 1. Decision

Adopt a compact display alias for GPT Deep Research, Fable-class research, and equivalent one-run external work.

```text
<PROJECT_ABBR>-DR-<SEQUENCE> <SHORT_TOPIC>
```

Adopted project abbreviations:

```yaml
Mnemosyne: MNE
Meta_Agent: MA
```

## 2. Compatibility correction to the Issue proposal

Issue #250 proposed a universal three-digit sequence. The adopted rule uses three digits by default for new projects, while preserving an established project convention when canonical IDs already exist.

Therefore:

- Mnemosyne begins with `MNE-DR-001`;
- existing Meta-Agent canonical IDs such as `MA-DR-08` are not renamed to `MA-DR-008`;
- future Meta-Agent allocation remains owned by the Meta-Agent route.

This avoids a presentation-only change breaking canonical research identity or historical references.

## 3. Initial aliases

```yaml
FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001:
  display_name: MNE-DR-001 验证包审计

FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001:
  display_name: MNE-DR-002 表面威胁
```

No current Fable task is resumed or executed by this adoption.

## 4. Issue handling

The canonical MNEMOSYNE-189 pull request should use `Closes #250`. GitHub issue and pull-request numbers share one repository-wide sequence; Issue #250 already occupies number 250, and Meta-Agent PRs #251/#252 were subsequently assigned and merged. MNEMOSYNE-189 does not reserve or guess its PR number before PR creation.

## 5. Boundaries

This record does not modify `current/human-approved-spec.md`, rename historical tasks, authorize quota use, or change another project's truth source.
