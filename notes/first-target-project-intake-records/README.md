# First Target Project Intake Records

## Positioning

- Non-execution-source pre-workspace holding area.
- This folder records first-target selection/intake artifacts before an approved target workspace exists.
- It is not Mnemosyne execution source.
- It is not a target workspace.
- It must not contain raw target materials, secrets, credentials, private source, unredacted personal/confidential data, or customer/confidential material.
- Once a target workspace is explicitly approved and created, relevant safe records may be copied/migrated to `target-projects/<target_project_id>/00-project-meta/` or another approved target-local path.
- Storing an intake record here does not authorize real dry-run, target workspace creation, target material ingestion, or target repository write.

## Current records

- `meta-agent/`: Meta-Agent selected for draft manifest preparation only; no workspace created, no target materials ingested, no target repository written.

## Meta-Agent alignment guard

- `meta-agent/meta-agent-analysis-alignment-guard.md` records that Meta-Agent requirements analysis is still pending in an external dialogue.
- Existing Meta-Agent draft run-manifest package is a provisional pre-analysis scaffold.
- Do not use it as completed requirements analysis, approved design specification, operational memory-system build plan, or approved real dry-run manifest.
