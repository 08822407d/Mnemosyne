# Startup Prompt — Receive Non-FABLE Comprehensive Health Review Handoff

Receive Mnemosyne handoff.

Use this authorized repository-backed handoff package:

`handoff/mnemosyne-non-fable-comprehensive-health-review-handoff-package.md`

Package ID:

`MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-HANDOFF-001`

## Required first operation

1. Read `commands/receive-mnemosyne-handoff.md`.
2. Read the authorized package.
3. Read only the minimum evidence paths needed to verify the receive report.
4. Output the required `mnemosyne_handoff_receive` YAML report.
5. Stop after the receive report.

Do **not** load Mnemosyne guidance in the same operation. I will send:

`加载 MNEMOSYNE 约束指导`

as a separate next message.

## Receiver guidance sequence

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - continue_received_task_under_refreshed_constraints
```

## Transferred local task

After the separate guidance refresh, perform:

`MNEMOSYNE-NON-FABLE-COMPREHENSIVE-HEALTH-REVIEW-001`

This is a bounded, read-only comprehensive health review of current Mnemosyne maintenance state.

Required boundaries:

- treat `current/human-approved-spec.md` as the only execution source;
- preserve the transferred local task through guidance refresh;
- use GitHub read-only access during the review;
- do not modify files, branches, commits, PRs, Issues, comments, labels, workflows, automation, or repository settings;
- do not create target workspaces, ingest target materials, access/write target repositories, build Meta-Agent, execute observer-assisted proof, approve a no-write exception, or promote regressions;
- exclude all FABLE5 review, independent design, Greenfield, comparison, task generation, and result-storage work;
- do not rerun completed Meta-Agent or artifact-delivery behavioral campaigns;
- verify current `master` against the package snapshot before substantive conclusions.

The package defines the full review scope, minimum evidence set, required deliverable, exclusions, and stop conditions.

For the final review result, generate a verified local Markdown file named:

`mnemosyne-non-fable-comprehensive-health-review.md`

when file tooling is available. Keep the chat response concise and do not duplicate the entire long report inline.

## Stop condition for this first message

Do not begin the health review yet. Complete only the handoff receive report and stop.