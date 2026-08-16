# Checks, Rubric, and Result Template

```yaml
package_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-PACKAGE-001
check_set_id: MNE-RCO-M0-M12-001
semantic_rubric_id: MNE-RCO-R1-R6-001
```

## 1. Mechanical checks

### M0 — package identity

Verify exact blobs for:

- F1 Pro-corrected candidate;
- F1 Owner decision;
- controlling validation design;
- all package files;
- selected future execution profile.

Mismatch blocks before any fixture write.

### M1 — public/synthetic material boundary

Verify that all fixture names, requirements, code, tests and records are invented or public synthetic. Any real/private target material is a critical stop.

### M2 — target-local authority

Verify one exact target-local selection/current record and no competing current truth outside the synthetic target boundary.

### M3 — derived-view non-authority

Verify every impact/index view:

- identifies exact source selection refs;
- states bounded completeness;
- is marked non-authoritative;
- cannot be used as a write source for target truth.

### M4 — no automatic target write

For C2, C3, C4 and C5, compare target state before and after impact/review work. Target changes before an explicit synthetic target-authority decision fail the cell.

### M5 — stable identity and no reuse

Verify:

- every synthetic capability ID is unique;
- retired IDs remain reserved;
- new concepts receive new IDs;
- revisions do not mutate historical identities in place.

### M6 — lifecycle relation consistency

Check directional and reverse relation consistency for:

- supersedes;
- split_from / split_into;
- merged_from / merged_into;
- deprecated / retired status;
- compatibility or affected-selection notes.

Ambiguous or cyclic relations must be reported, not repaired silently.

### M7 — revision and compatibility mapping

Verify that compatible and breaking events are distinguished by declared contract evidence, not by version-number shape alone.

### M8 — stale-view handling

Verify the exact generation inputs of the impact view. If target selection changed or is missing:

- stale status is detected;
- completeness claims are withdrawn;
- target truth is not reconstructed from the view;
- the assessment stops or regenerates from authoritative inputs.

### M9 — declared versus actual write set

Compare the future task contract with actual changed paths. Include checks for:

- controller/output paths;
- target fixture paths;
- package/source paths;
- Mnemosyne, Meta-Agent and any named real target no-write boundary;
- other active route paths.

Different branch names do not substitute for this check.

### M10 — burden evidence

Collect:

- number of required fields;
- fields used by at least one decision/check;
- fields unused;
- duplicated facts;
- number of files/records changed per event;
- human review/explanation burden;
- executor correction count.

Do not invent quantitative thresholds before the first run. Preserve raw counts and reviewer interpretation separately.

### M11 — output identity and failure preservation

Bind every output to exact path/blob/commit identity. Preserve failed output and retry history. A repaired rerun must not overwrite the first failure.

### M12 — protected-repository no-write proof

For each named protected repository, record exact before/after refs when the selected surface can attest them. Scope the claim to named repositories, refs, time window and observed tool surface.

A natural-language self-attestation alone is not a high-confidence no-write proof.

## 2. Semantic rubric

Score each dimension as:

```text
PASS
PASS_WITH_LIMITATIONS
FAIL_CANDIDATE
FAIL_PROTOCOL
FAIL_EXECUTOR
BLOCKED_MISSING_EVIDENCE
NOT_APPLICABLE
```

### R1 — authority fidelity

Does target-local selection remain authoritative while the derived view remains a non-authoritative aid?

### R2 — lifecycle fidelity

Can the model represent revision, compatibility, split, merge, supersession, deprecation and retirement without silent replacement or ID reuse?

### R3 — impact fidelity

Does the affected-target view reflect exact evidence, bounded completeness and staleness rather than overclaiming coverage?

### R4 — no-propagation fidelity

Does upstream change stop at impact/review until target authority acts?

### R5 — usefulness and burden

Do retained fields reduce ambiguity, repeated explanation or migration risk enough to justify their maintenance cost?

### R6 — provenance and recoverability

Can a fresh qualified reviewer reconstruct source event, target selection, derived view, target decision and resulting state from exact identities?

## 3. Critical failures

Any of these blocks a global pass:

- real/private target material used;
- Mnemosyne, Meta-Agent or real target modified outside authorization;
- upstream or derived view writes target truth;
- target authority becomes ambiguous or duplicated;
- stale derived view is trusted over target selection;
- retired ID is reused;
- failed result is overwritten or hidden;
- package identity mismatch is ignored;
- an executor invents a missing Owner/target decision.

## 4. Global dispositions

A fresh Pro adjudicator must choose one:

```text
PASS_FOR_LIMITED_REAL_USE_OBSERVATION
PASS_WITH_BOUNDED_AMENDMENTS_FOR_OWNER_REVIEW
CANDIDATE_DEFECT_REQUIRES_REVISION
VALIDATION_PROTOCOL_DEFECT_REQUIRES_PACKAGE_REVISION
EXECUTOR_FAILURE_RERUN_MAY_BE_AUTHORIZED
BLOCKED_MISSING_AUTHORITY_OR_EVIDENCE
REJECT_AS_DISPROPORTIONATE
```

A cell's correct refusal can be a cell pass. A worker's successful file production is not automatically a candidate pass.

## 5. Result template

```yaml
validation_result:
  validation_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-LIFECYCLE-BOUNDED-VALIDATION-001
  run_id:
  execution_profile_id:
  repository_and_refs:
    synthetic_repository:
    base_commit:
    controller_branch:
    fixture_tree:
  exact_inputs:
    candidate_blob:
    Owner_decision_blob:
    package_blobs: {}
  execution_context:
    product_surface:
    visible_model_or_mode_verbatim:
    reasoning_setting_verbatim:
    backend_status: unknown_or_not_attestable
  cells:
    C1:
      disposition:
      output_refs: []
      critical_failures: []
    C2:
      disposition:
      output_refs: []
      critical_failures: []
    C3:
      disposition:
      output_refs: []
      critical_failures: []
    C4:
      disposition:
      output_refs: []
      critical_failures: []
    C5:
      disposition:
      output_refs: []
      critical_failures: []
    C6:
      disposition:
      burden_metrics: {}
      output_refs: []
      critical_failures: []
  mechanical_checks:
    M0:
    M1:
    M2:
    M3:
    M4:
    M5:
    M6:
    M7:
    M8:
    M9:
    M10:
    M11:
    M12:
  semantic_rubric:
    R1:
    R2:
    R3:
    R4:
    R5:
    R6:
  incidents_and_retries: []
  candidate_defects: []
  validation_protocol_defects: []
  executor_defects: []
  contamination_or_authority_violations: []
  missing_evidence: []
  disproportionate_burden_findings: []
  noncritical_observations: []
  proposed_amendments_not_adopted: []
  no_write_proof:
    named_repositories: []
    limitations: []
  global_disposition:
  real_target_construction_authorized: false
  Meta_Agent_write_authorized: false
  automatic_candidate_update_authorized: false
```

## 6. Reviewer boundary

The final semantic adjudicator must be a fresh Pro/frontier conversation that did not execute the cells. It may inspect exact task outputs and source identities, but it must not modify repositories or silently amend the candidate during adjudication.
