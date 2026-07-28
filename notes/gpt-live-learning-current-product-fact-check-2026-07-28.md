# GPT Live Learning — Current Product Fact Check (2026-07-28)

> Time-sensitive, non-execution-source product fact check for the later GPT Live learning research route. This file does not configure GPT Live, attest the exact backend of any user session, approve a knowledge base, or substitute for pedagogical evidence.

```yaml
fact_check_id: GPT-LIVE-LEARNING-PRODUCT-FACT-CHECK-2026-07-28
created_by_task: MNEMOSYNE-168
checked_at: 2026-07-28
source_policy: official_OpenAI_sources_only
status: current_snapshot_requires_future_recheck
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Current official product identity

OpenAI announced GPT-Live on 2026-07-08 as a new generation of full-duplex voice models powering ChatGPT Voice.

```yaml
product:
  family: GPT-Live
  paid_default: GPT-Live-1
  free_default: GPT-Live-1_mini
  interaction_architecture: full_duplex_continuous_interaction
  availability_surface:
    - ChatGPT.com
    - iOS
    - Android
  rollout_and_account_variation: possible
```

Primary official source:

- https://openai.com/index/introducing-gpt-live/

## 2. Relationship to GPT-5.5

The user's earlier statement that GPT Live was described as having GPT-5.5-level intelligence was directionally grounded in the launch material, but the current architecture is more specific than a one-model equivalence claim.

OpenAI states that:

- GPT-Live handles continuous interaction;
- deeper search, reasoning or agentic work can be delegated to a frontier model behind the scenes;
- at launch, GPT-Live uses GPT-5.5 in the background;
- GPT-Live-1 Instant and mini use GPT-5.5 Instant in the background;
- GPT-Live-1 Medium and High use GPT-5.5 Thinking with medium or high reasoning effort.

```yaml
interpretation:
  valid_operator_summary: GPT_Live_can_draw_on_GPT_5_5_at_launch
  invalid_overstatement: every_voice_turn_is_directly_and_uniformly_generated_by_one_GPT_5_5_backend
  exact_backend_for_a_specific_session: unknown_or_not_attestable_without_provider_metadata
  future_model_mapping: explicitly_subject_to_change
```

The learning design should therefore record the visible `Instant | Medium | High` selection and observed behavior, but not treat that as exact-request backend attestation.

Primary official source:

- https://openai.com/index/introducing-gpt-live/

## 3. Interaction capabilities relevant to learning

Officially documented current capabilities include:

```yaml
interaction_capabilities:
  simultaneous_listen_and_speak: true
  interruption_and_barge_in: supported_with_environmental_limitations
  wait_while_user_thinks: requestable_not_infallible
  web_search: supported
  memory: supported
  text_in_same_chat: supported
  images_in_same_chat: supported_when_available_for_account
  visual_widgets: supported_for_selected_results
  manual_supported_file_attachment: account_dependent_possible
  find_or_add_files_from_ChatGPT_Library: not_currently_supported
  connected_apps_or_plugins: not_initially_supported
  video: not_supported_at_launch_in_Live
  screen_sharing: not_supported_at_launch_in_Live
```

Learning implications:

- formula-heavy or diagram-heavy explanations can move into text or images in the same chat;
- web search and memory can support a learning session, but their exact authority and evidence role still need explicit design;
- a persistent course knowledge base cannot be assumed to be automatically available through connected apps or the ChatGPT Library;
- manual file attachment may be usable, but must be tested on the actual account and surface;
- interruption, overlapping speech, background noise and long pauses can still cause recognition or turn-taking errors.

Official source:

- https://help.openai.com/en/articles/20001274

## 4. Behavior and response-style controls

Current official documentation states:

- preset ChatGPT personalities do not currently apply to Live;
- the user can ask Live to change tone, pace or response style within an individual conversation;
- precise playback-speed controls are not currently available;
- where available, `Instant`, `Medium` and `High` intelligence levels can be selected under Voice settings;
- higher intelligence levels may respond more slowly, especially when web search is used.

```yaml
learning_configuration_implication:
  preset_personality_as_primary_behavior_contract: unsupported
  session_level_instruction_for_tone_pace_and_style: supported
  persistent_course_behavior_contract: requires_separate_product_and_project_testing
  reasoning_level_selection: available_account_dependent
  one_setting_for_all_learning_subtasks: not_recommended_without_evidence
```

This reinforces the need to separate:

1. persistent project/course guidance;
2. session-local teaching mode;
3. current explanation action;
4. reasoning-level escalation for difficult subproblems.

Official source:

- https://help.openai.com/en/articles/20001274

## 5. Conversation continuity and duration

Voice operates inside a ChatGPT chat. The user can follow spoken responses in text, type in the same conversation and review prior messages without starting over.

Current official documentation also states that a single Live conversation can last up to two hours. Usage limits otherwise depend on plan and can change.

```yaml
continuity_implication:
  chat_transcript_available: true
  spoken_and_typed_turns_can_share_one_chat: true
  two_hour_single_session_cap: current_official_fact
  long_term_course_continuity: must_not_rely_on_one_voice_session
  cross_session_learning_state: requires_explicit_memory_and_handoff_design
```

Official source:

- https://help.openai.com/en/articles/20001274

## 6. Privacy and retention facts relevant to learning records

OpenAI currently states:

- audio clips from Live and Advanced Voice are stored with the transcript in chat history;
- clips are retained for 30 days;
- deleting the chat causes associated clips to be deleted within 30 days, subject to stated legal/safety exceptions and previously disassociated training data;
- archiving only removes the chat from the sidebar and does not delete the chat or associated clips;
- audio/video clips are not used for training unless the user chooses to share them;
- transcripts and other files may be used according to plan and data-control settings.

```yaml
learning_privacy_implication:
  voice_transcript_as_unquestioned_ground_truth: prohibited_candidate_principle
  retain_sensitive_learner_state_by_default: not_supported
  archive_equals_delete: false
  chat_deletion_irreversible: true
  user_data_controls_and_plan: must_be_checked_before_any_real_learning_pilot
```

Official source:

- https://help.openai.com/en/articles/20001274

## 7. Facts not yet established for the planned learning system

The official sources reviewed here do not establish all of the following for the user's intended workflow:

```yaml
unresolved_product_questions:
  - exact_project_instructions_behavior_in_Live_for_the_user_account
  - whether_a_selected_Project_knowledge_set_is_consistently_available_during_Live
  - how_memory_items_are_selected_and_injected_during_learning_dialogue
  - reliable_access_to_course_files_across_sessions
  - continuity_between_Live_and_text_when_switching_surfaces_or_devices
  - how_reasoning_delegation_affects_latency_and_turn_management_in_teaching
  - whether_math_notation_recognition_is_adequate_for_the_target_courses
  - how_voice_transcription_errors_are_exposed_and_corrected
  - whether_configured_learning_behavior_remains_stable_across_long_sessions
```

These require account-specific observation and controlled tests, not inference from the launch announcement.

## 8. Research-design consequences

The later GPT Live learning research should not begin with a single monolithic “system prompt.” It should distinguish:

```yaml
configuration_layers:
  course_or_project_authority:
  learning_session_goal_and_topic:
  teaching_mode:
  local_learner_state_and_uncertainty:
  current_explanation_action:
  voice_turn_management:
  text_visual_handoff_rule:
  persistence_and_privacy_policy:
  evaluation_and_stop_conditions:
```

Recommended comparison conditions:

- unconfigured Live versus bounded learning configuration;
- Instant versus Medium/High for selected task classes;
- voice-only versus voice plus text/visual handoff;
- generic “explain simply” versus adaptive local-prerequisite policy;
- no persistent learner evidence versus explicitly scoped evidence ledger;
- transcript-only state versus transcript plus user-confirmed correction.

No comparison should infer the exact served backend from latency or output quality.

## 9. Snapshot boundary

```yaml
snapshot_boundary:
  facts_current_as_of: 2026-07-28
  official_sources:
    - https://openai.com/index/introducing-gpt-live/
    - https://help.openai.com/en/articles/20001274
    - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
  recheck_required_before:
    - generating_a_product_specific_Deep_Research_prompt
    - configuring_a_real_learning_project
    - relying_on_files_apps_plugins_video_or_screen_sharing
    - recording_usage_limit_or_model_mapping_as_current_fact
    - starting_a_real_user_data_pilot
```

## 10. Boundaries

- This fact check does not attest a specific GPT Live session's backend.
- It does not approve GPT Live as an effective tutor.
- It does not establish that GPT-5.5-level reasoning is continuously available in every turn.
- It does not configure a Project, memory, file set or persistent knowledge base.
- It does not authorize storage of voice transcripts or learner evidence.
- It does not replace empirical learning-effectiveness evaluation.
