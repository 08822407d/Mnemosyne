# Meta-Agent Dedicated-Repository Mechanical Inventory — Codex/Local Git Task

> Mechanical prerequisite for Meta-Agent migration mapping. This task resolves the recursive Git-tree capability blocker found by `META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001`. It produces complete repository-object evidence and a preliminary deterministic classification. It does not perform semantic migration mapping, change Meta-Agent live state, or write the destination repository.

```yaml
task_id: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
prepared_by: MNEMOSYNE-192
status: READY_AFTER_MNEMOSYNE_192_MERGE_NOT_EXECUTED
preferred_surface:
  - OpenAI_Codex_Code_mode_with_full_repository_checkout_and_terminal
  - equivalent_local_git_checkout
source_repository: 08822407d/Mnemosyne
minimum_source_baseline: 5bb586c057c228fbb80e37529ed1245e7366f482
source_root: target-projects/meta-agent/
destination_repository: 08822407d/Meta-Agent
destination_write_authorized: false
Meta_Agent_target_truth_change_authorized: false
Meta_Agent_live_navigation_change_authorized: false
reasoning_class: mechanical_and_bounded_deterministic_classification
Pro_required: false
```

## 1. Why this task exists

The prior Pro migration-preparation run correctly stopped because the connected GitHub search/file surface could not prove recursive Git tree closure. Repeating that full task on the same surface would waste frontier quota.

This task uses a checked-out Git repository and Git's object model to produce the missing evidence. It deliberately separates:

```yaml
this_task_E0:
  - complete_tree_and_blob_identity
  - deterministic_content_hashes
  - front_matter_extraction
  - path_rule_preclassification

later_Pro_task_E1:
  - final_authority_and_memory_role_adjudication
  - migration_disposition
  - destination_mapping
  - behavior_guidance_adoption
  - memory_system_alignment
  - Owner_initialization_decision_package
```

## 2. Required first response

The executor must begin with:

```yaml
execution_intent:
  response_role: MECHANICAL_EXECUTION
  task_id: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
  execution_disposition: RUN_NOW_REQUIRED
  source_repository_write: authorized_within_exact_paths
  destination_repository_write: prohibited
  target_truth_change: prohibited
  live_navigation_change: prohibited
  cutover: prohibited
```

Do not ask the user to repeat decisions already frozen here.

## 3. Execution-time preflight

Before branch creation:

```yaml
preflight:
  repository: 08822407d/Mnemosyne
  execution_time_latest_master:
  minimum_baseline_is_ancestor_or_identical: true
  PR_256_merge_present: true
  accessible_open_PRs: []
  exact_task_ID_matches: []
  intended_branch_matches: []

  destination_repository: 08822407d/Meta-Agent
  destination_state:
    commits: 0
    branches: []
    open_PRs: []

  target_truth:
    path: target-projects/meta-agent/current/approved-spec.md
    effective_for_operational_use: false
```

Stop with `BLOCKED_STATE_CHANGED` if:

- latest master does not contain PR #256;
- another open PR overlaps `target-projects/meta-agent/migration/source-inventory/`;
- the destination is no longer empty;
- target truth or operational status changed;
- the checkout is shallow or missing objects required by the pinned source commit;
- Git commands cannot expose object names and paths losslessly.

## 4. Branch and write scope

Create exactly one branch from execution-time latest `master`:

```text
meta-agent-dedicated-repository-mechanical-inventory-001
```

Create at most one PR.

Allowed paths:

```text
target-projects/meta-agent/migration/source-inventory/
notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001-result.md
notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001-pr-finalization.md
```

Do not modify:

```text
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/current/active-context.md
target-projects/meta-agent/handoff/handoff-current.md
target-projects/meta-agent/authority/
target-projects/meta-agent/methodology/
target-projects/meta-agent/cases/
target-projects/meta-agent/history/
current/human-approved-spec.md
08822407d/Meta-Agent (all paths)
```

## 5. Required Git evidence

Pin one source commit:

```bash
SOURCE_COMMIT="$(git rev-parse origin/master)"
git merge-base --is-ancestor 5bb586c057c228fbb80e37529ed1245e7366f482 "$SOURCE_COMMIT"
SUBTREE_SHA="$(git rev-parse "$SOURCE_COMMIT:target-projects/meta-agent")"
```

The checkout must contain all required objects. Verify:

```bash
git cat-file -e "$SOURCE_COMMIT^{commit}"
git cat-file -e "$SUBTREE_SHA^{tree}"
```

Generate a lossless recursive stream twice:

```bash
git ls-tree -r -t -l -z "$SOURCE_COMMIT" -- target-projects/meta-agent/
```

`-r` recurses, `-t` includes tree entries, `-l` includes blob sizes, and `-z` preserves path bytes without newline/quoting ambiguity.

The two independent invocations must be byte-identical. Compute SHA-256 for each raw stream before parsing.

## 6. Required generator

Create and commit a standard-library-only generator:

```text
target-projects/meta-agent/migration/source-inventory/generate-source-inventory.py
```

The generator must:

1. accept `--source-commit`, `--source-root`, and `--output-dir`;
2. execute Git commands through `subprocess` without shell interpolation;
3. parse NUL-delimited `git ls-tree` output losslessly;
4. record every `tree`, `blob`, and `commit` entry if present;
5. verify each object with `git cat-file -e`;
6. obtain blob bytes using `git cat-file blob <sha>`;
7. compute SHA-256 and byte length for every blob;
8. classify UTF-8 versus binary without OCR or content rewriting;
9. extract selected scalar YAML front-matter fields when present;
10. apply deterministic path-rule preclassification;
11. write canonical UTF-8/LF JSONL and YAML/Markdown receipts;
12. sort records by raw repository path;
13. fail on duplicate path, unparseable object line, missing object, path outside source root, or nondeterministic output.

Do not depend on PyYAML or network packages. A minimal scalar front-matter extractor is sufficient; preserve `front_matter_parse_limited: true` when nested YAML is not parsed.

## 7. Output package

Create:

```text
target-projects/meta-agent/migration/source-inventory/README.md
target-projects/meta-agent/migration/source-inventory/generate-source-inventory.py
target-projects/meta-agent/migration/source-inventory/source-tree-closure-v0.1.yaml
target-projects/meta-agent/migration/source-inventory/source-tree-entries-v0.1.jsonl
target-projects/meta-agent/migration/source-inventory/source-blob-inventory-v0.1.jsonl
target-projects/meta-agent/migration/source-inventory/source-artifact-preclassification-v0.1.jsonl
target-projects/meta-agent/migration/source-inventory/source-inventory-verification-v0.1.md
```

Do not commit a NUL-delimited raw stream if repository tooling cannot review it safely. Instead preserve its SHA-256, byte length, exact command, and deterministic parsed representation.

## 8. Tree-entry schema

Every object entry:

```yaml
tree_entry:
  source_repository: 08822407d/Mnemosyne
  source_commit:
  source_root: target-projects/meta-agent/
  root_subtree_sha:
  path:
  relative_path:
  mode:
  object_type: tree | blob | commit
  object_sha:
  object_size: integer_or_null
```

For blob entries add:

```yaml
blob_identity:
  git_blob_sha:
  bytes:
  content_sha256:
  encoding: utf_8 | binary
  final_LF: true | false | not_applicable
```

## 9. Front-matter extraction

For UTF-8 files beginning with `---`, extract only unambiguous scalar values for:

```yaml
- target_project_id
- artifact_id
- artifact_role
- status
- authority_level
- target_truth_source
- target_runtime_truth_source
- target_runtime_truth_source_designated
- target_runtime_truth_source_effective
- effective_for_operational_use
- task_id
- research_id
- review_id
- migration_id
- checkpoint_id
```

Record:

```yaml
front_matter:
  present:
  extracted_scalars: {}
  parse_limited: true
  raw_front_matter_sha256:
```

Do not interpret nested structures as final authority.

## 10. Deterministic preliminary classification

This classification is input to later frontier review, not final migration disposition.

### 10.1 Path rules

```yaml
rules:
  current/approved-spec.md:
    preliminary_authority_class: target_truth
    migration_zone: Z1_TARGET_CORE
    requires_frontier_review: true

  current/:
    preliminary_authority_class: current_state_or_target_behavior_support
    migration_zone: Z1_TARGET_CORE

  authority/:
    preliminary_authority_class: owner_or_authority_support
    migration_zone: Z1_TARGET_CORE

  methodology/:
    preliminary_authority_class: approved_method_or_method_candidate
    migration_zone: Z1_TARGET_CORE

  cases/:
    preliminary_authority_class: case_or_feedback_evidence
    migration_zone: Z2_TARGET_EVIDENCE

  history/:
    preliminary_authority_class: decision_or_migration_history
    migration_zone: Z1_TARGET_CORE

  handoff/:
    preliminary_authority_class: handoff_or_receive_evidence
    migration_zone: Z1_TARGET_CORE

  research/:
    preliminary_authority_class: research_evidence_or_raw_transport
    migration_zone: Z2_TARGET_EVIDENCE

  candidates/:
    preliminary_authority_class: candidate
    migration_zone: Z3_TARGET_CANDIDATES

  migration/:
    preliminary_authority_class: migration_control_or_historical_migration_evidence
    migration_zone: Z4_TARGET_MIGRATION_CONTROL

  decision-support/:
    preliminary_authority_class: candidate_or_decision_support
    migration_zone: Z3_TARGET_CANDIDATES

  commands/:
    preliminary_authority_class: target_process_support_candidate
    migration_zone: Z1_TARGET_CORE
```

Anything unmatched becomes:

```yaml
preliminary_authority_class: unknown_requires_frontier_review
migration_zone: unknown_requires_frontier_review
```

### 10.2 Status and historical hints

Use front matter and path names only to add hints such as:

```yaml
- active_or_current
- candidate_not_adopted
- evidence_non_execution
- historical_timepoint
- failed_or_superseded_possible
- raw_transport
- unknown
```

Never mark an artifact `retire`, `exclude`, or `preserve_exactly` as a final decision in this mechanical task.

### 10.3 Material classification

Because the source repository is public, record:

```yaml
material_observation: existing_public_Git_history
new_storage_approval_implied: false
```

If a file itself declares private/secret/confidential content or cannot be decoded/classified, mark `material_review_required: true`. Do not expose additional private material.

## 11. Closure receipt

`source-tree-closure-v0.1.yaml` must include:

```yaml
tree_closure:
  task_id: META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001
  source_repository: 08822407d/Mnemosyne
  source_commit:
  source_root: target-projects/meta-agent/
  root_subtree_sha:
  git_version:
  command:
  raw_stream_1_sha256:
  raw_stream_2_sha256:
  raw_streams_identical: true
  raw_stream_bytes:
  total_entries:
  tree_count:
  blob_count:
  commit_entry_count:
  duplicate_paths: 0
  missing_objects: 0
  paths_outside_root: 0
  tree_entries_manifest_sha256:
  blob_inventory_sha256:
  preclassification_manifest_sha256:
  deterministic_second_generation_match: true
  recursive_tree_complete: true
  verifier_relation:
  limitations: []
```

If any required field cannot be established, return `BLOCKED_MECHANICAL_INVENTORY_INCOMPLETE` and do not create a PR claiming PASS.

## 12. Independent reproducibility check

Run the committed generator twice into separate temporary directories from a clean source commit and compare:

```yaml
- closure files excluding run timestamp
- tree entries JSONL
- blob inventory JSONL
- preclassification JSONL
```

All content hashes must match. Timestamps, if used, belong only in the human-readable result record and must not contaminate deterministic manifests.

## 13. Result record

The task result must state:

```yaml
result:
  source_commit:
  root_subtree_sha:
  recursive_tree_complete:
  tree_count:
  blob_count:
  manifests_and_hashes:
  preliminary_unknown_count:
  material_review_required_count:
  source_repository_writes:
  destination_repository_writes: 0
  target_truth_modified: false
  live_navigation_modified: false
  status: PASS_TO_FRONTIER_MAPPING_RESUME | BLOCKED_MECHANICAL_INVENTORY_INCOMPLETE
```

## 14. PR requirements

Before PR creation repeat open-PR and branch-lineage checks. The PR must:

- contain only allowed paths;
- be draft initially;
- include source commit and root subtree SHA;
- state that classification is preliminary/non-authoritative;
- state that destination writes and cutover remain prohibited;
- identify the next task as `META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001`;
- be marked ready only after final manifest re-read and hash verification.

## 15. Prohibited shortcuts

Do not:

- use GitHub code search as the inventory source;
- use `find` on a possibly incomplete checkout without object identity;
- omit tree entries;
- normalize or rename source paths;
- infer final migration dispositions;
- update live navigation;
- write the destination;
- initialize `08822407d/Meta-Agent`;
- perform shadow copy or cutover;
- add private material;
- claim exact backend identity.

## 16. Safe next action

After human merge of the E0 PR, run:

```text
META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001
```

in the dedicated Meta-Agent Pro conversation. That task consumes the merged mechanical evidence and must not repeat recursive enumeration unless identity verification fails.
