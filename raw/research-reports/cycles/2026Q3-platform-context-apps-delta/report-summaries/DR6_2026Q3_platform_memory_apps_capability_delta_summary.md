# DR6 — 2026Q3 Platform, Memory, Apps and Capability Delta Summary

```yaml
report_id: RPT-2026Q3-PLATFORM-DELTA-0001
cycle_id: RC-2026Q3-platform-context-apps-delta
report_type: deep_research
source_report: raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md
maintainer_review: raw/research-reports/cycles/2026Q3-platform-context-apps-delta/review-records/MNEMOSYNE-123-DR6-maintainer-evidence-review.md
status: accepted_with_corrections_as_current_supplemental_research_evidence
execution_source: current/human-approved-spec.md
execution_source_status: not_execution_source
```

## Central conclusion

The most important 2026Q3 delta is not “more built-in memory.” It is the need to govern distinct layers separately:

```text
Project / platform context
≠ saved memory
≠ connected-app availability
≠ app authentication
≠ sync/indexing
≠ source-system permission
≠ per-chat invocation
≠ app action approval
≠ repository authorization
≠ current Mnemosyne task authority
```

Mnemosyne's file-backed external-memory principle remains valid, but current platform behavior requires more explicit surface, memory, app, provenance and evidence boundaries.

## High-confidence accepted findings

1. `project-only` memory can be selected only when creating a new Project; existing default-memory Projects cannot be converted in place.
2. Project-only memory blocks references to chats outside the Project, but chats inside the same Project can reference one another.
3. On non-Enterprise plans, default-memory Project chats may reference project and non-project conversations when account memory settings permit.
4. Project instructions are Project-local and override global custom instructions inside the Project.
5. Connected apps can be invoked in Project chats through the tools `+` menu or by name; global connection/authorization remains separate.
6. GitHub repository authorization and sync selection are distinct. Search/index visibility can lag or be incomplete.
7. Standard public GitHub-app documentation describes a read-only code/search integration, while other plugin/app configurations may expose write actions. Operational capability must be checked from the actual action list and approval surface.
8. Deep Research uses only connected-app read actions during research and provides a reviewable plan, progress, citations, source list and export formats.
9. Synced app data may be saved or reused by ChatGPT Memory when Memory is enabled. Disconnecting an app stops future access but does not delete prior conversations that used the data.
10. Visible model and reasoning labels are operator-observed provenance, not a cryptographic or complete runtime model attestation.
11. Search/sync/connector results are relevance-oriented and cannot be assumed to be complete branch/ref/PR enumerations.
12. Mechanical no-write claims need layered evidence. “No write detected” is weaker than “default branch unchanged,” which is weaker than “no branch/PR/object write through all relevant channels.”

## Repository-specific corrections

### Issue mapping correction

The report incorrectly states that GitHub Issue #171 is the target-project-business-conversation guidance-loading question.

Correct mapping:

- Issue #170: long cross-conversation artifacts were not delivered file-first.
- Issue #171: low-risk requested file artifacts were not generated immediately in the same response.
- `current/handoff-guidance-open-question.md` / `HO-GUIDANCE-001`: whether target-project business conversations should also load full, trimmed, or no Mnemosyne guidance after project-local guidance.

Derived views and follow-up planning use this corrected mapping. The original report is preserved unchanged.

### Existing rule coverage

- `current/human-approved-spec.md` §13 already contains a long-transfer file-first principle. Issue #170 is therefore primarily an application/enforcement failure, though the rule can be made more deterministic.
- §18 already separates platform permission from current Mnemosyne task authority.
- §19 already requires mechanical no-write evidence or an explicit run-scoped exception.
- DR6 supports refinements and templates; it does not directly authorize execution-source updates.

## Accepted candidate guidance

- Strict cleanroom tests should use a newly created private Project with `project-only` memory, zero prior chats/files and explicit operator-recorded settings.
- Repository-dependent tests should record global repository authorization, actual surface, per-chat app invocation, sync/index state if known, and available actions.
- Long transfer prompts, handoffs and Codex tasks should default to downloadable files.
- When a user has already requested a low-risk artifact and no separate authorization is legally or operationally required, the artifact should be generated in the same response.
- Target-project business conversations should default to project-local guidance plus a reviewed, trimmed cross-project operator appendix; full Mnemosyne maintenance guidance should not be imported automatically.
- Surface playbooks should distinguish Chat, Project Chat, Deep Research, Work, Agent and Codex.
- No-write evidence should be modeled as levels rather than one binary statement.

## Limitations

- The report handoff says `connected_apps_used: none_in_this_chat_environment`.
- The report's repository read manifest lists only README and Issues #170/#171, although its prose discusses additional repository paths.
- Deep Research citation markers in the Markdown export may not be portable outside the originating conversation.
- Exact Enterprise Compliance API fields, branch/ref completeness guarantees, Project-chat GitHub sync behavior, Library/project-only interactions and model self-observation remain unresolved.
- Cross-platform comparative claims require direct source re-check before operational use.

## Recommended staged follow-up

1. **Work Package C1 — artifact delivery and immediate-generation repair**: resolve Issues #170/#171 with a bounded execution-source/loader/checklist update.
2. **Work Package B1 — provenance and no-write candidate pack**: create non-execution-source templates and taxonomy; do not modify §19 yet.
3. **Work Package D1 — surface playbooks**: one-page operational playbooks for Chat, Project Chat, Deep Research, Work, Agent and Codex.
4. **Work Package A1 — targeted live tests** only for unresolved, decision-relevant boundaries.
5. Consider an observer-assisted no-write proof task only if the combined mechanical gate becomes valuable again.
