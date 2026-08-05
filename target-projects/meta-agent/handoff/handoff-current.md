---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-HANDOFF-001
artifact_role: fresh_session_handoff
status: post_MA_DR_09_repair_PR_pending_human_merge
authority_level: non_execution_navigation
target_runtime_truth_source: false
last_updated_by_task: META-AGENT-PR248-HANDOFF-REPAIR-001
---

# Meta-Agent Handoff Current v0.1

The sole target truth is `target-projects/meta-agent/current/approved-spec.md`; it remains inactive for operational use.

```yaml
route: META_AGENT_PRODUCT_BUILD
repair_task: META-AGENT-PR248-HANDOFF-REPAIR-001
repair_PR: 249
handoff_effective: only_after_PR_249_merge_and_verification
startup_prompt: target-projects/meta-agent/handoff/meta-agent-post-ma-dr-09-next-conversation-startup-prompt.md
compatibility_guard: target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md
```

## Recovery order

1. approved-spec;
2. authority/source map;
3. active-context;
4. Mnemosyne-guidance compatibility guard;
5. methodology and decision/version log;
6. research README, independent-wave adjudication and candidate ledgers;
7. MA-DR-09 identity, formal review, binding addendum and downstream gate;
8. dedicated post-MA-DR-09 handoff package.

## Current research and archive state

- MA-DR-08 and MA-DR-10–15 reports are already exact, adjudicated and safe to archive at the chat-surface level.
- MA-DR-09 may be archived after PR #249 is merged and the canonical transport and handoff paths are verified on `master`.
- Archiving a conversation is an interface-organization action; it must not be treated as deleting the repository evidence.

## Next phase

Candidate specification and minimum offline prototype selection. No prototype, benchmark, Tier-0/1/2 pilot, private material, method promotion, real external write, or activation is authorized.
