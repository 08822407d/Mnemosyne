# Mnemosyne Handoff Correctness Validation and Protocol Hardening — Detailed TODO 001

```yaml
todo_id: MNE-HANDOFF-CORRECTNESS-VALIDATION-AND-PROTOCOL-HARDENING-TODO-001
status: todo_after_current_F2_handoff_succeeds
created_by_task: MNEMOSYNE-233
source: direct_Owner_instruction
execution_source: false
priority: high_after_current_route_transfer
current_task_execution_authorized: false
external_review_or_research_authorized: false
```

## Owner requirement

This is a detailed design/validation TODO, not an idea-capture note.

The future task must determine whether Mnemosyne already has a reliable handoff-correctness validation design.

- If no such design exists, create one.
- If one exists, treat the observed incomplete handoffs as falsifying evidence: the design may be unrealistic, defective, insufficiently enforced, or the old conversation may have failed to load/apply the relevant instructions.
- Do not preserve the current design merely because it exists in guidance.

## Evidence that motivates the task

At least the current F2 handoff produced:

1. a user-visible startup message that did not match the canonical repository startup artifact;
2. a merged handoff/package source-identity mismatch that the receiving conversation correctly blocked.

The Owner reports another handoff whose new Pro receiver also reported incomplete transfer. Its exact source/receiver outputs have not yet been ingested into this TODO and must be obtained before cross-route root-cause claims.

## Required “god-view” evidence study

Consider a bounded archival study using exported files for all prior handoff pairs:

- old/source conversation export;
- prepared package and startup artifact;
- new/receiver conversation export through first substantive continuation;
- exact repository identities and PR/merge history;
- any subsequent repair conversation.

Before export or repository storage:

- apply privacy/sensitivity and public-repository safety checks;
- preserve exact bytes when safe and mechanically possible;
- keep cold originals `DO_NOT_READ` / `ON_DEMAND`;
- use compact manifests for ordinary work.

Run independent analyses, subject to separate Owner provider/quota authorization:

- one or more fresh Pro conversations;
- one or more Fable 5 research/review conversations;
- optionally heterogeneous review when the protocol changes authority or trust boundaries.

The analyses must use a true “god-view” package rather than hidden cross-conversation context and must distinguish:
verified facts, package claims, receiver observations, model interpretation and Owner decisions.

## Required target workflow

Design and validate a workflow with these properties:

1. The old conversation switches to Pro before material handoff preparation.
2. It freezes the local task, authority, forbidden actions, evidence paths, guidance requirements and exact startup artifact.
3. It performs final-branch-head and post-merge path/blob closure.
4. A fresh new conversation runs the canonical startup prompt.
5. The new conversation's first receive reply is returned verbatim to the old conversation.
6. The old conversation can decide correctness using a frozen, mechanical acceptance oracle while running a next-tier model.
7. If the oracle cannot decide, at most one Pro turn should identify the main blocker and root-cause class.
8. The old conversation does not retire until receive correctness and task reconstruction are accepted.
9. The new conversation then proceeds under the exact required guidance and task boundaries.
10. The flow must distinguish:
   - package received;
   - identity verified;
   - task reconstructed;
   - guidance loaded;
   - substantive continuation ready.

## Guidance-loading requirement

The Owner requires a future design in which the old conversation determines exactly which project/Agent guidance is needed and the new conversation's startup execution can load those constraints itself at the end when required.

The future design must assess and, if justified, supersede the current fragile pattern that requires the Owner to send a separate follow-up guidance message.

It must preserve:

- visible evidence that guidance was actually loaded;
- task preservation across guidance loading;
- no unrelated route import;
- fail-closed behavior when required guidance is unavailable;
- distinction among Mnemosyne guidance, target-project owner rules and Agent-specific constraints;
- no inference that every handoff always needs Mnemosyne guidance.

Possible designs to evaluate include:

- one startup prompt with two explicit internal phases and two reports;
- a startup prompt that receives, self-verifies, then loads a source-selected guidance manifest;
- a task-local guidance bundle with exact path/blob identities;
- retaining a human gate only for high-impact ambiguity.

## Validation design requirements

The future validation package should include positive, negative and adversarial cases:

- correct package/path/ID/blob;
- wrong package path;
- wrong package ID;
- stale supporting blob;
- normal publication movement of `master`;
- chat-visible prompt drift from canonical startup artifact;
- package received but continuation blocked;
- guidance missing, stale, wrong project or wrong Agent;
- guidance load replaces or contaminates the transferred task;
- receiver silently substitutes a nearby artifact;
- source conversation retires before receive validation;
- next-tier old-conversation adjudication PASS and Pro escalation;
- post-merge change after preparation;
- concurrent writer and open-PR conditions.

Required acceptance criteria should measure:

- exact task reconstruction;
- authority and forbidden-action preservation;
- guidance correctness;
- false PASS / false BLOCK rates;
- number of Owner operations;
- number of Pro turns;
- recovery cost;
- auditability and cold-source burden.

## Expected outputs

The later task should produce, as evidence warrants:

- an inventory of existing handoff designs and gaps;
- a cross-handoff failure taxonomy;
- a validated handoff correctness oracle;
- a final-head/post-merge publication receipt;
- source-generated package/startup/operator-flow artifacts;
- a receiver report schema with separate receive and continuation states;
- a guidance-selection and self-load contract;
- a bounded replay/validation package;
- proposed amendments to `commands/prepare-mnemosyne-handoff.md`,
  `commands/receive-mnemosyne-handoff.md` and related guards;
- migration guidance for existing handoff packages;
- fresh independent review and Owner disposition.

## Boundaries

This TODO does not itself authorize:

- exporting any conversation;
- storing conversation exports in public Git;
- running Pro/Fable/Deep Research;
- modifying handoff commands or the execution source;
- applying the design to a target project;
- automatically loading guidance;
- repository writes beyond the current MNEMOSYNE-233 task.
