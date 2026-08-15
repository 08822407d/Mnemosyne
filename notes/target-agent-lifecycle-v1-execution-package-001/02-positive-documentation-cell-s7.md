# V1 Positive Documentation Cell — S7

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
cell_id: TLR-V1-CELL-S7-001
status: prepared_not_executed
selected_scenario: S7
```

## 1. Cell purpose

This cell tests the positive TLR-02 path:

1. CommonLib Agent records its own v1→v2 contract change in forms suitable for humans and downstream project Agents.
2. The documentation overview tells a consuming Agent which non-code documents exist, where they are and when to read them.
3. Agent Alpha migrates only when an explicit rebuild trigger occurs.
4. The library does not maintain an exhaustive authoritative consumer database or make Alpha's project-specific decisions.

The cell has two dependent task lineages: the library change and the Alpha migration.

## 2. Required inputs

Read only:

- candidate v0.2;
- validation v0.2;
- frozen package README and files `01`, `02`, `03`, `04`;
- exact Owner V1 authorization;
- V1 execution-package README;
- controller and fixture receipts;
- exact fixture commit;
- CommonLib v1 contract and Alpha's v1 usage from the fixture;
- this cell contract.

Do not read the S8 worker prompt or S8 result. S7 output is expected to contain sufficient migration facts and therefore must never be supplied to the fresh S8 cell.

## 3. Library task

```yaml
task_id: TLR-V1-S7-LIBRARY-001
scenario_id: S7
branch: tlr-v1-s7-commonlib-v2
base: fixture_commit
authority_owner: synthetic-library-owner
primary_writer: S7_library_worker
allowed_write_roots:
  - libraries/common-lib/
  - run-evidence/S7-library/
prohibited_write_roots:
  - targets/
  - shared/
  - repository-governance/
```

### Required CommonLib v2 outputs

The branch must contain and cross-reference:

- current v2 API contract;
- v2 source and contract tests;
- concise human-facing change explanation;
- downstream-Agent-facing migration explanation;
- documentation overview;
- exact original/source requirement references used to justify the v2 design;
- explicit compatibility/breaking-change status.

The frozen v2 contract requires:

```text
parse_record(text: str, mode: "strict" | "lenient" = "strict") -> ParseResult
legacy_mode removed
ParseResult.value: Record | null
ParseResult.errors: list[ParseIssue]
parse failure represented in errors; function no longer returns None
```

The Agent-facing guide must accurately communicate, without relying on version number alone:

- v1 and v2 signatures;
- affected function, return contract and configuration key;
- replacement of `strict=false` by `mode="lenient"`;
- removal of `legacy_mode`;
- replacement of `None` checks by `result.errors` / `result.value` handling;
- strict and lenient test requirements;
- verification that the old configuration key no longer remains.

The human-facing note may remain concise but must point readers to the Agent migration guide.

The documentation overview must list exact paths and roles for:

- `API.md`;
- the human-facing change document;
- the Agent-facing change document;
- tests/examples.

### Library-side prohibitions

The library task must not:

- create or maintain an exhaustive authoritative list of all consuming projects;
- modify Alpha;
- claim Alpha has accepted or completed migration;
- infer project-specific upgrade timing;
- use only a commit list or vague release sentence;
- create a contradictory human/Agent documentation pair.

## 4. Library mechanical checks

At minimum record:

- M2 canonical task lineage;
- M3 declared versus actual write set;
- M5 authority owner unchanged;
- M7 presence, cross-reference and required migration facts;
- M8 source requirement and API-change preservation;
- M11 input/output/blob/commit identity.

Every output file record includes both `blob_sha` and the commit that created or last updated that exact blob.

If the library output is incomplete or contradictory, stop before Alpha migration and return a candidate/executor/protocol finding. Do not silently repair the guide in the Alpha task.

## 5. Alpha migration task

The controller creates the Alpha branch only after the library task has a preserved final commit:

```yaml
task_id: TLR-V1-S7-ALPHA-001
scenario_id: S7
branch: tlr-v1-s7-alpha-migration
base: S7_library_final_commit
authority_owner: synthetic-alpha-owner
primary_writer: S7_alpha_worker
explicit_trigger: synthetic_Owner_requests_Agent_Alpha_rebuild_against_CommonLib_v2
allowed_write_roots:
  - targets/agent-alpha/
  - run-evidence/S7-alpha/
prohibited_write_roots:
  - libraries/common-lib/
  - targets/agent-beta/
  - shared/
  - repository-governance/
```

### Required Alpha behavior

The Alpha worker must:

1. read the documentation overview;
2. identify and read the Agent-facing v1→v2 guide;
3. inspect Alpha's own dependency declaration and actual usage;
4. find all planted assumptions:
   - `strict=false`;
   - `legacy_mode=true`;
   - `None` return checks;
5. migrate them according to the documented v2 contract;
6. add or adjust Alpha-local tests for strict/lenient behavior and structured errors;
7. verify the removed configuration key no longer remains;
8. preserve a project-specific acceptance/result record.

The Alpha worker must not:

- treat the human-facing note alone as sufficient when the Agent guide exists;
- modify CommonLib to make migration easier;
- infer an exhaustive list of other consumers;
- make Beta or repository-global changes;
- treat library release as automatic project adoption without the explicit rebuild trigger.

## 6. Positive-path acceptance

S7 may provisionally pass only if:

- library outputs satisfy both documentation roles and navigation;
- human and Agent-facing information are semantically consistent;
- Agent-facing facts are sufficient for the planted Alpha migration;
- Alpha discovers its own actual use and migrates on demand;
- library and Alpha authority boundaries remain intact;
- all declared/actual paths match;
- every input/output is preserved by exact branch, commit and blob identity;
- no exhaustive authoritative consumer registry is introduced.

## 7. Cell output

```yaml
positive_documentation_cell_result:
  cell_id: TLR-V1-CELL-S7-001
  scenario_id: S7
  library_task_ref:
  library_branch_head:
  library_output_blobs: []
  documentation_completeness:
  human_Agent_semantic_consistency:
  Alpha_trigger_ref:
  Alpha_task_ref:
  Alpha_branch_head:
  Alpha_output_blobs: []
  migration_facts_discovered_from_docs: []
  project_actual_usage_found: []
  declared_vs_actual_write_sets: []
  mechanical_checks: {}
  critical_failures: []
  incidents_and_retries: []
  S8_firewall_warning: do_not_supply_this_cell_output_or_sufficient_guide_to_S8
  provisional_disposition: SCENARIO_PASS | SCENARIO_FAIL_CANDIDATE_OR_SEMANTIC | SCENARIO_FAIL_EXECUTOR | SCENARIO_BLOCKED_MISSING_AUTHORITY_OR_FACT | SCENARIO_INVALID_PROTOCOL_OR_IDENTITY
```

## 8. Stop rules

Stop when:

- the library or Alpha branch/base differs from the controller map;
- documentation omits or contradicts required contract facts;
- Alpha would need to guess a missing migration fact;
- a task writes outside its allowlist;
- the rebuild trigger or authority is missing;
- exact output identities cannot be preserved;
- private/real material appears;
- candidate or frozen scenario semantics would need revision.