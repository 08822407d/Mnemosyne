# Package Integrity Checklist

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
file_role: package_pre_merge_and_pre_run_integrity
status: prepared_not_executed
```

## 1. Required-file inventory

Verify all exist at one pinned commit:

- `README.md`
- `00-run-scope-and-owner-decision.md`
- `01-synthetic-fixture-and-scenario-contracts.md`
- `02-next-tier-executor-taskbook.md`
- `03-mechanical-checks-and-rubric.md`
- `04-run-manifest-and-result-template.md`
- `05-startup-message.md`
- `06-package-integrity-checklist.md`

## 2. Source-reference integrity

Verify every package file points to:

```yaml
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
Owner_result_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001
```

Verify candidate v0.2 and validation v0.2 exist at the same pinned source commit used for execution.

## 3. Semantic integrity

Confirm the package does not contradict these Owner-confirmed boundaries:

- disjoint same-repository tasks may proceed concurrently only with proof;
- shared/global/unknown scope serializes, reconciles or blocks;
- library records its own changes; project Agent migrates on demand;
- human-facing and Agent-facing change documentation are distinct roles;
- no exhaustive consumer index is required by default;
- upstream direction does not create standing downstream write authority;
- change classification remains practical and non-overdesigned;
- no new substantive downstream content in parent/meta repositories;
- TLR-03/TLR-04 deferred details remain explicit;
- validation and target adoption remain separately authorized.

Any contradiction blocks package execution and requires Pro/frontier repair.

## 4. Scenario integrity

Verify:

- S0–S11 are present and uniquely identified;
- S10 is marked exploratory/non-baseline;
- S8 is isolated from the sufficient migration guide;
- S1 prohibits substantive parent/meta content;
- S5 requires Owner-initiated bounded downstream work;
- S7 includes both documentation roles and project-side migration;
- S9 does not require a fine taxonomy;
- S11 uses exact source-identified backup/restore.

## 5. Authorization integrity

Confirm no package file itself authorizes:

- repository creation;
- V0 or V1 execution;
- real-target write;
- private material;
- quota use;
- Deep Research/Fable;
- result ingestion into Mnemosyne;
- candidate adoption;
- PR/merge.

`00-run-scope-and-owner-decision.md` must remain unanswered until the Owner provides a later run-specific decision.

## 6. Material-safety integrity

Verify fixture/scenario files contain only synthetic names, contracts and code descriptions. Confirm absence of:

- credentials/secrets;
- real source code;
- personal/private conversations;
- learner/customer data;
- real target repository content;
- internal provider secrets.

## 7. Mechanical-evidence integrity

Verify the package requires:

- exact refs and hashes;
- one canonical lineage per task;
- declared/actual write-set comparison;
- shared/global/dependency checks beyond path intersection;
- real-repository before/after comparison;
- backup/restore identity comparison;
- preserved retries/incidents.

A package that permits natural-language-only no-write proof fails this checklist.

## 8. Output integrity

Confirm the final result contract requires complete decision-relevant content in the visible final response and does not replace it with only a file/link.

## 9. Pre-run receipt

```yaml
package_integrity_receipt:
  package_commit:
  required_files_present:
  source_refs_match:
  semantic_boundaries_match:
  scenario_inventory_match:
  authorization_remains_ungranted:
  material_safety_pass:
  mechanical_evidence_contract_pass:
  output_contract_pass:
  defects: []
  disposition: PASS | BLOCKED
```

Do not run V0 when disposition is `BLOCKED`.
