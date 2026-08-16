# Target-Lifecycle V1 — Owner Architecture Decision 001

> Durable record of the Owner's acceptance of the recovered-and-independently-verified fresh-Pro adjudication for `MNE-TARGET-LIFECYCLE-V1-001`. This decision accepts a provisional global architecture baseline for later target-specific consideration; it does not adopt the architecture into any real target.

```yaml
decision_id: MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001
task_id: MNEMOSYNE-215
decision_status: OWNER_CONFIRMED
source_candidate: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
source_candidate_blob: 1eaeffaf01b3eae878cd0a97cb5d1884b7dba3cc
source_run_id: MNE-TARGET-LIFECYCLE-V1-001
source_adjudication: notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-001.md
source_recovery_incident: notes/provenance-incidents/MNE-TARGET-LIFECYCLE-V1-ADJUDICATION-RECOVERY-001.md
accepted_global_disposition: PASS_WITH_BOUNDED_AMENDMENTS_FOR_OWNER_REVIEW
candidate_global_status: OWNER_ACCEPTED_PROVISIONAL_ARCHITECTURE_BASELINE_FOR_TARGET_SPECIFIC_CONSIDERATION
candidate_revision_required: false
V1_rerun_required: false
target_adoption_authorized: false
production_readiness_proven: false
execution_source_modified: false
```

## 1. Controlling Owner decision

The Owner confirmed:

> 接受 `MNE-TARGET-LIFECYCLE-V1-001` 的 recovered-and-independently-verified fresh Pro adjudication。
>
> 接受全局裁决 `PASS_WITH_BOUNDED_AMENDMENTS_FOR_OWNER_REVIEW`。
>
> 接受 candidate v0.2 作为可供未来各真实目标分别考虑采用的暂定全局架构基线；不将其解释为普遍正确性、production readiness 或任何真实目标已经采用。

The Owner also confirmed all decisions below.

## 2. Accepted architecture status

Candidate v0.2 now has sufficient bounded synthetic support to serve as a **provisional global architecture baseline** when a future real target evaluates whether to adopt, adapt or reject it.

This means future target-specific work may treat the following as the current tested global direction:

- a formal target-owned destination before substantive construction;
- target authority distinct from a bounded task writer;
- conditional same-repository concurrency only for proven disjoint work;
- fail-closed shared/global/unknown scope;
- no automatic upstream-to-downstream propagation;
- library-owned change documentation and project-owned on-demand migration;
- separate human-facing and Agent-facing change roles plus navigation;
- practical route evidence without a forced universal taxonomy;
- non-authoritative, source-identified backup and exact restore semantics;
- separate gates for candidate, validation, global acceptance and per-target adoption.

The decision does not establish universal correctness, quantitative reliability, provider portability or production runtime correctness.

## 3. Rerun decision

```yaml
rerun_decision:
  complete_V1: not_required
  S8: not_required
  S11: not_required
  reason:
    - all_baseline_scenarios_have_decision_relevant_evidence
    - protocol_discrepancy_is_deterministically_classifiable
    - no_contamination_or_candidate_defect_requires_reexecution
    - runtime_evidence_limit_changes_claim_strength_not_architecture_result
```

No rerun is authorized by this decision.

## 4. Required bounded amendments

Before the V1 execution profile is reused:

1. reconcile the fixture branch write allowlist with the required repository-root `README.md`;
2. require explicit test-evidence strength classification instead of treating file presence as execution;
3. preserve the distinction between:
   - `test_artifact_present`;
   - `statically_inspected`;
   - `runtime_executed`;
   - `runtime_passed`.

Before any separately authorized runtime supplement:

4. correct the S6 test's missing import;
5. freeze the exact commit/tree, runtime/toolchain, working directory, command, environment, selected tests, exit code and logs.

The first three are implemented in the MNEMOSYNE-215 follow-up branch for future profile reuse. The synthetic V1 evidence branches are not rewritten.

## 5. Preserved deferrals

The following remain open and are not silently resolved:

- TLR-03 detailed universal change taxonomy and mandatory change-event schema;
- TLR-04 final parent/meta minimum-content rule;
- production-grade concurrency automation;
- final human/Agent documentation serialization and synchronization design;
- optional consumer registration/notification mechanisms;
- real backup providers, accounts, credentials, retention and automation;
- quantitative migration reliability;
- target-specific adoption, migration and activation decisions.

## 6. Evidence-branch retention

All V1 evidence branches in `08822407d/mnemosyne-target-lifecycle-validation-002` remain retained.

```yaml
evidence_branch_decision:
  cleanup_authorized: false
  retain_until:
    - durable_evidence_refs_or_archive_mechanism_is_established
    - unique_branch_evidence_is_verified_preserved
    - Owner_issues_an_explicit_cleanup_release
```

The completed semantic adjudication removes the earlier “pending review” reason for indefinite retention, but it does not itself authorize deletion.

## 7. Still unauthorized

This decision does not authorize:

- adoption, migration or activation in Meta-Agent or any real target;
- automatic propagation into a target;
- runtime supplement or runtime correctness claim;
- S10, V2 or another validation run;
- modification of `current/human-approved-spec.md`;
- raw V1 evidence ingestion into Mnemosyne;
- deletion or rewriting of V1 evidence branches;
- Work pilot, Deep Research, Fable or external quota;
- changes to Meta-Agent, business targets or private material.

## 8. Future target gate

Each real target must receive its own decision package that identifies:

- target-owned authoritative repository/store and target root;
- target-specific differences from candidate v0.2;
- migration and compatibility plan;
- privacy, permissions and material class;
- validation evidence relevant to that target;
- rollback and backup plan;
- exact Owner adoption decision.

Global acceptance is permission to consider the architecture, not permission to deploy it.
