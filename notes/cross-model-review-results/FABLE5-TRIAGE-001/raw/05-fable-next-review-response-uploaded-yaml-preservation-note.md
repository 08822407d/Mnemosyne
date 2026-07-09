# Fable Next Review Response Uploaded YAML — Preservation Note

```yaml
record_type: raw_preservation_gap_notice
authority_level: non_execution_source_raw_preservation_only
created_by_task: MNEMOSYNE-096
intended_material: Fable next review response YAML uploaded by user as txt attachment
source_attachment_name: FABLE5's respond for human-triage-reply-with-original-user-answers.txt
local_attachment_size_bytes_observed: 18714
local_attachment_sha256_observed: 32c8030b432d9340286109e439f9ec0cc214c8e2c6b2e91ae40d640541d67753
status: metadata_and_source_pointer_preserved_not_full_verbatim_text
reason_full_text_not_embedded: avoid_manual_chunking_or_reencoding_error_for_large_uploaded_attachment
handling: future_tool_or_higher_fidelity_transfer_should_copy_attachment_verbatim
```

## Notice

The uploaded txt attachment was readable in the maintenance conversation and contains the full `fable_next_review_response` YAML from Fable 5.

At MNEMOSYNE-096 time, this repository file preserves the attachment identity, observed byte size, and observed SHA-256, but **does not embed the complete verbatim attachment text**. This is a deliberate partial-preservation limitation: manually re-chunking a large base64/text payload inside the current chat-to-GitHub connector path risks introducing truncation or transcription errors.

Future high-judgment review should treat the complete uploaded txt attachment as not yet durably copied into GitHub unless a later task adds a byte-faithful file and verifies it against:

```yaml
expected_size_bytes: 18714
expected_sha256: 32c8030b432d9340286109e439f9ec0cc214c8e2c6b2e91ae40d640541d67753
```

## Boundary

This notice is not execution source and does not authorize repair, canonicalization, execution-source update, target workspace/material/write/build/regression work, Codex task generation, or paused-route resumption.
