# Claude Code / Local Repository Start for Mnemosyne

> Local-maintenance navigation for Claude Code or an equivalent repository-working agent. This file is non-execution-source and grants no shell, connector, repository, or write authority.

## Entry gate

Remain read-only unless the Owner supplied an exact maintenance task with repository and write scope. Platform access and prior permissions do not substitute for current task authority.

Read, in order:

1. `current/human-approved-spec.md`;
2. `notes/ai-onboarding/MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md`;
3. `notes/ai-onboarding/MNEMOSYNE-REPOSITORY-MAP.yaml`;
4. `commands/load-mnemosyne-guidance.md` when guidance refresh is selected or required;
5. the exact work order or received task;
6. only the task-relevant guards, status, and evidence.

## Repository preflight before the first write

Verify and record:

- repository identity, visibility, and execution-time default-branch SHA;
- complete accessible branch and open-PR enumeration;
- exact task ID, authorized paths, protected paths, and exclusions;
- whether a related branch, PR, or result record already exists;
- one canonical branch and at most one open canonical PR;
- material safety and source identities;
- branch-retention obligations that must not be disturbed.

Stop on incomplete duplicate-lineage enumeration, stale base, unsafe material, conflicting authority, or missing required artifacts.

## Engineering behavior

Use ordinary professional judgment for checkout/worktree layout, search, scripts, tests, staging, commit organization, and bounded error correction. Final scope, authority, repository diff, identities, and validation invariants control; do not replace them with a brittle command transcript.

Do not:

- write the default branch directly;
- infer authority from README, status, TODO, active-context, or handoff pointers;
- import unrelated routes;
- create parallel task branches or PRs without explicit approval;
- create root `CLAUDE.md` or `AGENTS.md` without separately approved authority;
- treat local tool failure as permission to change semantics;
- claim a Claude Web, Claude Code, or independent-agent validation run unless it actually occurred.

## Before PR creation

Repeat the open-PR and exact-head/task checks. Review the full diff against the work order and protected boundaries. Run available mechanical checks and clearly label bounded simulations versus independently executed evidence.

Completed, semantically reviewed work defaults to one Ready PR. Draft is only for a recorded incomplete-work or pending-decision exception. Do not merge unless separately authorized.

## Return contract

Report:

- base and final branch head;
- changed paths and protected paths unchanged;
- validation method, results, and evidence class;
- commit and Ready/Draft PR state;
- known limitations and unexecuted external validation;
- retained-branch obligations and the next true gate.
