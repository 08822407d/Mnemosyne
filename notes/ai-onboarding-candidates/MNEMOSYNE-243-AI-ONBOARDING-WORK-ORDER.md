
# MNEMOSYNE-243 — Add non-execution-source AI onboarding materials

```yaml
task_id: MNEMOSYNE-243
run_after: MNEMOSYNE-242_merged_and_handoff_received
repository: 08822407d/Mnemosyne
task_class: documentation_and_navigation
execution_source_modified: false
active_guards_modified: false
root_CLAUDE_md_created: false
root_AGENTS_md_created: false
```

## Goal

Add a compact repository-native onboarding package so Claude Web/Fable 5, Claude Code and other strong reviewers can understand Mnemosyne quickly, provide grounded analysis, or accept a separately authorized takeover.

Use the candidate package supplied with this work order as a starting point. You may improve wording and repository-map coverage, but preserve the authority model and non-execution-source status.

## Required result

Create:

```text
notes/ai-onboarding/MNEMOSYNE-AI-START-HERE.md
notes/ai-onboarding/MNEMOSYNE-REPOSITORY-MAP.yaml
notes/ai-onboarding/MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md
notes/ai-onboarding/MNEMOSYNE-CURRENT-STATE-INDEX.yaml
notes/ai-onboarding/MNEMOSYNE-CLAUDE-WEB-FAST-CONTEXT.md
notes/ai-onboarding/MNEMOSYNE-CLAUDE-CODE-LOCAL-START.md
notes/ai-onboarding/MNEMOSYNE-TAKEOVER-CHECKLIST.md
notes/ai-onboarding/MNEMOSYNE-AI-ONBOARDING-MANIFEST.yaml
```

Add one concise pointer to `README.md`.

Do not add root `CLAUDE.md` or `AGENTS.md`; the current v0.1 execution source places them in future scope.

## Final invariants

- `current/human-approved-spec.md` remains the only execution source.
- No current status value is duplicated as a second truth source.
- Analysis/advice mode is read-only by default.
- Repository write and takeover require separate explicit authority.
- Cold originals remain on-demand.
- Web and local-agent entrypoints point to the same repository authority map.
- No current task, handoff or route is silently selected.
- The PR is Ready, not Draft, unless a material unresolved design decision remains.
- Do not merge.

## Validation

Run at least three fresh-context simulations:

1. web reviewer asked for a project assessment;
2. local Claude Code agent asked to perform a bounded maintenance task;
3. new agent asked to take over without an explicit task.

Expected behavior:

- reviewer reads only the minimal profile and labels uncertainty;
- local agent requests/uses explicit write authority;
- takeover attempt blocks until exact task/guidance is supplied.

Return the changed paths, validation notes, commit and PR URL.
