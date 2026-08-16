# V2 Package Integrity and Non-Execution Checklist

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-INTEGRITY-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
status: design_package_checklist
```

## 1. Required package files

```text
README.md
00-owner-gates-and-stage-boundaries.md
01-synthetic-fixture-and-scenario-contracts.md
02-v2-a-core-concurrency-taskbook.md
03-v2-b-ordered-cross-repository-taskbook.md
04-v2-c-connector-security-design-only.md
05-mechanical-checks-and-evidence-rubric.md
06-run-manifest-and-result-template.md
07-package-integrity-and-non-execution-checklist.md
```

All paths must exist before the package is called complete.

## 2. Source identity checklist

A publication result should record exact blobs for:

- Owner decision result;
- F2 fresh Pro adjudication;
- accepted provisional amendment candidate;
- staged validation design;
- every package file;
- current F2 status;
- task result, verification and finalization records.

## 3. Semantic integrity checklist

Confirm:

- amendment is a bounded extension, not a replacement for candidate v0.2;
- disjoint writes are not described as a sufficient proof;
- freshness checks include read/version identities;
- generated/derived and semantic effects are distinct from paths;
- leases require fencing before adoption;
- automatic compensation is not a default;
- V2-A, V2-B and V2-C have separate gates;
- V2-C remains design-only;
- evidence levels are not mislabeled as SLSA levels;
- no result implies production readiness or target adoption.

## 4. Non-execution checklist

For the design-preparation task, all must remain:

```yaml
synthetic_repository_created: false
validation_repository_written: false
validation_run_started: false
worker_or_controller_launched: false
connector_or_app_enabled: false
account_permissions_changed: false
external_quota_consumed: false
private_or_real_target_material_used: false
Meta_Agent_modified: false
real_target_modified: false
execution_source_modified: false
Target_Lifecycle_candidate_v0_2_modified: false
lock_or_lease_service_created: false
GitHub_Actions_or_merge_queue_configured: false
automatic_compensation_executed: false
```

Any true value invalidates a claim that this task performed design only.

## 5. PR preflight checklist

Before publication:

- read execution-time latest `master`;
- enumerate all accessible open PRs;
- confirm no duplicate MNEMOSYNE-222 branch/PR/result exists;
- compare exact changed paths;
- confirm branch is not behind `master`;
- confirm `current/human-approved-spec.md` is unchanged;
- confirm no Meta-Agent, validation-repository or real-target write;
- confirm package file count and identities;
- create one Ready PR, not Draft, because the design scope is complete;
- do not auto-merge.

## 6. Owner decision after package publication

Package merge does not itself select a run.

A later response must clearly state:

- design package exists;
- V2 execution remains unauthorized;
- the next decision concerns stage/sentinel selection and surfaces;
- V2-C requires a separate connector/security contract;
- no external quota is authorized by package merge.

## 7. Historical integrity

Do not edit:

- the original Fable report;
- visible process output;
- exact 30-file Fable input snapshot;
- V1 raw controller evidence;
- prior fresh Pro and Owner decisions.

Corrections and later decisions use new identified files.
