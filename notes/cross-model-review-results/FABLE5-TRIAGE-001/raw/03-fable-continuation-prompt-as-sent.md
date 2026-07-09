# Fable Continuation Prompt As Sent

```yaml
record_type: raw_preservation_only
authority_level: non_execution_source_raw_preservation_only
created_by_task: MNEMOSYNE-096
verbatim_status: reconstructed_from_current_conversation_visible_text
source_note: copied from the maintenance conversation message that generated the prompt for Fable 5
```

```markdown
Load Mnemosyne guidance as behavior guidance only, not as a maintenance handoff route import.

We are continuing the Mnemosyne Fable 5 cross-model review triage after the maintenance conversation recorded a summary of your previous response in PR #142 / MNEMOSYNE-095. The current ChatGPT maintenance conversation is running at GPT-5.5 Thinking only because the user’s Pro quota is exhausted, so avoid relying on this lower-strength conversation for high-judgment canonicalization.

Your task is read-only review and planning only.

Do not write repository files.
Do not generate Codex tasks.
Do not propose executable repair prompts yet.
Do not resume or close the paused post-handoff route.
Do not treat Fable review as truth voting or automatic writeback authority.
Do not update execution source.
Do not authorize target workspace creation, target material ingestion, target repository write, regression formalization, operational build, or auto-writeback.

Repository to inspect if available:

```text id="812qfi"
08822407d/Mnemosyne
```

Read these current evidence files if available:

```text id="mri7az"
current/human-approved-spec.md
commands/load-mnemosyne-guidance.md
notes/cross-model-review-results/README.md
notes/cross-model-review-results/FABLE5-REVIEW-001/manifest.yaml
notes/cross-model-review-results/FABLE5-REVIEW-001/03-maintainer-triage.md
notes/cross-model-review-results/FABLE5-REVIEW-002/manifest.yaml
notes/cross-model-review-results/FABLE5-REVIEW-002/02-maintainer-triage.md
notes/cross-model-review-results/FABLE5-REVIEW-003/manifest.yaml
notes/cross-model-review-results/FABLE5-REVIEW-003/02-maintainer-triage.md
notes/codex-task-results/MNEMOSYNE-094-result.md
```

Also inspect PR #142 / branch if accessible:

```text id="h4vl87"
PR: MNEMOSYNE-095 record Fable follow-up triage response
Branch: mnemosyne-095-fable-triage-response
Files:
- notes/cross-model-review-results/FABLE5-TRIAGE-001/manifest.yaml
- notes/cross-model-review-results/FABLE5-TRIAGE-001/01-fable-response-after-human-answers-summary.md
- notes/codex-task-results/MNEMOSYNE-095-result.md
- notes/cross-model-review-results/README.md
```

If you cannot access the repository or PR, ask the user to provide the above files. Do not infer their contents.

Context you should assume only as user-provided maintenance-context, not as execution source:

```yaml id="hidpzm"
current_state:
  MNEMOSYNE_095:
    purpose: record your previous Fable 5 follow-up triage response after human answers
    status: draft_PR_created_not_merged
    record_style: canonical_summary_stored_not_verbatim
    concern: raw original Fable/user material should be preserved before high-judgment follow-up
  lower_strength_conversation_risk:
    current_chatgpt_model: GPT-5.5 Thinking
    pro_quota: exhausted
    user_instruction: preserve original materials and defer high-judgment decisions until higher model/pro quota restored or GPT-5.6 available
```

Your review tasks:

1. **Check MNEMOSYNE-095 summary fidelity**
   - Compare the PR #142 summary against your previous Fable response if the original response is available in the user message.
   - Identify omissions, distortions, or unsafe wording.
   - Pay special attention to whether summary-only storage is sufficient or whether a raw-preservation file should be added.
   - Do not rewrite files; only report what should be fixed later.

2. **Recommend raw-material preservation scope**
   - Specify exactly which original materials should be preserved before further reasoning:
     - user’s original Chinese answers;
     - conservative interpretation supplied to you;
     - the exact prompt/package sent to Fable;
     - your full previous Fable response;
     - current user instruction about lower-model risk and deferring high-judgment work.
   - Recommend a path and metadata shape, but do not create the file.
   - Mark the recommended record as non-execution-source, raw-preservation-only, and no-repair-authority.

3. **Define the remaining read-only evidence-audit steps**
   - For Q2-2 canonical warning layer:
     - list exact files and facts that must be checked;
     - distinguish source layer, model-origin evidence, latest-version evidence, and authority level;
     - do not select the canonical layer unless evidence is conclusive and the user’s rules do not conflict.
   - For R3 hygiene:
     - list exact fresh-snapshot checks needed for R3-F-001, R3-F-003, and R3-F-004;
     - classify each as likely repository residue, by-design transfer artifact, parallel-work timing artifact, connector/retrieval issue, or already-resolved;
     - do not approve cleanup.

4. **Produce a risk-controlled next-work plan**
   - Separate:
     - safe now under lower model / low judgment;
     - must wait for higher model or restored Pro quota;
     - requires explicit user approval before any write;
     - should not be done at all in this Fable review track.
   - Do not generate a Codex task.
   - Do not generate a repair PR prompt.
   - Do not create a final canonical decision for Q2-2 unless the evidence is unambiguous.

Required output format:

```yaml id="26z4gc"
fable_next_review_response:
  repository_access:
    status: accessed | not_accessed | partial
    files_checked:
      - path
    files_missing_or_unavailable:
      - path
  mnemosyne_095_summary_fidelity:
    assessment: accurate | mostly_accurate_with_corrections | inaccurate | cannot_assess
    required_corrections:
      - item
    raw_preservation_needed: true_or_false
    raw_preservation_reason: text
  raw_materials_to_preserve:
    recommended_path: text
    required_contents:
      - item
    required_metadata:
      - key
    authority_boundary: non_execution_source_raw_preservation_only
  q2_2_warning_layer_audit_plan:
    status: open
    priority: high
    evidence_to_check:
      - file_or_fact
    current_known_conflict:
      pro_version_rule: text
      latest_version_rule: text
      attribution_strength_issue: text
    decision_now: yes_or_no
    reason: text
  r3_hygiene_recheck_plan:
    R3-F-001:
      fresh_checks:
        - item
      likely_classification_if_unchanged: text
      cleanup_approval: not_approved
    R3-F-003:
      fresh_checks:
        - item
      likely_classification_if_unchanged: text
      cleanup_approval: user_decision_required
    R3-F-004:
      fresh_checks:
        - item
      likely_classification_if_unchanged: text
      cleanup_approval: not_approved_until_rechecked
  next_safe_steps:
    safe_now:
      - item
    defer_until_higher_model_or_pro_quota:
      - item
    requires_explicit_user_approval_before_write:
      - item
    out_of_scope:
      - item
  final_boundary_statement: >
    No repository writes, no Codex tasks, no execution-source update, no target
    workspace/material/write/build/regression action, and no paused-route resumption
    are authorized by this response.
```
```
