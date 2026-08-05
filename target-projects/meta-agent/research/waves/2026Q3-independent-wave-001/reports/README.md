---
artifact_role: exact_research_report_navigation
status: eight_reports_recorded_or_repair_pending
target_project_id: meta-agent
target_truth_source: false
last_updated_by_task: META-AGENT-PR248-HANDOFF-REPAIR-001
repair_PR: PENDING_REPAIR_PR
---

# Independent Research Wave Reports

This directory preserves exact operator-exported report bytes for MA-DR-08, MA-DR-10 through MA-DR-15, including MA-DR-09 after the repair PR is merged.

## MA-DR-08 and MA-DR-10–15

Use the pre-existing `report-parts-manifest.yaml` entries and `identities/*.yaml`. PR #247 verified 56 transport components and reconstruction for seven reports.

## MA-DR-09 canonical transport

The canonical repair transport is:

```text
MA-DR-09 exact UTF-8 bytes
-> bzip2 level 9
-> Base64
-> reports/MA-DR-09-report-bz2-base64/part-001.txt ... part-037.txt
```

Read `identities/MA-DR-09.yaml` for order and hashes. The merged PR #248 path `MA-DR-09-report-parts-base64/` was an incomplete, noncanonical transport and is removed by this repair.

## Authority boundary

Reports are external non-execution evidence. They do not change target truth, methodology, permissions, pilot status, private-material status, or operational activation.
