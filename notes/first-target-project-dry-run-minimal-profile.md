# First Target-Project Dry-Run Minimal Profile

## Positioning and boundaries

- Positioning: non-execution-source test profile; provisional first-dry-run instrument; not a target-project delivery package.
- Current Mnemosyne execution source remains `current/human-approved-spec.md`; this profile is not execution source.
- The target project must eventually have its own execution source; do not use Mnemosyne's execution source as the target project's runtime truth source.
- The first run is design-only unless separately approved; do not write to the target project.
- Use public / synthetic / explicitly_redacted material by default.
- Do not introduce automation, MCP, RAG, Actions, or multi-agent coordination.
- Template completeness is not success; next-executor usability is part of success.
- Unpromoted D-01-D-07 content is not execution source.
- Reference, do not duplicate, the existing template packs: `notes/template-pack-review-and-first-scenario-selection.md`, `notes/target-project-memory-system-template-pack.md`, and `notes/delivery-manifest-template-pack.md`.

## Minimal profile fields

```yaml
dry_run_id: MNEMOSYNE-DRYRUN-001-PROVISIONAL
target_project_name: unknown_until_user_selects
target_project_type: unknown_until_user_selects
design_only: true by default
input_safety: public / synthetic / explicitly_redacted by default
target_goal: "State the target project's practical goal in 1-3 sentences; mark unknowns explicitly."
memory_system_goal: "State what persistent memory should help the target project remember, update, and hand off."
allowed_source_materials:
  - public project description or synthetic substitute
  - explicitly redacted user-provided notes
  - target-project execution source if it exists and is safe to use
  - current Mnemosyne template-pack references, as design references only
prohibited_sensitive_materials:
  - secrets or credentials
  - private source code unless separately approved for the repository visibility
  - customer/confidential data
  - unapproved personal data
  - unredacted proprietary raw materials
target_execution_source_or_unknown: unknown_until_user_confirms
3_to_7_core_memory_files:
  - target/current/human-approved-spec.md or equivalent target execution source
  - target/current/active-context.md
  - target/handoff/handoff-current.md
  - target/handoff/startup-instructions.md
  - target/current/todo.md
  - target/current/open-questions.md
  - target/notes/decision-log.md
update_workflow:
  - read target execution source first, if present
  - record unknowns instead of inventing missing state
  - separate raw, evidence, candidate, decision, handoff, and execution layers
  - update only design artifacts inside Mnemosyne unless target write approval is separately granted
handoff_requirement: "A fresh ordinary Thinking-model session can resume from the stated execution source, active context, handoff, TODO, and open questions without hidden assumptions."
unsupported_assumptions:
  - target project has not yet been selected
  - target execution source may not exist yet
  - tool access to target project is unverified
  - target repository visibility and sensitivity are unverified until checked
  - no automation, MCP, RAG, Actions, or multi-agent coordination is assumed
expected_outputs:
  - completed minimal profile
  - completed dry-run checklist
  - issue-log entries for observed memory-system failures
  - dry-run result record usable by the next executor
acceptance_criteria:
  - source priority is explicit and evidence-linked
  - design-only/no-target-write boundary is preserved
  - public-safe input boundary is preserved
  - unknowns and unsupported assumptions are complete enough for review
  - next executor can use the artifacts without reading full template packs first
stop_conditions:
  - target material is sensitive, unsafe, or ambiguous for current repository visibility
  - target write is requested without separate approval
  - execution source conflict cannot be resolved by the stated priority rule
  - required target-project facts are unknown and would be invented
  - proposed output depends on unverified automation or platform capability
user_confirmations:
  - selected target project or synthetic substitute
  - repository/storage visibility and sensitivity boundary
  - whether a target execution source exists
  - approval status for any non-public input
  - confirmation that the run remains design-only unless separately approved
```
