# MNE Cross-Repository Safe-Concurrency V2-A A1 — Owner Preparation Decision 001

```yaml
decision_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PREPARATION-OWNER-DECISION-001
task_id: MNEMOSYNE-230
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
cell: A1_positive_independent_pair
decision_status: OWNER_CONFIRMED_PREPARATION_ONLY
exact_run_plan_preparation_authorized: true
Mnemosyne_package_write_and_Ready_PR_authorized: true
A1_execution_authorized: false
validation_repository_write_authorized: false
validation_branch_creation_authorized: false
worker_or_integration_branch_creation_authorized: false
A2_to_A7_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
Meta_Agent_write_authorized: false
real_target_write_or_adoption_authorized: false
external_quota_authorized: false
automatic_retry_or_repair_authorized: false
auto_merge_authorized: false
```

## Owner decision

The Owner selected preparation of an exact V2-A A1 positive-independent-pair run plan after the accepted A0 disposition.

This decision authorizes the current Pro planning route to:

- select an exact public/synthetic fixture and branch topology;
- freeze controller and worker task contracts;
- freeze read, write, generated/derived, shared/global and semantic-effect sets;
- freeze both Alpha→Beta and Beta→Alpha construction checks;
- define exact result paths, evidence levels, stop conditions and retention;
- publish those planning artifacts through one Ready PR to Mnemosyne.

It does not authorize any validation-repository branch, file, commit, PR or test execution.

## Required later gates

Before A1 can run, a separate Owner G2A authorization must bind at least:

- the merged run-decision and source-manifest blobs;
- then-current protected Mnemosyne and Meta-Agent refs;
- the still-valid validation master, fixture, A0 evidence and branch inventory;
- exact visible model labels for the controller, Alpha worker and Beta worker;
- the exact branch and output contract;
- the no-retry and retention terms.

A0 authorization cannot be reused for A1. A merged preparation PR cannot be treated as A1 execution authorization.
