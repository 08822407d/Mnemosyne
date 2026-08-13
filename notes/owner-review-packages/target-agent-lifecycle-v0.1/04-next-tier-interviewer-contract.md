# Next-Tier Interviewer Contract

> Contract for conducting TLR-01 through TLR-05 after this package is merged to execution-time latest `master`.

```yaml
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
interviewer_role: bounded_next_tier_owner_review
repository_write_during_interview: false
```

## 1. Required receive sequence

Read from execution-time latest `08822407d/Mnemosyne@master`, in order:

1. `current/human-approved-spec.md`
2. `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md`
3. `notes/first-three-system-capability-selection-v0.3.md`
4. `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md`
5. `notes/target-agent-container-evolution-and-dependency-frontier-adjudication-v0.1.md`
6. `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md`
7. package `README.md`
8. `01-context-and-fixed-boundaries.md`
9. `02-decision-workbook.md`
10. `03-qa-guide.md`
11. `04-next-tier-interviewer-contract.md`
12. `05-answer-ledger-and-result-template.md`
13. `06-source-map-and-on-demand-reading.md`

Do not default-read:

- root `README.md`;
- `commands/load-mnemosyne-guidance.md`;
- `current/active-context.md`, `current/todo.md`, `current/open-questions.md`;
- `handoff/handoff-current.md` or unrelated handoffs;
- full historical conversations or research reports;
- old OR-01/OR-02 interview packages beyond the saved result;
- Meta-Agent repository/history;
- code-library or language-learning target repositories;
- paused FCV/Fable route material.

## 2. Required first response

Return a short `target_lifecycle_owner_review_receive` containing:

- package ID `MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001`;
- execution-time latest master commit;
- read/missing required files;
- confirmation that result 002 and candidate/adjudication identities agree;
- cold materials deliberately not read;
- current execution source;
- no handoff started and no unrelated route imported;
- no GitHub write, target write, activation, private ingestion, validation run, research, product configuration, or quota authorization;
- current question `TLR-01`.

If package identity differs, a required file is missing, latest master makes the package materially stale, or the saved Owner result conflicts with the package, return only:

`TARGET_LIFECYCLE_OWNER_REVIEW_RECEIVE_BLOCKED — <reason>`

Do not reconstruct missing content from chat memory.

## 3. Interview sequence

After receive passes:

1. explain the review goal in short natural Chinese;
2. ask `TLR-01` only;
3. explain the problem, recommendation, main trade-off, smallest implementation, deferral effect, and re-entry boundary;
4. accept free-form answers;
5. after each material answer:
   - restate the Owner answer;
   - separate answer from interviewer interpretation;
   - ask for correction/confirmation;
   - update the visible ledger;
   - proceed only after confirmation or explicit instruction to continue;
6. continue through `TLR-05`.

Do not force the Owner to use option codes. Do not treat a question or request for explanation as a decision.

## 4. Answer sources

Use `03-qa-guide.md` first.

Only if insufficient, use `06-source-map-and-on-demand-reading.md` to read the exact named source and tell the Owner which path was additionally read.

Do not browse the repository broadly or import cold history merely because it exists.

## 5. Status and escalation vocabulary

Use:

- `CONFIRMED`
- `PROVISIONAL`
- `DEFERRED`
- `REJECTED`
- `NOT_APPLICABLE`
- `FRONTIER_REENTRY_REQUIRED`
- `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED`
- `MISSING_ARTIFACT_BLOCKS_DECISION`

Mark:

`FRONTIER_REENTRY_REQUIRED — <question and reason>`

when an answer introduces or changes:

- execution source or target truth authority;
- automatic cross-target propagation;
- shared live runtime/database or competing writer;
- uncontrolled concurrent writes;
- parent repository as live target workspace;
- target operational activation;
- private/trust boundary;
- irreversible/high-cost migration.

Current product facts are not expected in this provider-neutral review. If the Owner asks about current GitHub/ChatGPT/Claude/Fable product behavior, mark `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED` rather than answering from memory.

## 6. Prohibited actions

During the interview, do not:

- create/update files, branches, commits, PRs, issues, repositories, backups, Projects, or Skills;
- modify or activate Meta-Agent;
- write either business target;
- ingest private source, customer material, credentials, or complete personal conversations;
- run the synthetic validation;
- run Deep Research or Fable;
- spend quota;
- claim candidate v0.2 exists;
- treat package choices as target adoption.

## 7. Completion

After TLR-01 through TLR-05:

- produce the complete result using the template;
- summarize the resulting v0.2 direction in natural Chinese;
- list all deferrals, re-entry items, and non-authorizations;
- ask the Owner to correct or confirm;
- wait.

Even after confirmation, do not save the result or create candidate v0.2 until the Owner gives a separate repository-write authorization and scope.
