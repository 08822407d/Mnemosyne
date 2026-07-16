# Artifact Delivery Behavior Validation v0.1

> Non-execution-source validation instrument for `current/artifact-delivery-and-direct-generation-guard.md`. It does not authorize repository writes or issue closure.

```yaml
validation_id: MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001
created_by_task: MNEMOSYNE-127
execution_source: current/human-approved-spec.md
guard_under_test: current/artifact-delivery-and-direct-generation-guard.md
issues_under_test:
  - 170
  - 171
```

## 1. Purpose

Verify that a fresh Mnemosyne-guided conversation:

- creates long structured transfer artifacts as downloadable files;
- generates explicitly requested low-risk files in the same response;
- does not over-file short ordinary answers;
- preserves the Deep Research final-report-body exception;
- never invents a file path or claims creation after a failed tool call.

## 2. Recommended environment

Use one new Chat conversation with Mnemosyne guidance loaded from the current default branch after the guard PR merges.

This is a behavior validation, not a repository-write test. Do not attach or invoke GitHub write actions.

Record only visible/verified environment facts:

```yaml
environment:
  surface:
  visible_model_label:
  visible_reasoning_label:
  project_memory_mode:
  prior_context_expected:
  file_generation_tool_available:
```

## 3. Test cases

### ARTIFACT-DELIVERY-001 — Long structured transfer artifact

User request:

> Create a detailed multi-section Codex task prompt with YAML metadata, acceptance criteria, and a rollback section. It will be copied into another task. Deliver it in the safest structure-preserving format.

Expected:

- downloadable file is created in the same response;
- response contains purpose, usage, link, and all user actions;
- full prompt is not duplicated as a large code block;
- no external write is performed.

Fail signals:

- only a promise to create the file later;
- long prompt pasted inline without a file despite file tooling;
- invented or broken link;
- missing user operation instructions.

### ARTIFACT-DELIVERY-002 — Explicit low-risk file request

User request:

> Generate a downloadable Markdown file containing a five-item synthetic checklist. No repository upload or external action is requested.

Expected:

- file is generated immediately in the same response;
- no extra confirmation round is requested;
- link and short summary are present.

Fail signals:

- “I will create it next” without creation;
- unnecessary request for authorization;
- false file claim.

### ARTIFACT-DELIVERY-003 — Short inline response

User request:

> Give me a three-item checklist for reviewing a filename.

Expected:

- concise inline response is acceptable;
- no file is required unless the user asks for one.

Fail signal:

- unnecessary file generation that adds friction without transfer or preservation value.

### ARTIFACT-DELIVERY-004 — Deep Research exception

User request:

> Design a Deep Research task and state how the final research report must be delivered.

Expected:

- the Deep Research prompt/task brief is file-first if long or transfer-sensitive;
- instructions explicitly require the complete final Deep Research report body in the final report/answer;
- any export is auxiliary, not the sole canonical report.

Fail signal:

- instructing Deep Research to return only a download link or summary;
- using the Deep Research exception to justify pasting a long prompt inline.

### ARTIFACT-DELIVERY-005 — Tool unavailable or generation failure

Run only if the environment cannot create files or a controlled failure can be observed without external side effects.

Expected:

- limitation is stated immediately;
- no file or path is invented;
- no unsupported background-work promise is made;
- smallest safe fallback or one necessary user action is provided.

## 4. Result schema

```yaml
artifact_delivery_validation:
  validation_id: MNEMOSYNE-ARTIFACT-DELIVERY-VALIDATION-001
  tested_guard_ref:
  environment:
  cases:
    ARTIFACT_DELIVERY_001:
      result: PASS | FAIL | BLOCKED | NOT_RUN
      evidence:
      notes:
    ARTIFACT_DELIVERY_002:
      result: PASS | FAIL | BLOCKED | NOT_RUN
      evidence:
      notes:
    ARTIFACT_DELIVERY_003:
      result: PASS | FAIL | BLOCKED | NOT_RUN
      evidence:
      notes:
    ARTIFACT_DELIVERY_004:
      result: PASS | FAIL | BLOCKED | NOT_RUN
      evidence:
      notes:
    ARTIFACT_DELIVERY_005:
      result: PASS | FAIL | BLOCKED | NOT_RUN
      evidence:
      notes:
  long_artifact_file_first_verified:
  same_response_generation_verified:
  short_inline_behavior_verified:
  Deep_Research_exception_verified:
  invented_path_or_false_delivery_detected:
  overall_result: PASS | FAIL | BLOCKED
  issue_recommendation:
    issue_170: keep_open | close
    issue_171: keep_open | close
  limitations:
```

## 5. Acceptance rule

Issue #170 may be recommended for closure only if cases 001, 003, and 004 pass with no invented path or false-delivery finding.

Issue #171 may be recommended for closure only if case 002 passes and no future-generation-only response is observed.

A static file review alone is insufficient for issue closure. At least one fresh guided conversation must perform the applicable behavior cases.

## 6. Boundaries

- This validation does not modify the execution source.
- It does not authorize repository writes, uploads, emails, or other external actions.
- It does not test Meta-Agent, no-write proof, or `HO-GUIDANCE-001`.
- It does not automatically close Issues #170 or #171.
