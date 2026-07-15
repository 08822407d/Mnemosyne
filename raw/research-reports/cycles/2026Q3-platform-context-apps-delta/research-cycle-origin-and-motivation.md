# RC-2026Q3-platform-context-apps-delta — Research Cycle Origin and Motivation

```yaml
cycle_id: RC-2026Q3-platform-context-apps-delta
status: supplemental_current_evidence_cycle
created_by_task: MNEMOSYNE-123
report_id: RPT-2026Q3-PLATFORM-DELTA-0001
prompt_id: PROMPT-2026Q3-PLATFORM-DELTA-0001
execution_source: current/human-approved-spec.md
execution_source_status: not_execution_source
```

## Why this cycle exists

This cycle refreshes Mnemosyne's platform and workflow evidence after several 2026Q3 product changes and live observations exposed gaps in the 2026Q2 evidence baseline:

- ChatGPT Projects now distinguish `default` and `project-only` memory, with materially different isolation behavior.
- Existing projects cannot be converted in place to `project-only`.
- Connected apps, plugins, sync/indexing, source-system authorization, per-chat invocation, approval policy, and current task authority are distinct layers.
- GitHub repository authorization and sync selection are distinct.
- Deep Research officially limits connected-app use to read actions during research.
- Synced app content may interact with ChatGPT Memory.
- Visible model labels and reasoning controls are insufficient as complete runtime provenance.
- Branch/ref enumeration and connector search results are not guaranteed to be complete mechanical repository snapshots.
- User-observed failures around long transfer artifacts and delayed low-risk artifact generation require evidence-backed workflow repair.

## Inputs

- Prompt original: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/research-prompts/originals/DR6_2026Q3_platform_memory_apps_capability_delta_prompt.md`
- Report original: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md`
- User-provided report received in the post-MNEMOSYNE-122 maintenance conversation.
- Current repository execution source and non-execution-source current/research views.
- Official product and platform documentation reviewed by the report and sampled again during maintainer review.

## Intended use

This cycle is high-weight, time-sensitive research evidence for:

- Project/memory/cleanroom design;
- apps/plugins/GitHub capability and permission terminology;
- surface selection;
- model/tool provenance;
- no-write evidence taxonomy;
- artifact/handoff hygiene;
- future live-test design.

It does not itself:

- modify `current/human-approved-spec.md`;
- approve any execution-source change;
- close Issues #170 or #171;
- resolve `HO-GUIDANCE-001`;
- authorize repository or target-project writes;
- establish permanent platform guarantees.

## Reading order

1. This motivation file.
2. Maintainer review:
   `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/review-records/MNEMOSYNE-123-DR6-maintainer-evidence-review.md`
3. Summary:
   `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/report-summaries/DR6_2026Q3_platform_memory_apps_capability_delta_summary.md`
4. Portable source manifest:
   `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/source-manifest.md`
5. Original report and prompt as needed.

## Freshness boundary

Platform facts are current only as of the report/review date. Any later operational decision that depends on product UI, model availability, plan limits, connected-app actions, or GitHub behavior must re-check current official documentation and visible account configuration.
