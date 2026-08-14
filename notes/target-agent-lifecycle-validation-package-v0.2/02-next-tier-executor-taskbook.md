# Next-Tier Executor Taskbook

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
file_role: frozen_execution_procedure
status: prepared_not_executed
```

## 1. Executor contract

The executor performs frozen public/synthetic scenarios. It is not the architecture author or final reviewer.

The executor must:

- use only the exact authorized repository/surface and package version;
- preserve task inputs, outputs, commits, diffs, failures and retries;
- distinguish authority owner from task writer;
- stop when required facts or permissions are missing;
- return semantic ambiguity to Pro/frontier;
- preserve TLR-03/TLR-04 deferrals rather than filling them in.

The executor must not:

- change candidate or validation semantics during the run;
- use real target/private material;
- modify Mnemosyne, Meta-Agent or real business targets;
- infer Owner approval from platform permission;
- create a second branch/PR for one task;
- claim a visible model picker proves backend identity;
- run external research or quota-consuming work unless separately authorized;
- publish run results into Mnemosyne without a later ingestion authorization.

## 2. Required read order

Read only the exact approved versions of:

1. `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md`
2. `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md`
3. package `README.md`
4. `00-run-scope-and-owner-decision.md`
5. `01-synthetic-fixture-and-scenario-contracts.md`
6. `02-next-tier-executor-taskbook.md`
7. `03-mechanical-checks-and-rubric.md`
8. `04-run-manifest-and-result-template.md`
9. the exact Owner run authorization

Do not broad-search Mnemosyne, Meta-Agent, target repositories, historical conversations or unrelated research.

## 3. V0 — Surface, identity and sentinel

### Step V0-1 — Receive

Return:

```yaml
validation_package_receive:
  package_id:
  candidate_id:
  validation_id:
  source_refs:
  required_files_read: []
  missing_files: []
  Owner_authorization_ref:
  phase_scope:
  repository_or_store:
  visibility:
  allowed_writes: []
  prohibited_repositories: []
  material_class:
  product_surface:
  visible_selection_verbatim:
  backend_status: unknown_or_not_attestable
  disposition: PASS | BLOCKED
```

If blocked, perform no write.

### Step V0-2 — Repository and material preflight

Verify:

- selected repository exists or creation is explicitly authorized;
- visibility matches the authorization;
- only public/synthetic material will be used;
- no secrets or credentials are present;
- default branch/base SHA are recorded;
- all accessible open PRs/branches relevant to this run are enumerated as required;
- exact allowed and prohibited repositories are recorded.

### Step V0-3 — Real-repository no-write baseline

Record before-run refs for:

- `08822407d/Mnemosyne`;
- Meta-Agent repository if accessible and named in the authorization;
- each explicitly prohibited real target repository if accessible.

Use mechanically comparable refs/commits. If an inaccessible repository is part of the claimed no-write scope, state the limitation and block any high-confidence no-write claim for it unless the Owner approves a run-scoped alternative.

### Step V0-4 — Sentinel result

No substantive scenario is run in V0.

Return one of:

- `V0_PASS_ELIGIBLE_FOR_SEPARATE_V1_DECISION`
- `V0_BLOCKED_MISSING_AUTHORITY`
- `V0_BLOCKED_MATERIAL_OR_VISIBILITY`
- `V0_BLOCKED_IDENTITY_OR_NO_WRITE_PROOF`
- `V0_PROTOCOL_DEFECT`

If the authorization is `V0_ONLY`, stop after returning the complete V0 bundle.

## 4. V1 — Bounded smoke execution

V1 begins only when explicitly authorized and V0 is valid.

### Step V1-1 — Create/pin fixture

Create the fixture described in `01-synthetic-fixture-and-scenario-contracts.md` in the selected synthetic repository.

Record:

- repository and visibility;
- initial default-branch SHA;
- fixture tree hash/commit;
- material-safety receipt;
- exact scenario set selected by authorization.

### Step V1-2 — Allocate task lineages

For every repository-writing scenario task:

- allocate a distinct task ID;
- perform duplicate-lineage preflight;
- use exactly one canonical branch;
- define the exact write set and dependencies;
- do not open a PR unless the run authorization explicitly requires it;
- never create parallel variants for one task.

### Step V1-3 — Execute in frozen order

Run S1 through S11 in order, subject to scenario dependencies and the Owner-selected scope.

For each scenario:

1. preserve exact input;
2. create a pre-action task contract;
3. state expected write set and authority boundary;
4. execute or block;
5. preserve exact output and changed paths;
6. run required mechanical checks;
7. assign only a provisional scenario disposition;
8. record all missing facts, corrections and retries;
9. do not edit the scenario definition after seeing the result.

### Step V1-4 — Negative and isolation cases

- S8 must use a fresh task/context that has not seen the sufficient Agent-facing migration guide.
- S9 must not be forced into a taxonomy absent from candidate v0.2.
- S1 must not create a substantive parent/meta design brief.
- S10 is exploratory and cannot change the candidate during execution.

### Step V1-5 — Restore test

Run S11 only after the source target state and snapshot identities are pinned. Preserve both successful and failed restore attempts.

### Step V1-6 — Real-repository no-write comparison

Compare after-run refs against the V0 baseline for every repository included in the no-write claim.

A natural-language statement that the executor “did not call a write tool” is not sufficient.

## 5. Scenario dispositions

The executor may assign:

- `SCENARIO_PASS`
- `SCENARIO_PASS_WITH_NONCRITICAL_OBSERVATION`
- `SCENARIO_FAIL_CANDIDATE_OR_SEMANTIC`
- `SCENARIO_FAIL_EXECUTOR`
- `SCENARIO_BLOCKED_MISSING_AUTHORITY_OR_FACT`
- `SCENARIO_INVALID_PROTOCOL_OR_IDENTITY`

The executor must not convert these into global architecture acceptance.

## 6. Retry rules

A retry is permitted only when:

- the prior attempt is preserved;
- the reason is classified as format/transport/executor error rather than hidden semantic repair;
- the same semantic input remains frozen;
- retry count and relation are recorded;
- a critical contamination does not invalidate the new context.

Do not retry by silently revealing expected answers, sufficient migration facts or reviewer conclusions to the worker.

## 7. Stop rules

Stop immediately when:

- authorization or repository identity is missing;
- real/private material is discovered;
- the executor is about to write outside the synthetic allowlist;
- target authority is ambiguous;
- a shared/global conflict has no reconciliation plan;
- output/commit/diff identity cannot be preserved;
- a deferred architecture rule would need to be invented;
- a critical failure contaminates dependent scenarios;
- no mechanically adequate no-write proof can be produced.

## 8. Return bundle

Return the complete bundle defined in `04-run-manifest-and-result-template.md`, including:

- V0 receipt/result;
- V1 run manifest if executed;
- scenario ledger;
- all artifacts and commit identities;
- mechanical checks;
- critical failures and incidents;
- exact no-write proof;
- executor limitations;
- proposed amendments clearly marked as non-adopted;
- one recommended routing disposition for Pro/frontier review.

Do not provide only a short summary or downloadable artifact pointer; the visible final response should contain the complete decision-relevant result, with files as optional supporting copies.
