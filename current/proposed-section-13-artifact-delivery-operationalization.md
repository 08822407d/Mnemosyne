# MNEMOSYNE-125 — Section 13 Artifact Delivery Operationalization Proposal

## Purpose

This document proposes an operational clarification for existing Section 12 and Section 13 rules in `current/human-approved-spec.md`.

It is not itself an execution source.

## Existing basis

Section 13 already defines long-content file-first delivery. This proposal only defines triggers, validation, and boundaries.

## Proposed trigger rules

### File-first delivery required

Prefer a downloadable file as the primary transfer artifact when the output is:

- a Codex task prompt;
- a handoff package;
- a replay/startup prompt;
- a review package;
- a verification checklist;
- a multi-part instruction intended for another AI conversation;
- a structured artifact where Markdown/YAML/code-block integrity matters.

The chat response should contain:

- purpose;
- usage instructions;
- download link;
- required user actions only.

### Direct response allowed

Direct chat output remains appropriate for:

- short explanations;
- short checklists;
- short summaries;
- non-transfer content not requiring structural preservation.

### Same-response low-risk artifact generation

When a user explicitly requests a file artifact and:

- no repository write is required;
- no external action authorization is required;
- no unresolved design decision is being made;
- no sensitive-content decision is pending;

the expected behavior is to generate the artifact in the same response rather than promise future generation.

## Validation criteria

A compliant response should satisfy:

- requested file artifact exists when generation is appropriate;
- response contains a clear file link and short purpose summary;
- long transfer content is not duplicated as a large chat code block;
- Deep Research full-report-body exception remains unchanged.

## Boundary

This proposal does not:

- modify no-write proof policy;
- modify Meta-Agent authority;
- resolve HO-GUIDANCE-001;
- close Issue #170 or #171 without behavior verification.
