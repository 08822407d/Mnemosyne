# FABLE5-GREENFIELD-001 Incident 001 — GF-STEP-2A safety routing and successful retry

```yaml
incident_id: FABLE5-GREENFIELD-001-INCIDENT-001
date: 2026-07-11
track_id: FABLE5-GREENFIELD-001
affected_step: GF-STEP-2A
record_type: provider_safety_routing_observation
authority_level: non_execution_source_operational_evidence
status: resolved_by_revised_fresh_conversation_retry
substantive_finding_status: not_reviewed
```

## 1. What was observed

During the first GF-STEP-2A attempt, the Claude/Fable web interface visibly changed the selected model from Fable 5 to Opus 4.8 and displayed an `Edit and retry with Fable 5` option.

The initial attempt had already read the three pinned repository sources and had produced substantial intermediate text before the routing event. No downloadable STEP2A artifact was delivered from that interrupted trajectory.

The user also observed that the long pasted task appeared as a non-editable `PASTED` block. The available edit UI exposed only a separate GitHub URL field, so the original long task could not be safely edited in place. A fresh conversation was therefore used for the revised task.

## 2. Evidence preserved

- Initial attempt identifier:
  - `step_id: GF-STEP-2A`
  - `step_name: capability_evidence_source_map_and_original_report_read_plan`
- Visible UI labels, transcribed from user screenshots:
  - `Switched to Opus 4.8`
  - `Edit and retry with Fable 5`
  - `PASTED`
  - `Editing this message will create a new conversation branch.`
- Partial intermediate output before routing:
  - canonical path: `incidents/INC-001-partial-output-before-routing.txt`
  - source size: 12759 bytes
  - source SHA-256: `8559223430f030f4b84838ff2665310bfcab5a165a1fc54646193e532dfc2a04`
- User screenshot source hashes retained in this record for provenance; screenshot binaries were not copied into the public repository:
  - `image.png`: 6266 bytes, SHA-256 `c7c994c1d52ba5c128fb50e3816d9f909f5f74bf6d6c41fe091376fc1ce5ec85`
  - `QQ_1783763441065.png`: 40185 bytes, SHA-256 `af2088c1b2496042e4f967d081d1ea6f8c4fc899239f6831e9976e6b4dc07704`

## 3. Classification limits

The exact Anthropic classifier category, rule, threshold, and routing rationale are unknown. This record does **not** assert that:

- the task was malicious or dangerous;
- any specific word caused the route;
- the request matched cybersecurity, biology, chemistry, distillation, or another named safeguard category;
- the partial output itself triggered the switch;
- the account or project received a persistent safety flag.

Public reporting in June–July 2026 states that Fable 5 may route some safeguarded requests to Opus 4.8 and that benign requests can be affected. No official Anthropic page describing the exact classifier behavior or thresholds was found during the maintainer web check. These external reports are corroborating context only, not proof of this incident's trigger.

## 4. Recovery action

A revised STEP2A prompt was run in a fresh Fable 5 conversation with:

- Research mode off;
- the same three pinned repository paths and expected blob SHAs;
- a narrower description centered on research evidence cataloging and staged report reading;
- explicit exclusion of model/service evaluation, final capability conclusions, architecture design, external research, and repository writes.

The revised task completed successfully under Fable 5 and produced:

- `steps/GF-STEP-2A/00-revised-prompt-as-sent.md`
- `steps/GF-STEP-2A/01-fable-chat-summary.md`
- `steps/GF-STEP-2A/02-research-source-map.md`

## 5. Operational lessons

These are process observations, not claims about Anthropic's internal detector:

1. A provider routing event must be recorded separately from the task's substantive result.
2. An interrupted Opus-routed trajectory is not accepted as the Fable result when the track requires Fable authorship.
3. A revised fresh-conversation run may be used when the original pasted task is not editable.
4. The retry should clarify legitimate scope and reduce ambiguous framing; it must not ask the model to bypass, defeat, conceal from, or evade safety systems.
5. The exact task sources, SHAs, Research setting, and authored model must be restated in the successful run.
6. Partial output can be preserved as incident evidence, but it is not merged into the canonical successful deliverable.
7. Future Fable prompts should describe bounded document-processing work directly and avoid unnecessary global framing about extracting or comparing model capabilities when that is not required for the immediate substep.

## 6. Relationship to STEP2A result

- Interrupted first attempt:
  - status: `safety_routed_to_Opus_4_8_before_deliverable`
  - canonical STEP2A result: no
- Revised successful attempt:
  - status: `GF_STEP_2A_complete_source_map_ready_for_STEP2B`
  - canonical track artifact: yes, as non-execution-source advisory evidence
- Substantive maintainer acceptance of STEP2A's evidence map:
  - deferred until GPT Pro quota is restored, per user instruction

## 7. Boundary

This incident record is operational evidence only. It does not define Anthropic policy, diagnose a proprietary classifier, authorize safety-filter circumvention, accept or reject the STEP2A evidence map, modify execution source, generate repair work, create target-project artifacts, or resume/close the paused route.
