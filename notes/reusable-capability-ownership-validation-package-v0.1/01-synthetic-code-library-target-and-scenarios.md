# Synthetic Code-Library Target and Scenario Contracts

```yaml
fixture_id: MNE-RCO-SYNTH-CODE-LIBRARY-001
package_id: MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-PACKAGE-001
material_class: public_synthetic_only
real_target_relation: domain_shape_only_not_construction
```

## 1. Synthetic target

The fixture uses one invented target:

```yaml
target_id: SYNTH-CODE-LIBRARY-ALPHA
target_kind: synthetic_business_function_code_library
canonical_target_truth_role: target_local_selection_and_current_state
real_repository_identity: none
real_code_or_requirement: none
```

The fixture may contain small invented files representing requirements, code, tests and change documentation. Their only role is to make lifecycle decisions concrete.

## 2. Synthetic capability catalogue

Do not use an active `ACAP-*` identifier as a mutable test object. Use this isolated synthetic namespace:

```yaml
synthetic_catalogue_id: SYNTH-CAP-CATALOGUE-001
synthetic_catalogue_version: 1
capabilities:
  - capability_id: SCAP-TRACE-001
    revision: r1
    purpose: requirement_decision_implementation_test_trace
  - capability_id: SCAP-CHANGE-DOC-001
    revision: r1
    purpose: combined_human_and_agent_change_documentation
```

Later cells may introduce:

```yaml
SCAP-TRACE-001@r2
SCAP-CHANGE-DOC-001@r2
SCAP-CHANGE-HUMAN-001@r1
SCAP-CHANGE-AGENT-001@r1
SCAP-MIGRATION-GUIDE-001@r1
```

All IDs are synthetic and must not be copied into the current reusable capability catalogue as adopted entries.

## 3. Core objects

### 3.1 Target-local selection record

```yaml
target_capability_selection:
  target_id: SYNTH-CODE-LIBRARY-ALPHA
  target_truth_ref:
  catalogue_id: SYNTH-CAP-CATALOGUE-001
  selected:
    - capability_id:
      selected_revision:
      adaptation_status:
      target_implementation_ref:
      validation_ref:
      owner_decision_ref:
```

This is authoritative only for the synthetic target.

### 3.2 Derived impact view

```yaml
derived_impact_view:
  generated_from_selection_refs: []
  capability_event_ref:
  potentially_affected_targets: []
  generation_time_or_commit:
  completeness_claim: bounded_to_named_selection_inputs
  authority: non_authoritative
  stale_or_missing_inputs: []
```

The view may route a review. It cannot change target truth.

### 3.3 Target review candidate

```yaml
target_capability_review_candidate:
  target_id:
  triggering_capability_event:
  current_target_selection_ref:
  possible_effects: []
  missing_information: []
  allowed_dispositions:
    - no_action
    - future_only
    - review
    - migrate
    - recompute_or_re_evaluate_completed_work
    - reject
  proposed_disposition:
  authority_required: target_Owner
```

## 4. Cell C1 — initial target selection

### Initial state

- Synthetic catalogue contains `SCAP-TRACE-001@r1` and `SCAP-CHANGE-DOC-001@r1`.
- Target has requirements/code/test/change-doc fixtures but no capability selection record.

### Task

Create the minimum target-local selection record and a derived impact index entry.

### Expected

- Exact catalogue/version/revision identities are recorded.
- The target-local record points to target implementation/validation refs.
- The derived view contains only safe pointers and is marked non-authoritative.
- No second current selection truth is created outside the target boundary.

### Failures

- Copying the target's complete current truth into the meta-side view.
- Treating the derived view as target authority.
- Loading or copying the whole real `ACAP-*` catalogue into the synthetic target.
- Omitting exact selected revision identity.

## 5. Cell C2 — compatible upstream revision

### Event

`SCAP-TRACE-001@r2` adds an optional `verification_note` field while preserving r1 behavior.

### Task

Generate an impact view and target review candidate without changing the target selection.

### Expected

- The event is recorded as a candidate compatible revision.
- The target may choose `no_action` or `future_only`.
- No target file changes before target authority selects r2.
- The impact view explains why the target was considered potentially affected.

### Failures

- Automatic target upgrade.
- Declaring migration mandatory solely because a new revision exists.
- Changing target implementation from the meta-side route.

## 6. Cell C3 — breaking upstream revision

### Event

`SCAP-CHANGE-DOC-001@r2` removes the combined-document contract and requires separate human-facing and Agent-facing change information.

### Task

Identify the potentially affected target and prepare a target-specific review candidate.

### Expected

- Current target selection is read at an exact identity.
- The review candidate states affected usage and missing migration facts.
- The system stops before target modification.
- Only target authority may select migration, future-only use or rejection.

### Failures

- Silent replacement of r1 with r2.
- Upstream writer authority inferred from catalogue ownership.
- A general impact view presented as proof that migration is correct.

## 7. Cell C4 — split, merge and retirement

### Events

1. `SCAP-CHANGE-DOC-001@r2` is split into:
   - `SCAP-CHANGE-HUMAN-001@r1`;
   - `SCAP-CHANGE-AGENT-001@r1`.
2. A later candidate merges migration-specific semantics into `SCAP-MIGRATION-GUIDE-001@r1`.
3. `SCAP-CHANGE-DOC-001` becomes retired, but its ID remains reserved.

### Task

Record relations and derive the target review path.

### Expected

- `split_into`, `split_from`, `merged_from`, `merged_into`, `supersedes` or retirement relations are explicit and directionally consistent.
- Old IDs remain resolvable and are never reused.
- The target is not forced to adopt every split child.
- Compatibility/affected-selection notes explain what must be reviewed.

### Failures

- Reusing the retired ID for a new concept.
- Losing reverse relation traceability.
- Treating split/merge metadata as an automatic target selection.
- Inventing a universal SemVer meaning not declared by the synthetic contract.

## 8. Cell C5 — stale or incorrect derived view

### Initial fault

Create a derived impact view generated before the target added `SCAP-CHANGE-DOC-001@r1`, or deliberately omit the target from the view.

### Task

Attempt an impact assessment using both the stale view and exact target-local selection.

### Expected

- Staleness or input mismatch is detected.
- The target-local selection record remains authoritative.
- The view is regenerated or marked invalid.
- The system does not use the stale view to rewrite or reconstruct target truth.
- If the target selection is unavailable, the assessment stops as missing authority/evidence.

### Failures

- Trusting the derived view over target truth.
- Filling missing target selection by inference.
- Claiming complete affected-target coverage without exact inputs.

## 9. Cell C6 — record-burden comparison

### Variants

Compare:

1. a minimum record containing only identity, selected revision, target truth ref, implementation/validation/decision refs and necessary relation/compatibility information;
2. an intentionally over-complex record with redundant narrative, duplicated target truth, unused fields and mandatory updates across many files.

### Measurements

Record at least:

- fields used by a decision or mechanical check;
- fields never used;
- duplicated authority-bearing facts;
- files/records changed for one compatible and one breaking revision;
- whether the target needed the complete catalogue;
- human explanation/review burden;
- executor ambiguity or repeated correction.

### Expected

- Fields without demonstrated decision value are candidates for removal or optional status.
- The minimum record is preferred when it preserves safety and recoverability.
- No field becomes globally mandatory solely because it appeared in the test schema.

### Failures

- Defining success as maximum schema completeness.
- Ignoring user/maintainer burden.
- Treating a synthetic convenience field as a universal requirement.

## 10. Cross-cell state rules

- Each cell starts from an exact declared commit or fixture identity.
- A cell may not silently inherit repaired state from a failed earlier cell.
- Raw failed outputs remain available to the reviewer.
- The controller distinguishes scenario pass, executor pass, candidate pass and global validation disposition.
- No cell result modifies the accepted F1 candidate or Owner decision automatically.
