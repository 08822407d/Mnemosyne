# Execution Source, Target Truth, and Supporting Memory — Terminology Note v0.1

> Non-execution-source terminology clarification derived from the Owner's OR-01 review. It explains existing roles; it does not amend `current/human-approved-spec.md` or any target truth source.

```yaml
terminology_note_id: MNEMOSYNE-EXECUTION-SOURCE-TARGET-TRUTH-TERMINOLOGY-001
task_id: MNEMOSYNE-202
status: owner_aligned_explanatory_note_not_execution_source
source_owner_review: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
execution_source_modified: false
```

## 1. Owner-aligned analogy

The accepted working analogy is:

```text
model ≈ CPU / replaceable computation unit
execution source ≈ the currently approved program that controls formal Agent behavior
supporting files ≈ requirements, source data, design evidence, state, logs, and recovery material
```

The analogy is intended to distinguish control logic from the evidence and state that helped produce or support it.

## 2. Execution source

An **execution source** is the currently approved programmatic/behavioral control layer that tells an Agent how it is formally required to act within its scope.

It answers questions such as:

- what purpose and constraints control this Agent;
- what behavior is required or prohibited;
- what authority and source precedence apply;
- what to do when sources conflict;
- what safety, privacy, escalation, and user-decision boundaries control execution.

For current Mnemosyne, `current/human-approved-spec.md` is the sole execution source. More specific approved guards operationalize it but do not become competing independent execution sources.

“Current” means **currently adopted and authoritative**, not merely the newest file by timestamp or commit.

## 3. What is not automatically execution source

The following may be essential without directly controlling behavior:

- raw conversations and original requirements;
- research prompts and reports;
- candidate requirements or designs;
- decision/rationale records;
- historical execution-source versions;
- active/current state;
- handoff;
- evaluation, postmortem, and task-result records;
- model interpretations and summaries.

Their normal role is to supply evidence, context, design input, auditability, or recovery. They influence future execution logic only through the applicable analysis, conflict review, Owner decision, and authorized update process.

## 4. Target truth source

A **target truth source** is broader than an execution source.

It may contain or designate:

- the target's approved behavior/program;
- authoritative business rules or current configurations;
- authoritative target state or data;
- the identity and location of canonical objects;
- conflict precedence among authoritative components.

A target truth source can therefore be one declared file, a controlled set of files, a database/store, or another explicit authoritative boundary. “Single target truth” means no ambiguous competing authority, not necessarily one physical file.

## 5. Current state and handoff

- **Current state / active context** answers: where is the work now, what is complete, blocked, unknown, and the safe next action?
- **Handoff** answers: how should a fresh qualified session navigate to the execution/target truth and resume?

Both may be newer than the execution source and still remain non-authoritative navigation. If they conflict with current approved control logic, the conflict must be surfaced rather than resolved by silently treating the newer navigation file as the program.

## 6. Historical versions

Historical execution-source versions should remain available for:

- explaining why the system behaved a certain way at a past time;
- reconstructing supersession and migration;
- evaluating whether an amendment introduced a defect;
- rollback or recovery when appropriate.

They are historical programs, not simultaneously active programs. An explicit current adoption marker and version/lineage relationship prevent ambiguity.

## 7. Practical test

When classifying a file or object, ask:

1. Does this object directly control what the Agent must do now?
2. Has the Owner/current authority adopted it for that role?
3. If it conflicts with another object, is it explicitly the controlling source?
4. Is it instead evidence, input, current state, navigation, history, or a candidate?

Only the approved controlling object/source set is execution source. Importance, detail, recency, or repository location alone do not grant that role.

## 8. Boundary

This note does not decide whether future target systems use one file or several canonical files, and it does not replace target-local authority design. It provides a shared vocabulary for later Mnemosyne, Meta-Agent, and target-system work.
