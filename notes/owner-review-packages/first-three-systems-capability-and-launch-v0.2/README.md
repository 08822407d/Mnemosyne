# First Three Systems Capability and Launch Owner Review v0.2 — Start Here

> Pro/frontier-prepared, self-contained package for a bounded same-conversation next-tier interview covering `OR-02` through `OR-09`. It incorporates the completed `OR-01` human review and the owner-reviewed capability catalogue v0.2. This package is a non-execution-source decision aid. It does not activate Meta-Agent, create target repositories, approve private-material storage, modify target truth, launch external research, or authorize repository writes during the interview.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
task_id: MNEMOSYNE-204
version: 0.2.0
status: prepared_pending_merge_and_owner_use
repository: 08822407d/Mnemosyne
prepared_from_master: 91efad2f2a2f22e99223c49460d27bd9fcbfdb68
execution_source: current/human-approved-spec.md
prerequisite_owner_result: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
catalogue: notes/reusable-agent-capability-catalog-v0.2.md
selection_candidate: notes/first-three-system-capability-selection-v0.2.md
question_range:
  - OR-02
  - OR-03
  - OR-04
  - OR-05
  - OR-06
  - OR-07
  - OR-08
  - OR-09
execution_disposition: RUN_AFTER_MERGE_IN_SAME_CONVERSATION_WITH_NEXT_TIER_INTERVIEWER
repository_write_during_interview: false
external_research_or_quota_authorized: false
```

## 1. Purpose

`OR-01` is complete. The Owner accepted the reusable Agent capability catalogue as a working inventory, reviewed all 42 v0.1 entries, amended their meaning, retired the duplicated `ACAP-036`, and produced a 41-entry active v0.2 catalogue. The remaining work is not another catalogue-wide review.

This package helps the Owner decide:

1. which already-reviewed capabilities form the compact shared floor for the first three systems;
2. which additional capabilities Meta-Agent should require, trigger, experiment with, or defer;
3. which additional capabilities the work/business-function code-library system should use;
4. which additional capabilities the long-term language teacher/practice Agent should use;
5. whether target-local truth and bounded meta-system pointers should be the default repository/store model;
6. where structured target truth, work code, complete private conversations, and non-authoritative backups should live;
7. the preparation and bounded-real-use order for the three systems;
8. which provider/model/product/Skills facts must be verified later rather than guessed now.

The package also supplies the detailed **answer guide requested by the Owner**. The next-tier interviewer should be able to explain every checklist item, why it is present, what omitting it changes, how it can be implemented compactly, and when the question must return to Pro/frontier or current product verification.

## 2. Decisions already fixed

The interview must not reopen these merely because another option looks attractive:

- `current/human-approved-spec.md` remains Mnemosyne's sole execution source.
- `OR-01` accepted the catalogue approach and its v0.2 amendments; the 41 active entries are not being re-reviewed from zero.
- Catalogue entries are portable capability candidates, not target runtime instructions or provider implementations.
- A target selects a minimum sufficient subset; it does not copy the entire catalogue into runtime context.
- Meta-Agent's sole target-truth path remains `08822407d/Meta-Agent@master:current/approved-spec.md`; it remains inactive for operational use.
- Meta-Agent activation, private-material ingestion, target creation, target writes, and product selection remain separately gated.
- Complete originals should be preserved honestly but normally remain cold/on-demand.
- Project business truth must not silently become common Mnemosyne capability or Meta-Agent methodology.
- Product/model/plan/Skills/settings/connector facts are time-sensitive and require current verification when decision-relevant.
- The paused FCV/Fable/A1/A2/V0–V3 route is unrelated and remains paused.

## 3. Review style selected by the Owner

The Owner's successful `OR-01` interaction established these preferences for this package:

- present manageable checklists in natural Chinese;
- explain each item or group before asking for a choice;
- allow item-by-item review when the Owner requests it;
- answer doubts before recording a final interpretation;
- preserve provisional answers, corrections, deferrals, and unresolved questions;
- do not force a one-message answer to every item;
- use a visible concise answer ledger;
- route high-impact architecture, authority, privacy, activation, or migration decisions back to Pro/frontier;
- do not answer current product facts from memory.

The interviewer should normally ask one coherent sub-group at a time. For `OR-02` through `OR-05`, the Owner may request the same item-by-item style used in `OR-01`; the package is designed to support that without another Pro planning turn.

## 4. Required reading order

Read from execution-time latest `08822407d/Mnemosyne@master` in this order:

1. `current/human-approved-spec.md`
2. this `README.md`
3. `01-context-and-fixed-boundaries.md`
4. `02-decision-workbook.md`
5. `03-capability-selection-and-qa-guide.md`
6. `04-next-tier-interviewer-contract.md`
7. `05-answer-ledger-and-result-template.md`
8. `06-source-map-and-on-demand-reading.md`

The interviewer does not need to run the full Mnemosyne guidance loader solely for this frozen interview. If the interaction changes into repository writing, external research, target creation, Meta-Agent activation, private-material intake, or another task class, it must stop and load the then-applicable latest guidance before acting.

The exact startup message is stored in `07-same-conversation-startup-message.md`.

## 5. Interview flow

1. Validate the package identity and all required files against execution-time latest `master`.
2. Return `owner_review_receive_v2` naming package ID, source commit, loaded paths, excluded cold sources, and no-write/no-run status.
3. State that `OR-01` is complete and begin with `OR-02`.
4. Ask one capability group, target-specific group, or tightly coupled decision at a time.
5. Use `03-capability-selection-and-qa-guide.md` as the primary answer source.
6. Read an on-demand source only if the guide is insufficient; disclose the exact extra path read.
7. After each material answer, restate the interpretation, invite correction, and update the visible ledger.
8. Do not treat silence as confirmation.
9. At `OR-06` through `OR-08`, capture Owner preferences but escalate any new architecture, truth, authority, privacy, activation, or irreversible migration choice.
10. At `OR-09`, separate the Owner's desired outcomes from current product facts requiring verification.
11. Return a complete clarification result in chat after `OR-02` through `OR-09` are confirmed, deferred, rejected, or escalated.
12. Do not write the result to GitHub until the Owner separately reviews the summary and authorizes exact save scope.

## 6. Why this package is suitable for a next-tier model

The Pro/frontier segment has already:

- incorporated the full 42-item Owner review;
- created the v0.2 capability catalogue and target-selection candidate;
- separated stable semantics, triggered modules, experiments, target-specific objects, and product facts;
- defined the repository/store and minimum-launch candidates;
- frozen question meanings, recommendations, dependencies, stop conditions, and escalation routes;
- prepared a detailed explanation and Q&A guide.

The remaining interaction is mainly bounded explanation, item-level clarification, answer capture, and semantic escalation. The next-tier interviewer does not receive authority to finalize architecture or operate the systems.

## 7. Completion condition

The review is complete when:

- `OR-02` through `OR-09` each have `CONFIRMED`, `PROVISIONAL`, `DEFERRED`, `REJECTED`, `NOT_APPLICABLE`, or an explicit escalation status;
- capability choices distinguish required, triggered, experimental, deferred, rejected, and target-specific objects;
- storage preferences distinguish structured truth, private originals, source code, and non-authoritative backups;
- launch ordering distinguishes preparation from operational activation or pilot execution;
- product-fact questions are listed separately from Owner preferences;
- the answer ledger preserves corrections and residual uncertainty;
- no repository, target truth, Meta-Agent, product configuration, research run, or private archive was changed merely by completing the interview.

The interaction may finish as `PARTIAL_WITH_DEFERRALS`; false certainty is not required.

## 8. Package files

```text
README.md
01-context-and-fixed-boundaries.md
02-decision-workbook.md
03-capability-selection-and-qa-guide.md
04-next-tier-interviewer-contract.md
05-answer-ledger-and-result-template.md
06-source-map-and-on-demand-reading.md
07-same-conversation-startup-message.md
```

## 9. Boundaries

This package does not:

- approve the shared floor or any target-specific selection;
- modify catalogue v0.2 or the v0.2 planner selection;
- choose repository names, visibility, cloud/local storage, provider, model, plan, Skill, setting, or quota;
- create or activate any system;
- authorize private source, customer data, credentials, or complete personal conversations in Git or another service;
- authorize the next-tier interviewer to write GitHub;
- convert an interview answer directly into execution source or target truth;
- require reading complete historical conversations, full research reports, old handoffs, or unrelated task archives;
- attest the hidden backend serving either the Pro planner or next-tier interviewer.
