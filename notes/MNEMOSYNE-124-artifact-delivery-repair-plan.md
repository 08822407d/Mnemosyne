# MNEMOSYNE-124 Artifact Delivery and Direct Low-Risk Generation Repair Plan

> Historical suspect-period planning record. This file was created after PR #173 during a user-reported reasoning-quality incident. It is retained for audit only and is superseded by `current/artifact-delivery-and-direct-generation-guard.md` and `notes/codex-task-results/MNEMOSYNE-127-result.md`. It is not current guidance or execution source.

## Purpose

Repair workflow failures recorded by Issue #170 and Issue #171.

This is a candidate implementation package. It does not by itself modify the execution source.

## Scope

### Issue #170 — Long transfer artifact file-first delivery

Trigger file-first delivery when all or most of the following apply:

- content is long;
- content must be copied into another ChatGPT conversation, Codex task, or external tool;
- Markdown/YAML/code block structure must be preserved;
- content is a prompt package, handoff package, review package, verification checklist, or multi-part instruction.

Expected behavior:

- create downloadable artifact first;
- keep chat response as summary, pointer, and user operation instructions;
- split into chunks only when a single artifact cannot safely represent the transfer.

### Issue #171 — Immediate generation of low-risk requested artifacts

When the user explicitly requests a file artifact and:

- no repository write is required;
- no external action authorization is required;
- no sensitive data handling decision is required;
- no unresolved design decision must be made;

then generate the artifact in the same response.

Do not defer generation merely to request another confirmation round.

## Exceptions

The Deep Research full-report-body rule remains unchanged:

- full Deep Research final report content remains in the final report body;
- downloadable exports are secondary copies only.

## Validation criteria

Future verification should check:

- requested artifact exists when required;
- download link is provided;
- long transfer body is not unnecessarily duplicated in chat;
- required user actions are separated from explanation;
- no artifact generation rule accidentally grants execution authority.

## Open decisions

Before modifying `current/human-approved-spec.md`, review:

- exact section placement;
- interaction with existing Section 12 operation/conclusion separation;
- interaction with Section 13 file-first rules;
- whether a separate operator appendix is preferable to expanding execution-source rules.

## Historical disposition

MNEMOSYNE-127 selected the separate user-approved behavior-guard pattern, matching the repository's existing single-active PR guard architecture. The earlier proposal's useful intent was re-evaluated and rewritten; its ambiguous conditions and fragmented PR lineage were not adopted as the active implementation.
