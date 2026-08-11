# Reusable Agent Capability Catalogue — v0.1 to v0.2 Mapping

> Compatibility and review mapping for the owner-reviewed v0.2 candidate. It preserves v0.1 identity and does not update any target capability-selection record automatically.

```yaml
mapping_id: MNEMOSYNE-REUSABLE-AGENT-CAPABILITY-CATALOG-V0_1-TO-V0_2-001
task_id: MNEMOSYNE-202
old_catalogue: notes/reusable-agent-capability-catalog-v0.1.md
old_version: 0.1.0
new_catalogue: notes/reusable-agent-capability-catalog-v0.2.md
new_version: 0.2.0
owner_review_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
automatic_target_migration: false
```

## 1. Mapping classes

- **PRESERVE** — identity and core semantics remain; wording may be clarified.
- **AMEND** — same identity, material scope or behavior clarification added.
- **GENERALIZE** — provider/target-specific wording replaced by portable semantics; adapters move to dated evidence.
- **MERGE_AND_RETIRE** — old entry is absorbed into another ID and remains historical.
- **RENAME_WITH_SEMANTIC_REBALANCE** — same identity, new name corrects emphasis without discarding the core requirement.
- **MATURITY_ONLY** — semantics remain but evidence status is explicitly downgraded/provisional.

## 2. ID mapping

| v0.1 ID | v0.2 disposition | v0.2 ID | Material change |
|---|---|---|---|
| `ACAP-001` | PRESERVE | `ACAP-001` | none |
| `ACAP-002` | AMEND | `ACAP-002` | “single” means one current adopted authority boundary/source set, not one file or newest timestamp. |
| `ACAP-003` | AMEND | `ACAP-003` | role separation should normally appear in human-navigable repository/store organization. |
| `ACAP-004` | AMEND | `ACAP-004` | byte identity, normalization, and substantive-content change are separate dimensions. |
| `ACAP-005` | AMEND | `ACAP-005` | frontier reasoning is required/recommended for material semantic conflict analysis; mechanical checks retain exact duplicates. |
| `ACAP-006` | AMEND | `ACAP-006` | preserve all material external rationale and source paths; runtime reading remains selective. |
| `ACAP-007` | PRESERVE | `ACAP-007` | none |
| `ACAP-008` | PRESERVE | `ACAP-008` | none |
| `ACAP-009` | AMEND | `ACAP-009` | primary rationale is source/evidence role and synthesis into approved control logic; context economy is secondary. |
| `ACAP-010` | AMEND | `ACAP-010` | adds no-specific-rule coverage-gap handling. |
| `ACAP-011` | AMEND | `ACAP-011` | permits explicitly non-authoritative identity-pinned recovery snapshots/backups. |
| `ACAP-012` | MATURITY_ONLY | `ACAP-012` | detailed boundaries marked provisional pending real migrations; evolution emphasized over rollback. |
| `ACAP-013` | MATURITY_ONLY | `ACAP-013` | accepted direction, multi-target evidence still missing. |
| `ACAP-014` | PRESERVE | `ACAP-014` | none |
| `ACAP-015` | PRESERVE | `ACAP-015` | none |
| `ACAP-016` | PRESERVE | `ACAP-016` | none |
| `ACAP-017` | AMEND | `ACAP-017` | adds next-tier → frontier → next-tier staged clarification pattern. |
| `ACAP-018` | PRESERVE | `ACAP-018` | none |
| `ACAP-019` | PRESERVE | `ACAP-019` | OR-01 provides practical interviewer/ledger evidence but not universal validation. |
| `ACAP-020` | AMEND | `ACAP-020` | broadens beyond learning; permits only scoped evidence-calibrated user-state hypotheses. |
| `ACAP-021` | PRESERVE | `ACAP-021` | none |
| `ACAP-022` | AMEND + MATURITY_ONLY | `ACAP-022` | observable triggers and bounded attempt budgets replace reliance on model self-confidence; validation remains open. |
| `ACAP-023` | PRESERVE | `ACAP-023` | none |
| `ACAP-024` | PRESERVE | `ACAP-024` | triggered rather than universal use remains explicit. |
| `ACAP-025` | PRESERVE | `ACAP-025` | none |
| `ACAP-026` | PRESERVE | `ACAP-026` | none |
| `ACAP-027` | AMEND | `ACAP-027` | adds context-sensitive “排版不对” structural repair trigger. |
| `ACAP-028` | GENERALIZE | `ACAP-028` | replaces universal one-report assumption with canonical output / ancillary summary / representation-role separation. |
| `ACAP-029` | PRESERVE | `ACAP-029` | none |
| `ACAP-030` | AMEND | `ACAP-030` | present single-lineage default is not a permanent ban on validated parallel contribution. |
| `ACAP-031` | AMEND | `ACAP-031` | adds periodic stale/zombie retention-obligation audit. |
| `ACAP-032` | PRESERVE | `ACAP-032` | none |
| `ACAP-033` | MATURITY_ONLY | `ACAP-033` | general cross-repository behavior remains provisional beyond migration evidence. |
| `ACAP-034` | MATURITY_ONLY | `ACAP-034` | purpose accepted; practical thresholds and burden need real use. |
| `ACAP-035` | AMEND | `ACAP-035` | becomes the combined promotion gate and portability/generalization filter. |
| `ACAP-036` | MERGE_AND_RETIRE | `ACAP-035` | separate entry retired; ID remains historical and is never reused. |
| `ACAP-037` | PRESERVE | `ACAP-037` | additional uses may emerge from target practice. |
| `ACAP-038` | RENAME_WITH_SEMANTIC_REBALANCE | `ACAP-038` | “Reversible real-use iteration” becomes “Early bounded use with controlled evolution”; rollback is optional, not central. |
| `ACAP-039` | MATURITY_ONLY | `ACAP-039` | no measured automation trigger exists yet. |
| `ACAP-040` | AMEND + MATURITY_ONLY | `ACAP-040` | recognized as a focused design problem requiring research/real use. |
| `ACAP-041` | MATURITY_ONLY | `ACAP-041` | provider-specific Skill semantics remain unverified until current product use. |
| `ACAP-042` | MATURITY_ONLY | `ACAP-042` | direction accepted; population requires current evidence and tests. |

## 3. Target compatibility rule

No target currently has an Owner-approved v0.1 selection record derived from this catalogue. If a future task encounters a v0.1 candidate reference:

1. preserve the old reference as historical evidence;
2. compare the selected IDs through this mapping;
3. require target-local review for amended/generalized/retired entries;
4. map `ACAP-036` to the relevant `ACAP-035` scope rather than copying both;
5. do not adopt v0.2 automatically merely because it is newer.

## 4. Provider-fact separation

`ACAP-028`, `ACAP-040`, `ACAP-041`, and `ACAP-042` require special care:

- portable semantics remain in the reusable catalogue;
- current ChatGPT, Claude, Fable, Skills, export, context, tool, plan, or privacy behavior belongs in dated provider/product evidence;
- user observations may be recorded as observations but do not replace current official verification or bounded behavior tests;
- later product changes update adapters/evidence without silently redefining portable target purpose.

## 5. Validation and rollback/revision

v0.2 remains a candidate. If target selection shows that the merge, renames, or broadened entries make the catalogue less understandable:

- preserve this mapping and evidence;
- issue a later version with explicit split/merge mapping;
- do not rewrite v0.1 or v0.2 history;
- prefer revision/migration to an assumption that rollback is the normal evolution path.
