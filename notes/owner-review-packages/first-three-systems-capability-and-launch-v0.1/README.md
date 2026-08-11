# First Three Systems Capability and Launch Owner Review — Start Here

> Frontier-planned, self-contained owner-review package for a bounded same-conversation next-tier interview. This package is a non-execution-source decision aid. It does not activate Meta-Agent, create target repositories, approve private-material storage, modify any target truth source, launch external research, or authorize repository writes.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
task_id: MNEMOSYNE-201
version: 0.1.0
status: prepared_pending_merge_and_owner_use
repository: 08822407d/Mnemosyne
prepared_from_master: ee3a9fc1acc67e2efd5f7269fd77f097d055a97e
execution_source: current/human-approved-spec.md
execution_disposition: RUN_AFTER_MERGE_IN_SAME_CONVERSATION_WITH_NEXT_TIER_INTERVIEWER
repository_write_during_interview: false
external_research_or_quota_authorized: false
```

## 1. Purpose

The Owner has selected the next step proposed after MNEMOSYNE-200: review the candidate reusable Agent capability catalogue, the first three system selections, target storage/repository choices, and the order of first real use.

The frontier/Pro planning work in this package does four things before handing the interaction to a next-tier model:

1. freezes the decision scope and the facts already established;
2. converts the catalogue and launch questions into contextualized human choices rather than unexplained IDs;
3. supplies a compact question-and-answer reference so the interviewer can answer ordinary doubts without reconstructing the whole repository;
4. defines stop and escalation rules for architecture, authority, privacy, operational activation, and current product facts.

The interview is intended to reduce Pro quota use while preserving decision quality. It is also a bounded practical test of the current `NEXT_TIER_INTERVIEWER` candidate architecture; success or failure should later be recorded as evidence, not assumed in advance.

## 2. What the Owner will decide

The package covers nine decision groups:

1. whether the 42-entry capability catalogue is a usable working inventory;
2. which capabilities should be the shared minimum across all three systems;
3. which additional capabilities Meta-Agent should initially require, trigger, or experiment with;
4. which additional capabilities the work/business-function code-library system should initially require, trigger, or experiment with;
5. which additional capabilities the long-term language teacher/practice Agent should initially require, trigger, or experiment with;
6. whether target work should normally use target-local repositories/stores with bounded meta-system pointers;
7. where code, structured target truth, and complete private conversation/source originals should be stored;
8. which system or combination should enter bounded real use first;
9. which provider/product questions should be deliberately deferred to current-fact verification rather than answered from memory.

The package permits free-form answers, partial approval, rejection of the premise, and deferral. It does not require the Owner to approve every item at once.

## 3. Decisions already fixed and not being reopened here

- `current/human-approved-spec.md` remains Mnemosyne's sole execution source.
- The capability catalogue and all three-system selections are candidates, not active rules.
- Meta-Agent's current target truth remains in `08822407d/Meta-Agent`; it is still inactive for operational use.
- Target creation, operational activation, private-material ingestion, repository writes, and external research remain separately gated.
- Complete material originals should be preserved honestly but normally remain cold/on-demand rather than routine runtime input.
- A target's business truth must not be silently promoted into reusable Mnemosyne capability or Meta-Agent methodology.
- Current provider/model/plan/Skills/product facts must be reverified when they become decision-relevant.
- The paused FCV/Fable/A1/A2/V0–V3 route is unrelated and remains paused.

## 4. Reading order for the next-tier interviewer

Required, in this order:

1. `current/human-approved-spec.md`
2. this `README.md`
3. `01-context-and-fixed-boundaries.md`
4. `02-decision-workbook.md`
5. `03-capability-and-qa-reference.md`
6. `04-next-tier-interviewer-contract.md`
7. `05-answer-ledger-and-result-template.md`
8. `06-source-map-and-on-demand-reading.md`

The interviewer should not load root `README.md`, `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, `current/open-questions.md`, complete historical conversations, full research reports, old handoffs, or task-result archives merely because they exist.

The exact startup message is in `07-same-conversation-startup-message.md`.

## 5. Interview flow

1. Read and validate the required files from execution-time latest `master`.
2. Return a short receive receipt naming the package ID, source commit, loaded paths, excluded cold sources, and write status.
3. Present the concise context summary.
4. Ask `OR-01` first.
5. Ask one decision group or one coherent dependency group at a time.
6. Answer ordinary questions from `03-capability-and-qa-reference.md` and the permitted on-demand sources.
7. After each material answer, restate the interpretation and invite correction.
8. Maintain a visible cumulative answer ledger.
9. Stop and escalate when the contract requires frontier review, current product research, or a new storage/authority analysis.
10. At completion, return a clarification result in chat. Do not write it to GitHub until the Owner separately says to save it and confirms the exact path/scope.

## 6. Why the package is suitable for next-tier interaction

The underlying architecture and option design have already been prepared. The remaining work is mostly:

- explaining frozen concepts;
- collecting Owner preferences;
- recording corrections and deferrals;
- preserving question IDs and dependencies;
- detecting when an answer leaves the bounded scope.

It is not suitable for the interviewer to independently decide:

- Mnemosyne versus Meta-Agent ownership of a future common capability library;
- operational activation of Meta-Agent;
- target truth or authority changes;
- private-data storage approval without Owner choice;
- current Claude/ChatGPT/Fable/Skills capability facts without verification;
- methodology promotion or execution-source modification.

## 7. Completion condition

The owner-review interaction is complete when:

- every `OR-*` question is confirmed, explicitly deferred, rejected, or escalated;
- the visible ledger distinguishes verbatim answers from interviewer interpretations;
- repository/storage and launch-order preferences are recorded with residual uncertainty;
- current product-fact questions are separated from Owner decisions;
- any high-impact item requiring Pro/frontier re-entry is listed;
- no repository or target truth was modified merely by completing the interview.

## 8. Package files

```text
README.md
01-context-and-fixed-boundaries.md
02-decision-workbook.md
03-capability-and-qa-reference.md
04-next-tier-interviewer-contract.md
05-answer-ledger-and-result-template.md
06-source-map-and-on-demand-reading.md
07-same-conversation-startup-message.md
```

## 9. Boundaries

This package does not:

- make candidate catalogue entries approved requirements;
- choose repositories, visibility, products, models, plans, Skills, or quotas;
- start a Meta-Agent pilot or a target pilot;
- authorize private source or personal conversations in Git;
- authorize the next-tier interviewer to write GitHub;
- convert an answer into execution source or target truth automatically;
- require all source files to be loaded during the interview;
- attest the exact hidden backend serving either the planner or interviewer.
