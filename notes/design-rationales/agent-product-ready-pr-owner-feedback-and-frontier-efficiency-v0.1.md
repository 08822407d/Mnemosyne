# Design Rationale — Agent-Product Ready PR, Owner Feedback, and Frontier-Turn Efficiency v0.1

```yaml
rationale_id: MNE-AGENT-PRODUCT-READY-PR-OWNER-FEEDBACK-FRONTIER-EFFICIENCY-001
task_id: MNEMOSYNE-210
status: user_selected_design_formalized
source_incident: PR_277_workflow_and_post_merge_state_failure
source_user_decisions:
  - current_conversation_Owner_challenge_after_TLR_formalization
  - current_conversation_Owner_evidence_on_behavior_feedback_vs_full_PR_review
execution_source_modified: false
```

## Problem

The prior workflow treated a completed Agent-product change as Draft, asked the Owner to review/turn it Ready, omitted the model requirement for that mechanical step, and left stale route state after the Owner merged the PR.

For Mnemosyne-like products, large changes are often natural-language behavior constraints, decision records, memory structures and validation packages. Requiring the Owner to understand every line before every merge is costly and does not reliably predict the combined behavior. By contrast, many user-visible behavior deviations are inexpensive for the Owner to notice during real use and can be reported with concrete context.

The system still needs strong protection against hidden or high-impact failures and must retain the Owner's merge authority.

## Decisive alternatives

### Alternative A — Draft by default plus comprehensive Owner PR review

Rejected because:

- it transfers the Agent's semantic-review burden to the Owner;
- Draft-to-Ready does not prove a review happened;
- large natural-language diffs impose high human cost;
- static reading is often a weak predictor of integrated Agent behavior;
- it creates extra manual and frontier-conversation steps without corresponding evidence.

### Alternative B — Agent self-review plus automatic merge

Rejected because:

- it removes the Owner's explicit authority gate;
- it can conceal scope, privacy, authority or migration errors;
- it weakens rollback and accountability;
- no current instruction authorizes auto-merge.

### Alternative C — Ready PR after Agent/mechanical review, Owner manual merge, real-use feedback and risk-adaptive validation

Selected.

The responsible Agent completes semantic and mechanical review, reports risks/deferrals and recommends a disposition. Completed work is submitted as a Ready PR. The Owner decides whether to merge without being assumed to have reviewed every line. Concrete behavior feedback becomes first-class repair evidence. Hidden/high-impact risks still use proactive checks and explicit gates.

## Why selected

This model minimizes Owner cost while preserving control and improving evidence quality:

- Ready status accurately represents completed work;
- the Agent remains accountable for pre-merge quality assurance;
- the Owner retains merge timing and acceptance authority;
- behavioral failures are captured where they are most observable;
- privacy, authority, data integrity and irreversible changes remain proactively guarded;
- the workflow no longer manufactures a meaningless Draft-to-Ready step as pseudo-review.

## Frontier-turn efficiency choice

A scarce Pro/frontier segment should complete all authorized open-ended synthesis, review and package design before ending. Mechanical PR creation, metadata updates and post-merge checks do not justify continued Pro use, but if the Owner explicitly keeps Pro selected and asks the current Agent to continue, the Agent should complete all authorized work rather than stop after bookkeeping.

The frontier completion check is selected over two alternatives:

- always stop at every authorization boundary without preparing downstream work — rejected as wasteful fragmentation;
- infer all adjacent permissions and continue automatically — rejected because repository, quota, privacy and irreversible-action gates remain real.

## Assumptions

- the responsible Agent can perform meaningful semantic review and disclose uncertainty;
- the Owner can recognize many user-visible behavior deviations during use;
- Git history, result records and rollback remain available;
- separate validation is used when behavior cannot be safely assessed through ordinary use;
- user-observed feedback can be preserved without publishing sensitive material.

## Risks

- the Agent may miss a defect and overstate merge readiness;
- some behavior problems may appear only after long use;
- passive feedback may not reveal privacy, authority or data-integrity failures;
- Ready PRs may be misread as validated or production-ready;
- lower Owner review burden could reduce incidental discovery of documentation errors.

## Controls and falsification

Controls:

- explicit Agent semantic-review and mechanical-check record;
- clear `RECOMMEND_MERGE / REQUEST_CHANGES / BLOCKED` disposition;
- no claim that Ready or merge proves correctness;
- risk-adaptive synthetic validation and isolated trials;
- protected execution-source, privacy, authority and irreversible-action gates;
- post-merge verification and stale-state repair;
- focused behavior-feedback records and regression tests after incidents.

Falsification/revision triggers:

- repeated serious defects passing the Ready gate;
- evidence that Agent self-review is systematically unreliable for a change class;
- hidden-risk incidents not covered by current safeguards;
- Owner feedback that summaries are insufficient for merge decisions;
- evidence that another review workflow materially lowers total Owner cost or risk.

## Affected artifacts

```text
current/agent-product-ready-pr-and-frontier-efficiency-guard.md
current/github-single-active-pr-lineage-guard.md
current/owner-review-branch-ledger-guard.md
commands/load-mnemosyne-guidance.md
notes/chatgpt-github-write-preflight-checklist.md
```

The decision does not modify `current/human-approved-spec.md`, authorize automatic merge, or automatically apply to another target repository.
