# Handoff Protocol Repository Audit — Fresh Pro Adjudication 001

```yaml
adjudication_id: MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-PRO-ADJUDICATION-001
source_task: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
source_verdict: REPOSITORY_AUDIT_COMPLETE_READY_FOR_PRO_OWNER_REVIEW
source_outputs:
  complete_response_sha256: 07d6e4f672db63c22b70878690e4068e5865a7dbe7892bf1e07f96080d79ee93
  repository_audit_sha256: 508e903fa5d0685a0d5ad50d0d1183efd8364cb7dc756e3d6a7727fdb8df4fc4
  failure_taxonomy_sha256: 47ae2d61e8d2851c53f4d43cd71ed670b2f5a78adcabac35f525a694f955e268
  validation_design_sha256: a25eabd0064eebadaae0db8a17aa2f958103097ea67e28188aa3c0cacfe96405
  guidance_comparison_sha256: 64007294f86c4a26b7beffc2d2515c24231f16a988fccaa66c73c46c08472c43
  patch_spec_sha256: a843de2c77ae50f416a6d119aa2f550c1a1eb381b3ac10e2d5857b6747e57e9d
formal_disposition: ACCEPT_WITH_THREE_REQUIRED_CORRECTIONS_AND_BOUNDED_ADOPTION_PLAN
repository_writes_performed_by_this_adjudication: false
generic_handoff_commands_modified: false
MNE_HVAL_001_executed: false
```

## 1. Accepted conclusions

The Pro review accepts the following as well-supported within the audit's repository-only scope:

1. The archived F2 startup-drift and source-archive-identity failures are producer/publication-side contract failures; the receiver correctly failed closed in the exercised identity-mismatch case.
2. Handoff 002's package-required report and Rehearsal Contract 001's acceptance field set were mechanically incompatible, and Handoff 003's single-schema repair closes that structural defect on the audited master.
3. The generic prepare/receive/load command layer does not provide the same typed identity/oracle/publication-closure guarantees as the F2 route-specific repair.
4. `handoff/handoff-current.md` is a stale global pointer and should not remain an apparent live route selector.
5. Cross-route root-cause claims remain blocked without exact source/receiver exports for the Owner-reported other handoff.
6. The guidance architecture comparison's strongest immediate option is C (source-selected guidance manifest) while retaining A as the universal trigger/fallback; B2 and E require validation; D should not be the default.

## 2. Required correction 1 — invalid YAML artifact

The required `failure-taxonomy.yaml` source file is not valid YAML. The first parse failure occurs at the unquoted value:

```text
correction_validation_status: designed_and_published_not_behaviorally_exercised (receive_rehearsal_run: false)
```

Additional multi-line sequence strings also require folded-scalar syntax.

Disposition:

```yaml
source_Fable_file:
  preservation: exact_original_retained
  semantic_use: readable_evidence
  machine_parse_status: FAIL
Pro_repaired_derivative:
  filename: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001-failure-taxonomy-yaml-repair-001.yaml
  bytes: 29772
  sha256: e0ae9db3afadebeebb5405467328c2b226ce33f04616020471d006acf5662c33
  yaml_parse: PASS
  failure_case_count: 12
  transformation: syntax_only_quoting_and_folded_scalars
```

This is a required mechanical correction, not grounds to rerun Fable.

## 3. Required correction 2 — validation count and quota inconsistency

The MNE-HVAL-001 scenario table contains **21** scenario IDs:

```yaml
positive: 3
negative: 15
adjudication: 3
total: 21
```

The source summaries incorrectly state 22. The source design's suggested ceiling of 20 fresh receiver conversations cannot execute 21 mandatory fresh-receiver scenarios, before any explicitly authorized invalid-run reissue.

Disposition:

```yaml
corrected_scenario_count: 21
corrected_suggested_receiver_conversation_ceiling: 24
corrected_Pro_turn_ceiling: 6
automatic_retry: false
fresh_reissue:
  allowed_only_after_explicit_Owner_authorization: true
  package_maximum: 2
```

Corrected design:

```yaml
filename: MNE-HVAL-001-PRO-CORRECTED-VALIDATION-DESIGN-001.md
bytes: 15042
sha256: 78419602b6489ced71f165a6991d6873f07dbd5ed914d3a8e12c7f05d10a2142
status: PRO_CORRECTED_DESIGNED_NOT_EXECUTED
```

## 4. Required correction 3 — current Handoff 003 behavioral state

The audit correctly reports that `master@e726dea...` still says:

```yaml
receive_rehearsal_run: false
guidance_loaded_in_receiver: false
```

That is a repository fact, but it is stale relative to this receiving conversation.

Current conversation evidence establishes:

1. the canonical Startup Prompt 003 was used;
2. the receiver emitted the canonical receive-only report and stopped;
3. the Owner sent a separate `加载 Mnemosyne 指导约束` message;
4. the receiver emitted `mnemosyne_guidance_refresh` and preserved the Package 004 readiness task;
5. the Owner later switched the conversation back to Pro and authorized formal continuation.

This is a positive behavioral exercise of receive-state separation, separate guidance loading and task preservation. The exact originating-conversation mechanical-oracle output and complete conversation export are not durably preserved here, so the evidence is not represented as a full archived god-view validation.

```yaml
current_route_behavioral_state:
  receive_only_phase_exercised: true
  separate_guidance_phase_exercised: true
  transferred_task_preserved: true
  substantive_continuation_separately_authorized: true
  originating_oracle_transcript_durably_archived: false
  disposition: POSITIVE_BEHAVIORAL_EXERCISE_WITH_ARCHIVAL_LIMITATION
```

## 5. D1–D5 Pro dispositions

These are engineering dispositions for staged preparation. They do not silently modify active commands or the execution source.

### D1 — guidance architecture

```yaml
A_separate_Owner_message:
  disposition: RETAIN_AS_UNIVERSAL_FALLBACK_AND_CURRENT_DEFAULT
C_source_selected_guidance_manifest:
  disposition: RECOMMEND_FOR_NEXT_ADDITIVE_IMPLEMENTATION
B2_two_phase_startup_with_Owner_acceptance_token:
  disposition: DEFER_UNTIL_MNE_HVAL_001
E_human_gate_only_on_high_impact_triggers:
  disposition: DEFER_UNTIL_TRIGGER_VALIDATION
D_task_local_guidance_bundle:
  disposition: REJECT_AS_DEFAULT
HO_GUIDANCE_001: remains_open
```

### D2 — patch scope

Prepare only the low-risk first stage:

```yaml
selected_for_next_implementation_candidate:
  - P-04_publication_receipt
  - P-05_startup_transfer_fidelity
  - P-06_optional_guidance_manifest_mode_and_task_echo
  - P-09b_deprecate_handoff_current_as_global_route_pointer
deferred_until_validation_or_new_Owner_decision:
  - P-00
  - P-01
  - P-02
  - P-03
  - P-07
  - P-08
  - P-10
  - P-11
  - P-12_execution
```

No command/guard change is authorized merely by this adjudication; prepare a reviewed implementation PR only after the Owner accepts the staged scope.

### D3 — validation

```yaml
corrected_design_publication: recommended
fixture_publication: separately_gated
scenario_execution: separately_gated
quota_authorization: separately_gated
```

### D4 — god-view exports

```yaml
disposition: DEFER
reason:
  - not required to close the current F2 G2A composition defect
  - privacy/public-repository preflight not yet performed
  - cross-route root-cause remains explicitly unknown
```

### D5 — handoff-current

```yaml
disposition: SELECT_P09B_DEPRECATION_BANNER_AS_RECOMMENDATION
reason: removes a stale dual route pointer and makes the Owner startup message the only route selector
```

## 6. Safe continuation

The next bounded repository task should:

- preserve both Fable result sets exactly;
- publish these Pro adjudications and corrected derivatives;
- register `MNE-DR-006 交接加固`;
- update the F2 route status with the positive rehearsal/guidance evidence and the corrected G2A-template gate;
- replace `handoff/handoff-current.md` with a non-route-selecting deprecation banner;
- update the handoff-hardening TODO to R0-audit-complete;
- publish one Ready PR;
- not modify generic commands/guards yet;
- not issue G2A, execute A1 or write the validation repository.

The current GitHub connector exposes read/search/fetch actions only, so this adjudication prepares an exact mechanical write package rather than claiming that a branch or PR was created.
