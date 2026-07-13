# Mnemosyne Post-113 Maintenance — New Conversation Startup Prompt

Copy the text below into a new ordinary ChatGPT conversation.

```markdown
Receive Mnemosyne handoff.

Use this authorized handoff package:

- `handoff/mnemosyne-post-113-maintenance-options-handoff-package.md`

This is an explicit handoff receive. It is not merely a request to load behavior guidance.

First read repository evidence:

- `README.md`
- `current/human-approved-spec.md`
- `commands/receive-mnemosyne-handoff.md`
- `handoff/mnemosyne-post-113-maintenance-options-handoff-package.md`
- `current/review-and-validation-status.md`
- `notes/codex-task-results/MNEMOSYNE-113-result.md`
- `notes/chatgpt-work-mode-assessment-2026-07.md`

Then verify:

- PR #160 is merged;
- `current/human-approved-spec.md` is still the sole execution source;
- the handoff package is a non-execution-source transfer artifact;
- the current long conversation remains the receiver/storage finisher for `FABLE5-GREENFIELD-001`;
- this new conversation must not automatically continue the Fable greenfield track;
- the paused post-handoff Meta-Agent route remains paused unless I explicitly choose it.

Your first response must use the receive schema from `commands/receive-mnemosyne-handoff.md` and then present these route choices:

- Route A — post-MNEMOSYNE-113 merge verification and closeout;
- Route B — ordinary Pro comprehensive Mnemosyne health review;
- Route C — explicit resumption of the paused post-handoff Meta-Agent route;
- Route D — bounded ChatGPT Work read-only pilot and policy research;
- Route E — maintenance backlog reprioritization.

For each route, state:

- recommended surface: Chat, ChatGPT Work, or Codex;
- why that surface is appropriate;
- required evidence;
- prohibited actions;
- expected deliverable;
- whether repository writes are needed.

Recommend a route, but do not choose on my behalf.
Do not write repository files before I choose a route.
Do not generate Codex tasks before I choose a route.
Do not modify execution source.
Do not resume or close the paused post-handoff route.
Do not create target workspace/material/write/build/regression artifacts.

ChatGPT Work guidance is candidate guidance only. Do not promote it into `current/human-approved-spec.md` without a later explicit user-approved task after a bounded pilot or further evidence review.
```
