# Platform, Project Memory, Apps and Surface Delta Status

> Non-execution-source current research/wayfinding view. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
record_type: current_research_delta_status
created_by_task: MNEMOSYNE-123
cycle_id: RC-2026Q3-platform-context-apps-delta
report_id: RPT-2026Q3-PLATFORM-DELTA-0001
status: ingested_with_corrections_as_supplemental_current_evidence
execution_source_modified: false
```

## Current high-signal conclusions

- Strict cleanroom tests should use a newly created private Project with `project-only` memory, zero prior chats/files and explicit operator-recorded configuration.
- Existing default-memory Projects cannot be converted in place to project-only.
- Global app/repository authorization, per-chat invocation, sync/indexing, app action permissions and current task authority are distinct.
- GitHub sync/search is relevance-oriented and cannot be assumed to provide complete branch/ref/PR enumeration.
- Deep Research uses connected-app read actions only during research.
- Synced app data may enter ChatGPT Memory when Memory is enabled; disconnecting the app does not remove prior conversations that used the data.
- Visible model/reasoning labels are provenance fields, not complete runtime attestation.
- No-write claims need layered evidence and should distinguish “not detected,” “default branch unchanged,” “branch/PR unchanged within complete coverage,” and “run surface technically read-only.”
- Long transfer artifacts should be file-first.
- A requested low-risk artifact should be generated in the same response when no additional authorization is actually required.

## Corrected issue/open-question mapping

- Issue #170: long artifact not delivered file-first.
- Issue #171: low-risk requested artifact not generated immediately.
- `HO-GUIDANCE-001`: whether target-project business conversations should load additional full/trimmed/no Mnemosyne guidance.

## Evidence paths

- Original report: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md`
- Summary: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/report-summaries/DR6_2026Q3_platform_memory_apps_capability_delta_summary.md`
- Maintainer review: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/review-records/MNEMOSYNE-123-DR6-maintainer-evidence-review.md`
- Portable source manifest: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/source-manifest.md`

## Next recommended staged work

1. artifact-delivery and direct-generation repair for Issues #170/#171;
2. provenance/no-write candidate template pack;
3. surface playbooks;
4. only then targeted live tests for unresolved product boundaries.

## Boundaries

This view does not modify the execution source, close issues, resolve `HO-GUIDANCE-001`, authorize repository or target-project writes, or turn research recommendations into approved rules.
