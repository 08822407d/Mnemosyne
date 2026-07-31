# Inline Operator-Flow Delivery Amendment Record

```yaml
record_id: MNEMOSYNE-INLINE-OPERATOR-FLOW-AMENDMENT-001
created_by_task: MNEMOSYNE-185
status: proposed_active_on_merge
execution_source_modified: false
source_guard: current/artifact-delivery-and-direct-generation-guard.md
load_command: commands/load-mnemosyne-guidance.md
```

## 1. User-reported problem

The repository-first Fable5 delivery design correctly stored task prompts, operator guides and input manifests, but the user still had to find and open repository files to learn the operating procedure. This was unnecessarily inconvenient and conflicted with the intended separation of visible user operations from supporting artifacts.

## 2. Adopted interpretation

For any cross-conversation or external-Agent task, two deliverables are distinct and both are required:

```yaml
canonical_transfer_artifact:
  role: preserve_the_complete_long_task_and_machine_reusable_structure
  preferred_form: repository_file_or_verified_downloadable_file

same_response_operator_flow:
  role: let_the_user_execute_without_repository_browsing
  required_location: the_design_or_launch_conversation_response
```

A repository `OPERATOR.md` remains useful for auditability and later reuse. It cannot be the only place where the user learns what to do.

## 3. Minimum visible operator flow

The design or launch response must state, as applicable:

1. whether a PR must be reviewed or merged before execution;
2. the exact conversation/Project/product surface to open;
3. visible model, mode, effort or Research setting where selected;
4. clean-context, memory, connector and contamination requirements;
5. exact files, folders, links or downloadable artifacts;
6. preflight steps and expected receipt;
7. the launch instruction or direct downloadable task file;
8. return artifacts and return destination;
9. stop/fallback rules and prohibited actions;
10. whether multiple tasks require separate contexts.

## 4. Scope

The rule applies to:

- Pro and Deep Research tasks;
- Fable tasks;
- Codex tasks;
- new ChatGPT conversation prompts and handoffs;
- cross-model reviews, validations, replays and adjudications;
- future equivalent external-Agent packages.

It does not require duplicating a long task body inline. A verified downloadable file may carry the full prompt while the response carries the complete operating procedure and concise scope.

## 5. Authority and activation

The user's current instruction is direct task-local authority for this conversation. Repository-wide behavior-guard activation occurs only after the canonical MNEMOSYNE-185 PR is reviewed and merged.

No execution-source change is required because the existing execution source already requires visible separation of user operations; this amendment makes the artifact-delivery behavior operationally explicit.

## 6. Validation posture

This change is directly exercised in the MNEMOSYNE-185 final response by:

- presenting both Fable5 operator flows inline;
- providing the long research-task bodies as verified downloadable Markdown files;
- preserving repository paths as supporting references rather than requiring repository browsing.

A later broad behavioral campaign is not required before using this low-risk usability correction. Any recurrence should reopen validation of task-delivery compliance.
