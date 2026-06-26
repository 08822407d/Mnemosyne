# MNEMOSYNE-056 Result Record

```yaml
task_id: MNEMOSYNE-056
task_name: Target-project workspace boundary and layout proposal
started_from_latest_master: user_task_premise_says_fresh_latest_master; remote_head_not_independently_verified
user_input_summary: >-
  Preserve the user's structural design concern as candidate design input: target-project content stored inside the Mnemosyne repository should be treated as an intentional first-class target-project workspace pattern, not merely a Codex Cloud workaround. Create a non-execution-source proposal, update current state/handoff references, and preserve no-target/no-material/no-write boundaries.
files_intended_to_edit:
  - notes/target-project-workspace-boundary-and-layout-proposal.md
  - notes/codex-task-results/MNEMOSYNE-056-result.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_actually_edited:
  - notes/target-project-workspace-boundary-and-layout-proposal.md
  - notes/codex-task-results/MNEMOSYNE-056-result.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_created:
  - notes/target-project-workspace-boundary-and-layout-proposal.md
  - notes/codex-task-results/MNEMOSYNE-056-result.md
files_modified:
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_not_modified:
  - current/human-approved-spec.md
  - raw/research-reports/**
  - raw/user-design-restatements/**
  - manual-import-inbox/**
  - AGENTS.md
  - CLAUDE.md
  - .github/workflows/**
  - automation scripts
proposal_summary:
  - Created a candidate non-execution-source proposal for a three-layer boundary: Mnemosyne global layer, target-project workspace layer inside Mnemosyne repo, and target project runtime truth source/external repository.
  - Proposed `target-projects/` as a first-class long-lived workspace root, not a temporary inbox, not Mnemosyne execution source, and not automatically the target runtime truth source.
  - Proposed a target directory layout separating project meta, user input, Mnemosyne design workbench, delivery package, dry-runs, and feedback/lessons.
  - Marked user originals/raw requirements/restatements placement as candidate and requiring user confirmation.
  - Documented feedback-to-Mnemosyne lesson boundaries and labels for example citations.
execution_source_modified: false
target_workspace_created: false
target_project_selected: false
target_materials_ingested: false
target_repository_written: false
open_questions_added:
  - Whether `target-projects/` should become the standard workspace root.
  - Whether target-specific Mnemosyne-generated intermediate work should live under each target workspace instead of global notes.
  - Where user originals, raw requirements, restatements, redactions, and user decisions should live.
  - How Mnemosyne-global lessons should cite target-specific examples without promoting target-specific design into global policy.
  - Whether future dry-run folder conventions should migrate to target-scoped workspace paths after user approval.
protected_file_check: passed_no_output
verification_commands_and_outputs:
  - command: git status --short
    output: |
      M current/active-context.md
      M current/open-questions.md
      M current/todo.md
      M handoff/handoff-current.md
      ?? notes/target-project-workspace-boundary-and-layout-proposal.md
  - command: git diff HEAD --stat
    output: |
      current/active-context.md  |  4 ++++
      current/open-questions.md  | 14 ++++++++++++++
      current/todo.md            |  2 ++
      handoff/handoff-current.md | 11 +++++++----
      4 files changed, 27 insertions(+), 4 deletions(-)
      Note: initial pre-staging check; final staged self-check includes created files.
  - command: git diff HEAD --name-only
    output: |
      current/active-context.md
      current/open-questions.md
      current/todo.md
      handoff/handoff-current.md
      Note: initial pre-staging check; final staged self-check includes created files.
  - command: git diff HEAD -- targeted files
    output: |
      Targeted diff showed expected updates to current/active-context.md, current/todo.md, current/open-questions.md, and handoff/handoff-current.md. The untracked proposal/result files are represented by git status until staged.
  - command: grep -n "Target-Project Workspace Boundary and Layout Proposal" notes/target-project-workspace-boundary-and-layout-proposal.md
    output: |
      1:# Target-Project Workspace Boundary and Layout Proposal
  - command: grep -n "target-projects/" notes/target-project-workspace-boundary-and-layout-proposal.md current/open-questions.md current/todo.md
    output: |
      notes/target-project-workspace-boundary-and-layout-proposal.md:53:target-projects/
      notes/target-project-workspace-boundary-and-layout-proposal.md:58:- `target-projects/` is a first-class long-lived workspace root for target projects handled by Mnemosyne.
      notes/target-project-workspace-boundary-and-layout-proposal.md:70:target-projects/<target_project_id>/
      notes/target-project-workspace-boundary-and-layout-proposal.md:116:This task does not create `target-projects/` or any real target-project directory. The layout above is only a proposal in a code block.
      notes/target-project-workspace-boundary-and-layout-proposal.md:124:- Put target-specific user input under `target-projects/<target_project_id>/01-user-input/`.
      notes/target-project-workspace-boundary-and-layout-proposal.md:169:3. decision on whether `target-projects/` becomes the standard root;
      current/open-questions.md:40:- Should `target-projects/` become the standard root for all target-project workspaces inside the Mnemosyne repository?
      current/open-questions.md:48:- Should future first-target dry-run folder conventions move from `notes/target-project-dry-runs/<dry_run_id>/` to `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/` after user approval?
  - command: grep -n "MNEMOSYNE-056" current/active-context.md current/todo.md current/open-questions.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-056-result.md
    output: |
      current/active-context.md:34:- MNEMOSYNE-056: target-project workspace boundary/layout proposal created as non-execution-source candidate design; no target project selected, no target materials ingested, no target repository written, and execution source unchanged.
      current/todo.md:45:- MNEMOSYNE-056: created target-project workspace boundary/layout proposal as non-execution-source candidate design; no target selected, no target materials ingested, no target repository written, and execution source unchanged.
      current/open-questions.md:38:## MNEMOSYNE-056 target-project workspace boundary questions
      current/open-questions.md:43:  - status: candidate_recommendation_from_MNEMOSYNE-056
      current/open-questions.md:47:  - status: candidate_recommendation_from_MNEMOSYNE-056
      handoff/handoff-current.md:22:- MNEMOSYNE-056 created a non-execution-source proposal for target-project workspace boundaries and layout. It treats target-project content inside the Mnemosyne repo as an intentional workspace pattern, not merely a Codex Cloud workaround. User must still approve/revise it before first real target-project dry-run.
      handoff/handoff-current.md:74:- MNEMOSYNE-056: target-project workspace boundary/layout proposal created as non-execution-source candidate design; no target project selected, no target materials ingested, no target repository written, and execution source unchanged.
      notes/codex-task-results/MNEMOSYNE-056-result.md:1:# MNEMOSYNE-056 Result Record
      notes/codex-task-results/MNEMOSYNE-056-result.md:4:task_id: MNEMOSYNE-056
  - command: grep -n "not merely a Codex Cloud workaround" notes/target-project-workspace-boundary-and-layout-proposal.md handoff/handoff-current.md || true
    output: |
      notes/target-project-workspace-boundary-and-layout-proposal.md:7:positioning: target-project content stored in Mnemosyne repo is an intentional workspace pattern, not merely a Codex Cloud workaround
      notes/target-project-workspace-boundary-and-layout-proposal.md:18:This proposal therefore treats target-project content stored inside the Mnemosyne repository as a first-class, intentional target-project workspace pattern. It should be understood as a normal Mnemosyne design-factory and design-archive pattern, not merely a Codex Cloud workaround or temporary compromise for current attachment/write limitations.
      handoff/handoff-current.md:22:- MNEMOSYNE-056 created a non-execution-source proposal for target-project workspace boundaries and layout. It treats target-project content inside the Mnemosyne repo as an intentional workspace pattern, not merely a Codex Cloud workaround. User must still approve/revise it before first real target-project dry-run.
  - command: grep -n "No real target-project dry-run has occurred" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:41:- No real target-project dry-run has occurred.
      current/todo.md:22:- No real target-project dry-run has occurred.
      handoff/handoff-current.md:25:- No real target-project dry-run has occurred.
  - command: grep -n "No target project has been selected" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:42:- No target project has been selected.
      current/todo.md:24:- No target project has been selected.
      handoff/handoff-current.md:26:- No target project has been selected.
  - command: grep -n "No target materials" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:43:- No target materials have been uploaded/ingested.
      current/todo.md:25:- No target materials have been uploaded/ingested.
  - command: grep -n "No target.*repository.*written" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:44:- No target repository has been written.
      current/todo.md:26:- No target-project repository has been written.
      handoff/handoff-current.md:28:- No target-project repository has been written.
  - command: find target-projects -maxdepth 2 -type f -print 2>/dev/null || true
    output: |
      (no output)
  - command: git diff HEAD --name-only | grep -E '^(current/human-approved-spec\.md$|raw/research-reports/|raw/user-design-restatements/|manual-import-inbox/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
    output: |
      (no output)
  - command: git status --short
    output_after_result_record_written: |
      M  current/active-context.md
      M  current/open-questions.md
      M  current/todo.md
      M  handoff/handoff-current.md
      A  notes/codex-task-results/MNEMOSYNE-056-result.md
      A  notes/target-project-workspace-boundary-and-layout-proposal.md
  - command: git diff HEAD --name-only
    output_after_result_record_written: |
      current/active-context.md
      current/open-questions.md
      current/todo.md
      handoff/handoff-current.md
      notes/codex-task-results/MNEMOSYNE-056-result.md
      notes/target-project-workspace-boundary-and-layout-proposal.md
known_gaps:
  - This is a proposal only; user must decide whether/how to promote it.
  - User originals/raw requirements/restatements placement remains unresolved by design.
  - The result does not independently verify remote latest master beyond the task premise.
manual_review_required:
  - User must review, approve, revise, or reject the proposed target-project workspace boundary/layout before the first real target-project dry-run.
  - User must decide whether `target-projects/` becomes the standard root.
  - User must decide the policy for originals, raw requirements, restatements, redactions, and target-specific user decisions.
completion_claim: >-
  MNEMOSYNE-056 created the requested non-execution-source target-project workspace boundary/layout proposal, updated current state and handoff files, did not modify current/human-approved-spec.md, did not create a real target-project workspace directory, did not select a target project, did not ingest target material, and did not write any target repository.
```
