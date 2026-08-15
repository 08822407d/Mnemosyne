# Target-Lifecycle V0 Run — Owner Authorization 001

> Durable record of the Owner's explicit authorization of the Pro-recommended V0-only profile. This record authorizes the named synthetic-repository creation and V0 scope, but it does not itself execute V0, authorize V1, modify real targets, or authorize result ingestion into Mnemosyne.

```yaml
authorization_id: MNE-TARGET-LIFECYCLE-V0-RUN-AUTHORIZATION-001
source_decision_candidate: notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001.md
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
run_id: MNE-TARGET-LIFECYCLE-V0-001
owner_decision_status: CONFIRMED
phase_scope: V0_ONLY
repository_or_store: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
material_class: public_synthetic_only
repository_creation_authorized: true
synthetic_repository_write_authorized: true
V0_authorized: true
V1_authorized: false
Mnemosyne_write_during_V0: prohibited
Meta_Agent_write_during_V0: prohibited
real_target_write_during_V0: prohibited
web_or_research: prohibited
Deep_Research_or_Fable: prohibited
external_quota_authorized: false
raw_output_location: 08822407d/mnemosyne-target-lifecycle-validation-002/runs/MNE-TARGET-LIFECYCLE-V0-001/
Mnemosyne_result_ingestion_authorized: false
visible_selection_verbatim: PENDING_EXECUTION_TIME_OPERATOR_RECORD
exact_backend_status: unknown_or_not_attestable
expires_with_run: true
not_future_precedent: true
```

## Owner instruction

The Owner explicitly confirmed the decision candidate and instructed:

> `确认 MNE-TARGET-LIFECYCLE-V0-RUN-DECISION-CANDIDATE-001。`
>
> `授权按推荐方案创建公开合成验证仓库，并且仅运行 V0。`
>
> `不要运行 V1，不要写入 Mnemosyne、Meta-Agent 或真实目标。`

The same message separately authorized one Ready PR for the MNEMOSYNE-211 post-merge closeout and prohibited auto-merge.

## Allowed V0 actions

- recheck that `08822407d/mnemosyne-target-lifecycle-validation-002` does not already exist;
- create that public synthetic-only repository;
- initialize only the frozen V0 sentinel material and `runs/MNE-TARGET-LIFECYCLE-V0-001/` scope;
- read merged Mnemosyne validation-package inputs;
- write only the synthetic repository within V0 scope;
- perform repository/ref/path/diff/schema/hash/identity and no-write checks;
- preserve attempts, failures, incidents and the complete V0 result bundle in the synthetic repository;
- stop after V0 and return for review.

## Prohibited actions

- start V1 or any substantive S1–S11 scenario;
- write to `08822407d/Mnemosyne` as part of V0 execution;
- write to Meta-Agent or any real business/language-learning target;
- use private or real target material;
- use web research, Deep Research, Fable, API budget or other external quota;
- ingest raw V0 results into Mnemosyne;
- modify the candidate, validation design, execution source or any real target;
- treat a V0 pass as architecture acceptance or target adoption.

## Current execution capability status

At authorization-time recheck, the target repository returned GitHub `404 Not Found`, consistent with the intended name being unused.

The currently exposed GitHub connector action set does not provide a repository-creation mutation. Therefore the authorization is valid, but execution is currently blocked before repository creation:

```yaml
execution_block:
  status: BLOCKED_TOOL_CAPABILITY_REPOSITORY_CREATION_UNAVAILABLE
  owner_authorization_missing: false
  repository_name_conflict: false
  validation_started: false
  substitute_store_selected: false
  safe_behavior: do_not_substitute_another_store_or_run_V0
```

A later execution surface that can create the authorized repository may resume from this record. The exact visible model/mode must be copied verbatim at launch before V0 proceeds.
