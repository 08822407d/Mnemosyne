# Mnemosyne Authority and Evidence

> This file is non-execution-source navigation. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

## Authority layers

### 1. Execution source

`current/human-approved-spec.md` defines Mnemosyne's approved global boundaries. No onboarding file, command, guard, task package, status record, handoff, PR, merge, research report, or model memory may silently replace it.

### 2. Current local task selection

A direct current Owner instruction, an exact work order, or an explicitly received handoff package may select a local task within the execution-source boundaries. Nearby files and historical context do not select a task.

A task package may narrow work and prohibit adjacent actions. It does not authorize changes to the execution source unless the Owner separately approves that exact change.

### 3. Behavior and process guidance

Commands and approved guards constrain behavior within their stated scopes. `commands/load-mnemosyne-guidance.md` refreshes applicable constraints while preserving the current task; it does not start a handoff or import a maintenance route.

### 4. Evidence

README, current-status files, active context, handoffs, TODOs, open questions, decisions, task results, reviews, validations, research reports, raw originals, prior chat context, and model memory may support claims. They do not independently authorize action.

## Platform permission versus task authority

Repository or app access is only a technical capability. A write requires both:

1. current platform permission for the exact operation; and
2. explicit current Mnemosyne task authority for the repository, branch, paths, and action.

A persistent app permission, approval card, prior task, branch existence, or open PR is not future-task authority.

## Claim discipline

Use explicit labels when the distinction matters:

- `VERIFIED_REPOSITORY_FACT`
- `DIRECT_OWNER_INSTRUCTION`
- `SOURCE_ARTIFACT_CLAIM`
- `OPERATOR_REPORTED_FACT`
- `MODEL_INFERENCE`
- `DESIGN_RECOMMENDATION`
- `UNKNOWN_REQUIRES_EVIDENCE`

Hashes establish bytes only. PR state establishes repository state only. Approval or merge does not prove correctness, validation success, target adoption, hidden backend identity, or comprehensive human review.

## Conflict and freshness handling

When sources conflict:

1. preserve the conflict;
2. follow the execution source for global authority;
3. follow the exact current Owner instruction for local selection within that boundary;
4. verify execution-time repository and time-sensitive platform facts;
5. stop before a high-impact action when the conflict remains material.

Do not repair a conflict by inventing a missing decision or by choosing the nearest handoff/status file.

## Repository-write preflight

Before writing, establish:

- exact repository and current visibility;
- execution-time default-branch SHA;
- all accessible branches and open PRs needed for duplicate-lineage checks;
- one canonical task branch and at most one open canonical PR;
- authorized changed-path allowlist and protected paths;
- material safety, source identities, and preservation level;
- validation, rollback, Ready-versus-Draft, and branch-retention requirements.

A completed Agent-product change defaults to one Ready PR when semantic review and mechanical checks pass and no material decision remains. Do not merge unless separately authorized.
