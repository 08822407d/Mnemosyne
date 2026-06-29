# DR4 User Originals / Requirements / Redaction Governance Summary

- report_id: RPT-2026Q2-UIG-0001
- cycle_id: RC-2026Q2-user-input-governance
- source_report: `raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md`
- execution_source_status: not_execution_source

## 1. Executive summary

DR4 recommends a conservative v0.1 governance pattern: original layer outside Git; approved/control layer inside Git. User originals, raw requirements, sensitive project/customer material, secrets, private source, and unredacted personal/confidential data should default outside the repository. In-repository material should be limited to safe, reviewed, and approved artifacts such as decisions, redacted excerpts, synthetic substitutes, and non-secret external pointers/manifests.

## 2. Core governance model

The report separates original evidence, explanatory restatements, user-approved decisions, disclosure-safe variants, and provenance/pointer metadata. AI or human restatements can help explain and organize material, but they are not original requirements and do not become an approved baseline without a user decision.

## 3. Storage decision matrix summary

Public or visibility-unverified repositories should store only public, synthetic, or explicitly redacted material. Verified private repositories may support a broader working set, but private visibility does not automatically authorize raw originals because Git history, clones, forks, PR references, and later visibility changes can preserve exposure.

## 4. Authority model

Original external sources hold evidentiary authority outside Git. User-approved decisions hold the highest in-repository target authority within their approved scope. Restatements hold explanatory authority only. Redacted excerpts and synthetic substitutes support disclosure or test/design work. External pointers provide provenance without storing unsafe content.

## 5. Repository visibility / Git history implications

Visibility-unverified or possibly-changing visibility should be treated as public-equivalent / public-risk for storage decisions. Moving, deleting, or reverting a file does not erase prior Git history exposure. Private repo status reduces access for current readers but does not remove history or future visibility-switch risk.

## 6. Redaction and synthetic substitute policy

Redacted excerpts require a documented review method, removed-category list, reviewer/approval record, and residual-risk statement. Synthetic substitutes must be clearly labeled and should not be reversible to confidential originals. Both are eligible in Git only when safe and approved for the repository visibility.

## 7. External pointer policy

External pointers should identify source ownership, location type, access status, authority level, sensitivity, allowed use, and why the original is not stored in Git. Pointers must not themselves contain secrets, credentials, personal/confidential details, or sensitive precise locations.

## 8. Candidate Mnemosyne v0.1 implications

Before real target material intake, Mnemosyne should have a per-target storage policy, redaction manifest schema, external pointer schema, and leak/mistaken-storage response. Target-scoped safe inputs should use `target-projects/<target_project_id>/01-user-input/`, with `originals/` containing pointers/README by default rather than raw originals.

## 9. Known limits and open questions

DR4 is research evidence only, not execution source. OP-08 remains open for broader privacy/redaction/access-control governance. Per-target policy still requires user approval, including repository visibility assessment, approved storage scope, redaction/pointer approach, and no-target-write/run-manifest gates.
