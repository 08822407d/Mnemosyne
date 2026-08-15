# Target-Lifecycle V1 Baseline Run — Owner Authorization 001

> Durable record of the Owner's explicit confirmation of `MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001` and authorization for the bounded V1 baseline. This record does not itself start V1. V1 may begin only after the canonical Ready PR containing this record is merged to `master` and execution-time identity verification passes.

```yaml
authorization_id: MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
task_id: MNEMOSYNE-212
owner_decision_status: CONFIRMED
source_decision_candidate: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
confirmed_candidate_blob: 42bb0415243a7ffa7658d57bb6a651c86f5fb991
confirmed_canonical_branch: mnemosyne-212-v0-adjudication-and-v1-plan
confirmed_reviewed_branch_head: f35e1b4c28785dc0dc59273047a06bdf6a049653
source_master_at_confirmation: 930b5ed0c8d1db82e46fd9439035db3f2dd20c46
execution_profile: notes/target-agent-lifecycle-v1-execution-package-001/README.md
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
run_id: MNE-TARGET-LIFECYCLE-V1-001
phase_scope: V1_BASELINE_ONLY
repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
pinned_V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
material_class: public_synthetic_only
selected_scenarios:
  - S1
  - S2
  - S3
  - S4
  - S5
  - S6
  - S7
  - S8
  - S9
  - S11
excluded_scenarios:
  - S10
V1_authorized: true
V1_executed: false
V2_authorized: false
raw_result_ingestion_into_Mnemosyne_authorized: false
architecture_acceptance_authorized: false
target_adoption_authorized: false
external_quota_authorized: false
activation_gate: canonical_Ready_PR_merged_and_execution_time_master_identity_verified
expires_with_run: true
not_future_precedent: true
```

## 1. Owner confirmation

The Owner explicitly confirmed the exact reviewed objects:

```text
canonical branch:
mnemosyne-212-v0-adjudication-and-v1-plan

reviewed head:
f35e1b4c28785dc0dc59273047a06bdf6a049653

V1 decision candidate blob:
42bb0415243a7ffa7658d57bb6a651c86f5fb991
```

The Owner authorized this exact V1 profile and separately authorized one Ready PR to `master`, prohibited Draft status, and prohibited auto-merge.

## 2. Authorized V1 scope

After the activation gate passes, V1 may:

- use only `08822407d/mnemosyne-target-lifecycle-validation-002` for V1 writes;
- pin execution to V0 final head `e8e3296922185b4b70997c2351d6f39423f2cd4f` before the first V1 write;
- execute S1, S2, S3, S4, S5, S6, S7, S8, S9 and S11;
- use the staged three-conversation execution profile;
- create only the execution-profile-named controller, fixture, task and result branches in the synthetic repository;
- preserve exact branch, commit, tree and blob identities plus failed attempts, incidents and retries;
- perform required path/write-set, material-safety, isolation, backup/restore and no-write checks;
- read the exact named real-repository refs only as permitted by the execution profile for no-write proof;
- return the complete bundle for a fresh Pro semantic adjudication.

## 3. Required conversation topology

```text
MNE-DR-003 Execute
  - next-tier model
  - main controller / fixture / Core / S7 / S11 / mechanical closeout

MNE-DR-003 S8
  - separate fresh next-tier conversation
  - S8 only
  - must not have seen S7 sufficient migration documentation or concrete migration facts

MNE-DR-003 Review
  - separate fresh Pro conversation
  - must not have executed a V1 scenario cell
  - semantic adjudication only
```

At each execution conversation launch, record the actual visible model/mode and reasoning setting verbatim. A visible selection does not attest the exact served backend.

## 4. S8 knowledge firewall

S8 must use a new conversation that has not received:

- S7's sufficient Agent-facing migration guide;
- S7 worker output;
- concrete new CommonLib signatures;
- argument replacement values;
- removed configuration keys;
- return-object field details;
- a summary of those hidden migration facts.

If contamination cannot be ruled out, S8 must not run. A contaminated S8 attempt is invalid and cannot be repaired by continuing in the same conversation.

## 5. Prohibited actions

This authorization does **not** permit:

- V1 execution before the canonical Ready PR is merged and latest-`master` identities are verified;
- S10 or V2;
- writes to `08822407d/Mnemosyne` during V1 execution;
- writes to `08822407d/Meta-Agent`;
- access to or writes in unnamed real targets;
- private or real-target material;
- Web research, Deep Research, Fable or other connected apps during V1;
- separate external/API quota spend;
- scenario PR creation;
- modification of candidate v0.2, validation v0.2 or frozen scenario semantics during execution;
- raw V1 result ingestion into Mnemosyne;
- architecture acceptance;
- real-target adoption or migration;
- cleanup/deletion of V1 evidence branches before the required fresh Pro adjudication and evidence-preservation gate.

## 6. Publication and activation semantics

The Owner's confirmation occurred while the exact candidate and execution package existed on the canonical MNEMOSYNE-212 branch. This is valid authority evidence because the authorization binds to the exact reviewed branch head and candidate blob.

However, branch-local authorization is **not** an execution input yet. V1 activation requires all of the following:

1. one canonical Ready PR from `mnemosyne-212-v0-adjudication-and-v1-plan` to `master`;
2. that PR is merged by the Owner;
3. execution-time latest `master` is re-read;
4. the merged candidate, execution package and this authorization record are mechanically matched to the confirmed identities/content lineage;
5. the synthetic repository still has V0 final head `e8e3296922185b4b70997c2351d6f39423f2cd4f` as the required V1 starting point;
6. no conflicting V1 execution has started.

Until all six conditions hold:

```yaml
V1_execution_state: AUTHORIZED_BUT_NOT_ACTIVE_PENDING_PR_MERGE_AND_IDENTITY_VERIFICATION
```

## 7. Owner wording preserved

The controlling Owner message confirmed the candidate and authorized:

- the exact branch/head/blob above;
- saving this authorization record on the same branch;
- one Ready PR to `master`, not Draft and not auto-merged;
- V1 only after that PR is merged and latest-`master` identity verification completes;
- the exact synthetic repository and V0 base;
- S1–S9 and S11, excluding S10/V2;
- the three-conversation execution topology and model-tier roles;
- the S8 knowledge firewall;
- synthetic-repository-only writes;
- no private material, Web/Deep Research/Fable/other apps/external quota;
- no scenario PRs, raw Mnemosyne ingestion, architecture acceptance, target adoption or cleanup authorization.

This record must not broaden that scope.