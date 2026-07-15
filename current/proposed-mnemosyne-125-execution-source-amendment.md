# Proposed Human-Approved Spec Amendment — MNEMOSYNE-125

## Purpose

Operationalize existing Section 12 and Section 13 artifact delivery principles.

This proposal does not take effect until promoted into `current/human-approved-spec.md` through normal self-improvement workflow review.

## Proposed additions to Section 13

### File-first delivery trigger conditions

When an artifact is intended for cross-conversation transfer, external AI task execution, or preservation of structured content, the default delivery format should be a downloadable file.

Examples:

- Codex task prompts;
- handoff packages;
- replay/startup prompts;
- review packages;
- verification checklists;
- multi-part structured instructions.

The chat response should contain:

- purpose;
- usage instructions;
- required user actions;
- download link.

The full artifact should not normally be duplicated as a large chat code block.

### Direct generation of explicitly requested low-risk artifacts

If a user explicitly requests an artifact and all of the following are true:

- no repository write is required;
- no external authorization decision is required;
- no sensitive-data handling decision is pending;
- no unresolved design decision determines the artifact content;

the artifact should be generated in the same response instead of only promising future generation.

### Validation criteria

A compliant response should satisfy:

- requested artifact exists when file delivery is selected;
- download location is provided;
- chat response contains a concise summary rather than an unnecessary duplicate full artifact;
- Deep Research final-report-body exception remains unchanged.

## Non-goals

This amendment does not:

- authorize repository writes;
- change Meta-Agent authority;
- change no-write proof policy;
- resolve HO-GUIDANCE-001;
- close Issue #170 or #171 before behavioral verification.
