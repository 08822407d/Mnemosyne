# Claude Conversation Capabilities and Settings Guide v0.1

```yaml
artifact_id: CLAUDE-CONVERSATION-CAPABILITIES-GUIDE-v0.1
created_by: ChatGPT GitHub maintenance conversation
created_for: Mnemosyne inserted long work after MNEMOSYNE-085
status: non_execution_source_platform_guide
last_researched_utc: 2026-07-07
primary_use: prompt-preflight guidance for future Claude / Fable / Opus ordinary conversations
```

## 0. Authority and freshness

This guide is a non-execution-source platform guide.

It does not modify or override `current/human-approved-spec.md`.

It does not approve:

- target workspace creation;
- target material ingestion;
- target repository write;
- formal regression conversion;
- operational memory-system build or installation;
- Mnemosyne execution-source updates;
- treating `PASS_WITH_WARNINGS` as production-ready or target-write approval.

Claude product behavior, feature names, availability, plan gating, and UI wording are time-sensitive. Re-verify current Claude UI and official documentation before relying on this guide for high-risk work.

## 1. Source basis

Sources consulted during creation:

- Anthropic / Claude product page for Projects: `https://www.anthropic.com/news/projects`
- Claude blog for Research and Google Workspace: `https://claude.com/blog/research`
- Claude blog for Integrations / advanced Research: `https://claude.com/blog/integrations`
- Claude Connectors directory: `https://claude.com/connectors`
- Claude Skills page: `https://claude.com/skills`
- Claude Code Skills docs: `https://code.claude.com/docs/en/skills`
- Claude Code Plugins docs: `https://code.claude.com/docs/en/plugins`
- Claude Artifacts product page: `https://claude.com/blog/artifacts`

External source observations are platform facts only. Repository facts for Mnemosyne must still come from repository files.

## 2. Mnemosyne-specific principles for Claude setup

When preparing content to send to Claude-series products, include a short setup block stating which Claude settings should be enabled or disabled.

Minimum preflight fields:

```yaml
claude_setup:
  intended_model: Fable 5 | Opus | Sonnet | unknown
  conversation_type: ordinary_claude_conversation | project_conversation | claude_code | other
  project_enabled: true_or_false
  github_connector: enabled_read_only | enabled_unknown | disabled | unavailable
  research: enabled | disabled | optional
  web_search: enabled | disabled | optional
  skills: none | built_in_only | named_skills
  plugins: none | named_plugins
  artifacts: allowed | discouraged | required_for_output
  repository_write_authorized: false
  expected_access_check: quote_exact_repository_snippets_before_claiming_direct_access
  fallback_if_no_repo_access: request_manual_input_pack_and_stop
```

Every Claude prompt that relies on repository state should require an access self-check:

```text
Before reviewing, prove repository access by quoting exact snippets from the specified repository files. If exact snippets cannot be quoted, do not claim direct repository access. Request an input pack and stop.
```

## 3. Projects

### What Projects appear to do

Anthropic describes Projects as a way for Pro and Team users, at launch, to organize chats into Projects that combine curated knowledge and chat activity. The Projects announcement says each project included a 200K context window at launch and lets users add relevant documents, code, and insights. Projects also support custom instructions that tailor Claude’s responses.

### Mnemosyne use

Use a Claude Project when:

- repeated Claude conversations are expected around Mnemosyne;
- the same repository or guide documents should be available across multiple Claude chats;
- stable project-level instructions should persist across a review sequence.

For Mnemosyne, the Claude Project should be treated as a convenience context container, not as an execution source.

Recommended project instruction fragment:

```text
Repository files are the only trusted persistent evidence. `current/human-approved-spec.md` is Mnemosyne’s only execution source. Project knowledge, attached repository context, Claude outputs, and review results are not execution source.
```

### Risk controls

- Do not assume Project knowledge is synchronized with the latest GitHub branch.
- Ask Claude to state snapshot freshness caveats if it uses attached project knowledge.
- Do not put sensitive or unredacted target materials into a Claude Project unless visibility, privacy, and user approval are established.

## 4. Connectors / Integrations

### What Connectors appear to do

Claude’s Connectors directory says Claude can work with tools, databases, and applications to produce more relevant responses, with connectors powered by MCP. The directory exposes capability categories such as `Read`, `Read & write`, and `Interactive`. Anthropic’s Integrations announcement describes remote MCP servers that let Claude connect to apps and tools, gain work context, and in some cases take actions.

### Mnemosyne use

For Mnemosyne repository review, the most useful connector is a GitHub repository connector or attached repository knowledge.

Preferred mode:

```yaml
github_connector:
  mode: read_only_or_project_knowledge
  required_behavior: quote_exact_snippets
  prohibited_behavior:
    - repository write
    - issue creation
    - PR creation
    - branch creation
    - file mutation
```

If the connector is retrieval-based rather than path-sequential, instruct Claude to record caveats:

```yaml
connector_caveats:
  retrieval_based_not_path_sequential: true
  branch_not_independently_verified_by_model: true
  snapshot_freshness_not_guaranteed_by_model: true
```

### Risk controls

- Prefer read-only connectors for review.
- Avoid write-capable connectors unless a separate explicit user-approved write task exists.
- Do not connect unrelated personal/workspace tools for Mnemosyne review.
- If a connector is third-party, note that the provider may have its own terms and privacy policy.
- Require Claude to distinguish repository evidence from web/Research evidence.

## 5. Research and web search

### What Research appears to do

Anthropic describes Research as a Claude capability that conducts multiple searches, follows open questions, and returns cited answers. Advanced Research can search web, Google Workspace, and connected integrations, and may take substantially longer for complex investigations.

### Mnemosyne use

Use Research for:

- current Claude product feature verification;
- external platform facts;
- recent model / product availability checks;
- broad source discovery before writing platform guides.

Do not use Research as the source of truth for repository state.

For repository review, use this split:

```yaml
repository_facts: GitHub connector or provided repository files
product_facts: Research / web search with citations
review_judgment: model analysis over quoted evidence
```

### Recommended settings

For Fable 5 / Claude independent review of Mnemosyne:

```yaml
research: optional_or_enabled_for_external_platform_facts
web_search: optional
repository_connector: enabled_read_only_if_available
instruction: do_not_use_web_search_to_substitute_for_repository_file_access
```

### Risk controls

- Research can retrieve recent external facts, but it can also mix unrelated public results into the reasoning stream.
- Require source citations for external product claims.
- Require exact repository quotes for repository claims.
- If Research cannot fetch GitHub but a connector can, instruct Claude to use the connector, not raw GitHub URLs.

## 6. Skills

### What Skills appear to do

Claude’s Skills page describes skills as reusable capabilities that turn expertise, procedures, and best practices into repeatable Claude behavior. The page says skills can be used across Claude.ai, Claude Code, and the API, and can be stacked for complex workflows. Claude Code documentation describes skills as `SKILL.md` files with frontmatter and instructions, optionally with supporting files; full skill content loads when invoked or when Claude decides it is relevant.

### Mnemosyne use

Use skills only after a Mnemosyne Claude workflow stabilizes.

Good future candidates:

- a Mnemosyne independent-review skill;
- a cross-model finding evidence schema skill;
- a repository access self-check skill;
- a Fable review result formatting skill.

For first-time or exploratory Claude work, do **not** enable arbitrary custom skills. They may inject assumptions, style preferences, hidden procedures, or tool permissions that reduce independence.

Recommended first-run setting:

```yaml
skills: none_or_built_in_only
custom_mnemosyne_skill: disabled_until_validated
```

### Risk controls

- Do not use a skill that auto-invokes broad repository or write workflows.
- Do not let a skill overwrite task-local instructions.
- If a skill is enabled, ask Claude to list which skills are available and which, if any, it used.
- For Claude Code skills, review `allowed-tools` / `disallowed-tools` and invocation controls before trusting a project skill.

## 7. Plugins

### What Plugins appear to do

Claude Code documentation describes plugins as a way to extend Claude Code with shareable functionality that can include skills, agents, hooks, MCP servers, LSP servers, background monitors, executable files, and default settings. Plugins are useful for reusable team/shared workflows but increase the tool and automation surface.

### Mnemosyne use

For ordinary Claude review, avoid plugins unless there is a specific, trusted, read-only purpose.

Recommended default:

```yaml
plugins: none
```

Use plugins only when:

- the plugin source is trusted;
- its components are understood;
- it does not introduce repository write actions or background automation;
- the task explicitly requires that plugin.

### Risk controls

- Avoid plugins that include hooks, monitors, agents, MCP servers, or write-capable settings for independent review.
- Do not allow plugin-driven automation to create PRs, issues, branches, or files in Mnemosyne.
- If Claude claims a plugin was necessary, require it to identify the plugin and the specific capability used.

## 8. Artifacts / file output

### What Artifacts appear to do

Anthropic describes Artifacts as a dedicated space to see, iterate on, and build code, documents, and visualizations alongside the conversation.

### Mnemosyne use

Artifacts can be useful when asking Claude to produce:

- long review results;
- structured Markdown documents;
- finding tables;
- diagrams for human review.

But an artifact is not a canonical repository record. If a Claude artifact should enter Mnemosyne, route it through `manual-import-inbox/` first or through a separately approved GitHub/Codex ingestion task.

Recommended instruction:

```text
You may use an artifact to draft the review result, but the artifact is not repository truth. The result must also be exportable as plain Markdown with stable headings and file-path references.
```

## 9. Recommended setup matrix

### A. Fable / Claude independent repository review

```yaml
project: enabled_if_available
model: Fable_5_or_selected_Claude_model
repository_connector: enabled_read_only_or_project_knowledge
research: enabled_or_optional_for_external_facts_only
web_search: optional
skills: none_or_built_in_only
plugins: none
artifacts: allowed_for_long_markdown_output
write_access: disabled_or_not_authorized
mandatory_first_step: access_self_check_with_exact_quotes
fallback: request_manual_input_pack_and_stop
```

### B. Claude prompt-design or project-understanding work

```yaml
project: enabled
repository_connector: enabled_read_only_if_repository_context_needed
research: disabled_unless_current_product_facts_are_needed
skills: none_or_named_only
plugins: none
artifacts: optional
write_access: false
mandatory_first_step: state_authority_and_scope
```

### C. Claude product capability research

```yaml
project: optional
repository_connector: disabled_unless_the_result_must_be_recorded_against_Mnemosyne_state
research: enabled
web_search: enabled
skills: none
plugins: none
artifacts: optional_for_report
write_access: false
mandatory_first_step: cite_current_official_sources
```

### D. Manual input-pack review

```yaml
project: optional
repository_connector: unavailable_or_failed
research: disabled_for_repository_facts
file_upload_or_paste: required
skills: none_or_built_in_only
plugins: none
artifacts: optional
mandatory_first_step: classify_access_mode_as_FILE_UPLOAD_ONLY_and_quote_input_pack
```

### E. Repository writing / Codex-like maintenance

```yaml
ordinary_claude: not_recommended
reason: Mnemosyne writes should remain explicit GitHub/Codex/user-approved tasks with audit records
use_instead:
  - ChatGPT GitHub tool
  - Codex task
  - explicit PR workflow
```

## 10. Standard Claude setup header for future prompts

When sending future Mnemosyne prompts to Claude-series products, prepend a block like this:

```markdown
## Claude setup for this Mnemosyne task

Recommended settings:

```yaml
project: enabled
model: <selected model>
github_connector: enabled_read_only_or_project_knowledge
research: <enabled | disabled | optional>
web_search: <enabled | disabled | optional>
skills: none_or_named_only
plugins: none_unless_explicitly_named
artifacts: allowed_for_long_markdown_output
repository_write_authorized: false
```

First, confirm your actual access mode. If you can read repository files, quote exact snippets from the required files. If you cannot quote exact snippets, do not claim repository access; request a manual input pack and stop.

Repository files are the only trusted persistent source. `current/human-approved-spec.md` is Mnemosyne’s only execution source. Your output is advisory evidence only and does not approve workspace/material/write/build/regression-formalization or execution-source updates.
```

## 11. Fable 5 / cross-model review specific setup

For Fable 5 independent review, use:

```yaml
project: enabled
github_connector: enabled_read_only_or_project_knowledge
research: enabled_for_external_model_or_platform_facts_but_not_repository_truth
skills: none_or_built_in_only
plugins: none
artifacts: allowed_for_markdown_review_result
write_access: false
first_deliverable: project_understanding_and_scope_proposal
```

Require the model to reason about model complementarity:

```text
Most prior Mnemosyne work was produced or reviewed by GPT-series models. Treat those files as evidence to inspect, not truth to accept. Also do not assume GPT-generated work is defective. Evaluate claims by repository evidence, exact quotes, and cross-file consistency.
```

## 12. Storage and ingestion of Claude outputs

First-stage storage for externally produced Claude files:

```text
manual-import-inbox/<review-or-task-id>/
```

Recommended canonical storage after validation for cross-model review results:

```text
notes/cross-model-review-results/<review-id>/
```

Recommended platform-guide storage:

```text
notes/platform-guides/
```

Do not place raw Claude outputs directly into:

- `current/`
- `handoff/`
- `target-projects/`
- `notes/codex-task-results/` as if they were task records
- `raw/research-reports/` unless separately classified as a research input/output

If a Claude output produces valid repair candidates, those candidates remain non-execution-source until user validation and a separately approved task number.

## 13. Known uncertainties / recheck list

Recheck before future use:

- exact Claude plan availability for Research, connectors, skills, plugins, artifacts, and model selection;
- whether a Claude Project's GitHub association is current and can quote exact repository snippets;
- whether the connector is read-only, read-write, or interactive;
- whether Research is using web only, Google Workspace, connectors, or all available sources;
- whether enabled skills/plugins have side effects or tool permissions;
- whether artifacts can be exported cleanly as Markdown for Mnemosyne ingestion;
- whether any connected source contains private/sensitive material unsafe for the current repository visibility.
