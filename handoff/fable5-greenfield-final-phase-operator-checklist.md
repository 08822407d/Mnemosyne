# Operator Checklist — FABLE5-GREENFIELD Final-Phase Handoff

## A. Finish repository handoff preparation

1. Review the handoff PR created by the old conversation.
2. Confirm it is the only merge target and is not draft.
3. Merge it manually.
4. Do not enable auto-merge.

## B. Start the receiving ChatGPT conversation

1. Open a new **ordinary ChatGPT conversation**. ChatGPT Work is not needed for
   handoff receipt or storage-only result intake.
2. Ensure the GitHub app can access `08822407d/Mnemosyne`.
3. Upload or paste:
   `MNEMOSYNE-FABLE5-GREENFIELD-FINAL-PHASE-STARTUP-PROMPT.md`.
4. Send it.
5. Wait for the receiving conversation's `mnemosyne_handoff_receive` report.

## C. Load guidance as a separate operation

After the receive report, send exactly:

`加载 MNEMOSYNE 约束指导`

Wait for a behavior-guidance refresh report that confirms:

- the received task is preserved;
- handoff was not replaced by unrelated maintenance state;
- `current/human-approved-spec.md` is the execution source;
- single-active PR and artifact-delivery guards are applied.

## D. Execute Fable GF-STEP-4

1. Open a fresh Fable 5 conversation.
2. Research mode: **OFF**.
3. Upload the corrected
   `FABLE5-GREENFIELD-001-GF-STEP-4-complete-input-package.zip`,
   or upload the task plus the four files individually.
4. Send the literal bootstrap from the task instructions.
5. Do not provide any existing GPT/Mnemosyne design file.
6. Download Fable's final Markdown output.
7. Preserve the Fable chat summary.

## E. Return the result to the new ChatGPT conversation

Provide:

- Fable's chat summary;
- the downloadable GF-STEP-4 Markdown file.

The receiver should:

- preserve it exactly;
- create one ready PR;
- not perform substantive acceptance under Thinking;
- classify only the declared continuation:
  - GF-STEP-3R repair gate; or
  - ready to request explicit authorization for GF-STEP-5.

## F. STEP5 firewall

Do not authorize STEP5 merely because STEP4 finishes.

STEP5 must wait for an explicit user message authorizing read-only access to
specific current-design paths. GPT Pro substantive adjudication and Mnemosyne
repairs remain a separate later workflow.

## G. Retire the old conversation

After the new conversation confirms receive + guidance refresh, do not return
new Fable results to the old long conversation. Keep it only as historical
audit context.
