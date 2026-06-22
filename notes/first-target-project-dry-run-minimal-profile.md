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
schema_tailoring_rationale: "Explain why this target project needs the selected 3 to 7 core memory files/roles, and why omitted candidate roles are unnecessary for this first design. Do not copy the Mnemosyne directory/file layout by default; file names and locations are provisional target-project design choices. 不得默认照搬 Mnemosyne 的目录或文件布局。"
candidate_core_memory_roles_not_a_required_package:
  - target execution source
  - active work context
  - handoff
  - task/TODO state
  - open questions
  - raw/original-source evidence
  - decision record
selected_core_memory_files:
  instruction: "Select only 3 to 7 core memory files/roles that the specific target project actually needs. Do not prepopulate a fixed seven-file Mnemosyne-shaped schema."
  items:
    - role:
      proposed_path:
      why_needed:
      authoritative_or_non_authoritative:
      update_owner_or_actor:
      update_trigger:
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
