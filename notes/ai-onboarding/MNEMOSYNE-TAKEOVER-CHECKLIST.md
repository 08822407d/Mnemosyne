# Mnemosyne Takeover Checklist

> Non-execution-source gate for takeover or continuation. Completing this checklist does not itself authorize work.

- [ ] The Owner explicitly selected takeover or continuation.
- [ ] The exact task, work order, or handoff package path and identity are known.
- [ ] The package was received through the applicable receive workflow when handoff is used.
- [ ] `current/human-approved-spec.md` was read as the only execution source.
- [ ] Required guidance was refreshed as a separate phase without replacing the received task.
- [ ] The exact repository, execution-time default-branch SHA, branches, and open PRs were verified.
- [ ] The local task was restated without importing another route.
- [ ] Authorized actions, changed paths, protected paths, and prohibited actions were restated.
- [ ] Required evidence paths, source identities, and preservation levels were verified.
- [ ] Dynamic repository, platform, model, and product facts were reverified where material.
- [ ] Open questions and recommendations were separated from approved work.
- [ ] Repository-write authority and one canonical branch/PR lineage were confirmed when writing is required.
- [ ] Existing branch-retention obligations were carried forward unchanged unless their release gate was separately verified.
- [ ] External-agent or product-surface validation is labelled actual only when that surface was invoked.
- [ ] The Agent can state `READY`, `BLOCKED`, or `AWAITING_OWNER_DECISION` with evidence.

If no exact task or handoff is selected, return `BLOCKED_NO_EXACT_TASK`, remain in read-only analysis/advice mode, and do not infer a task from `handoff/handoff-current.md`, active context, status files, TODOs, or prior chat memory.
