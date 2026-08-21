# Mnemosyne AI Start Here

> Repository-native onboarding for AI reviewers and maintenance agents. This file is **non-execution-source navigation**. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

## Purpose and non-purpose

Mnemosyne designs, audits, and delivers external persistent-memory systems for AI agents and projects. Models perform replaceable computation; versioned files provide durable memory and audit evidence.

This package helps a fresh agent find the minimum relevant material. It does **not**:

- select a task, route, handoff, validation, or target project;
- authorize repository or external-system writes;
- replace `commands/load-mnemosyne-guidance.md`;
- make status, handoff, research, result, or raw files execution sources;
- authorize root `CLAUDE.md` or `AGENTS.md`.

## First decision: identify the requested mode

| Mode | Default | Required task authority |
| --- | --- | --- |
| Analysis or advice | Read-only | The user's current question |
| Formal review | Read-only | Exact review package or exact review scope |
| Repository maintenance | No write until authorized | Explicit Owner task with repository/write scope |
| Takeover or continuation | Blocked until selected | Exact Owner-selected task or handoff plus required guidance refresh |

When the request does not clearly select one of these modes, use conservative read-only analysis and state the uncertainty.

## Minimum read order

1. Read `current/human-approved-spec.md`.
2. Read `notes/ai-onboarding/MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md`.
3. Read `notes/ai-onboarding/MNEMOSYNE-REPOSITORY-MAP.yaml`.
4. Read the exact task, handoff, review package, or files named by the Owner.
5. Read only the additional status, guard, command, evidence, or raw files that the selected task requires.
6. Reverify execution-time repository, branch, PR, platform, and model facts whenever they matter.

Do not infer a live task from `README.md`, `current/active-context.md`, `handoff/handoff-current.md`, status files, TODOs, open questions, prior chat memory, or nearby task records.

## Mode-specific additions

### Analysis or advice

Read only the minimum files needed to answer. Keep the operation read-only. Separate verified repository facts, source claims, inference, recommendation, and unknowns.

### Formal review

Add the exact review package and manifest, then follow only its cited evidence paths. Verify artifact identities and freshness. A fluent review, score, PR approval, or merge is evidence—not execution authority or proof of comprehensive human review.

### Repository maintenance

Also read:

- `notes/ai-onboarding/MNEMOSYNE-CLAUDE-CODE-LOCAL-START.md`;
- `commands/load-mnemosyne-guidance.md` when guidance loading is selected or required;
- the task-relevant guards;
- execution-time branch and open-PR state.

Both platform permission and explicit Mnemosyne task authority are required before writing.

### Takeover or continuation

Also read `notes/ai-onboarding/MNEMOSYNE-TAKEOVER-CHECKLIST.md`. Receive an exact package when handoff is used, refresh guidance as a separate phase when required, preserve the transferred task, and continue only after the Owner's explicit continuation gate.

## Cold-source boundary

Complete old conversations, research prompts and reports, historical handoffs, completed-task records, and `raw/` originals are normally `DO_NOT_READ` / `ON_DEMAND`. Read them only for a task-specific reconstruction, dispute, migration, incident, citation, or full-history trigger. State which cold originals were actually read.

## Safe stop rules

Stop or remain read-only when:

- the exact task or package is missing;
- authority, repository, branch, write scope, visibility, or material safety is unknown;
- a required identity, path, or current-state check fails;
- sources conflict in a way that changes a high-impact action;
- a requested external validation surface was not actually invoked.

Never fabricate continuity, external-agent execution, validation evidence, repository state, or permission.
