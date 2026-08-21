
# Mnemosyne AI Onboarding Package — Design 001

```yaml
design_id: MNE-AI-ONBOARDING-PACKAGE-DESIGN-001
status: proposed_non_execution_source
target_consumers:
  - Claude_Web_with_Fable_5
  - Claude_Code_in_VS_Code
  - Claude_Code_CLI
  - ChatGPT_or_other_repository_reviewers
root_CLAUDE_md: not_proposed_in_v0_1
root_AGENTS_md: not_proposed_in_v0_1
```

## 1. Problem

Mnemosyne contains a large number of status, guard, handoff, evidence and historical files. A capable model can inspect the repository, but without a stable entrypoint it may:

- read too much cold history;
- mistake status or handoff files for execution authority;
- import an unrelated live route;
- miss the correct guidance set;
- duplicate stale facts in a new summary;
- require a long conversation to reconstruct project purpose and current boundaries.

The onboarding package should make initial understanding fast without becoming a second execution source.

## 2. Governing constraints

The package must preserve:

1. `current/human-approved-spec.md` as the only execution source.
2. `commands/load-mnemosyne-guidance.md` as the behavior-guidance loader.
3. task-specific packages and direct Owner instructions as the source of local task authority.
4. `current/active-context.md`, `handoff/handoff-current.md`, TODOs and status files as non-execution-source evidence.
5. cold originals as `DO_NOT_READ` / `ON_DEMAND`.
6. repository-visibility and privacy checks before importing material.
7. explicit separation among analysis, advice, maintenance and takeover modes.

The current v0.1 spec says `CLAUDE.md` and `AGENTS.md` are future capabilities. Therefore this design does not add either root file. A future tiny root pointer may be considered only after a separate approved spec change.

## 3. Proposed repository package

```text
notes/ai-onboarding/
├── MNEMOSYNE-AI-START-HERE.md
├── MNEMOSYNE-REPOSITORY-MAP.yaml
├── MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md
├── MNEMOSYNE-CURRENT-STATE-INDEX.yaml
├── MNEMOSYNE-CLAUDE-WEB-FAST-CONTEXT.md
├── MNEMOSYNE-CLAUDE-CODE-LOCAL-START.md
├── MNEMOSYNE-TAKEOVER-CHECKLIST.md
└── MNEMOSYNE-AI-ONBOARDING-MANIFEST.yaml
```

A short link should later be added to `README.md`:

```text
AI / external-review entrypoint:
notes/ai-onboarding/MNEMOSYNE-AI-START-HERE.md
```

## 4. Design rules

### Single entrypoint, no duplicated truth

`MNEMOSYNE-AI-START-HERE.md` explains how to navigate but does not copy detailed current state. Dynamic facts live in their canonical status files.

### Pointer-based current state

`MNEMOSYNE-CURRENT-STATE-INDEX.yaml` lists:

- topic;
- canonical status path;
- authority class;
- freshness rule;
- whether the file is routinely readable or on-demand.

It should not copy mutable status values.

### Mode-specific reading

The package defines four modes:

```yaml
analysis_or_advice:
  default: read_only
  minimum:
    - START_HERE
    - human_approved_spec
    - repository_map
    - task_specific_sources

formal_review:
  default: read_only
  additional:
    - exact review package
    - cited status and evidence files

local_maintenance:
  write_requires_explicit_task: true
  additional:
    - load_mnemosyne_guidance
    - relevant guards
    - current repository and PR state

takeover:
  requires_explicit_Owner_selection: true
  requires:
    - exact task or handoff package
    - guidance refresh
    - task reconstruction
    - authority and forbidden-action confirmation
```

### Web and local variants share one truth

The web fast-context card is a compact subset for attachment or Project knowledge. The local-start file explains how Claude Code should use repository search and Git. Both point to the same execution source and repository map.

## 5. Fast-context targets

### Claude Web / Fable 5

A model should understand in approximately five minutes:

- what Mnemosyne is;
- what is and is not execution authority;
- which files to read for the current request;
- how to label facts, inferences and recommendations;
- when to request a task-specific package;
- why cold originals are not loaded by default.

### Claude Code

A local agent should understand:

- it may inspect the repository and run ordinary Git/tooling operations;
- repository writes require an explicit task;
- final state and validation invariants matter more than a brittle command transcript;
- it must inspect current branch/PR state before writing;
- it should return a diff/verification report;
- it must not infer a live handoff from `handoff-current`.

### Takeover

A new agent may take over only after:

- Owner explicitly selects takeover;
- exact task and required guidance are loaded;
- repository state is reverified;
- local task, authority and exclusions are restated;
- unresolved decisions are separated from implementation.

## 6. Lifecycle and freshness

The onboarding package is stable navigation. It should change rarely.

Dynamic changes should normally update:

- canonical status files;
- current route records;
- task-specific packages;

not the onboarding prose.

The onboarding manifest records file identities and package version. A periodic review checks only pointers, not every project fact.

## 7. Implementation sequence

1. Merge the pending F2/G2A/handoff/HVAL publication.
2. Create a separate onboarding branch and Ready PR.
3. Add the eight files above.
4. Add one README pointer.
5. Verify no execution-source or active-guard file changes.
6. Test three synthetic sessions:
   - Claude Web read-only advice;
   - Claude Code local maintenance;
   - fresh takeover with explicit task.
7. Record gaps and refine before considering a root `CLAUDE.md`.

## 8. Acceptance criteria

```yaml
execution_source_duplicated: false
root_CLAUDE_md_created: false
root_AGENTS_md_created: false
dynamic_status_values_duplicated: false
web_fast_context_exists: true
local_agent_start_exists: true
takeover_checklist_exists: true
repository_map_machine_readable: true
cold_originals_default_on_demand: true
analysis_and_write_authority_separated: true
README_pointer_added: true
```
