---
guard_id: META-AGENT-MNEMOSYNE-GUIDANCE-COMPATIBILITY-001
artifact_role: retired_process_compatibility_guard_pointer
status: retired_after_dedicated_repository_cutover
active_guard: false
target_project_id: meta-agent
target_truth_source: false
last_updated_by_task: MNEMOSYNE-META-AGENT-SOURCE-RETIREMENT-001

cutover:
  repository: 08822407d/Meta-Agent
  PR: 3
  merge_commit: eb71ed350e7cf1783d73580466a3656fad2a3b69

Mnemosyne_guidance_loaded_by_default_for_Meta_Agent: false
Meta_Agent_owned_behavior_guidance_adopted: false

historical_original:
  repository: 08822407d/Mnemosyne
  commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
  path: target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md
---

# Meta-Agent — Retired Mnemosyne Guidance Compatibility Pointer

The temporary Mnemosyne-guidance compatibility layer is retired after the dedicated-repository cutover.

Mnemosyne maintenance guidance is no longer Meta-Agent behavior authority, product authority, current-state authority, or a default load dependency. Meta-Agent conversations must not automatically run the former augmented Mnemosyne guidance command or import Mnemosyne maintenance routes.

This retirement does not create or adopt new Meta-Agent-owned behavior guidance. Any future Meta-Agent behavior-guidance package requires its own target-scoped Owner decision and validation in `08822407d/Meta-Agent`.

The complete former compatibility guard remains recoverable as historical process evidence at:

```text
08822407d/Mnemosyne@8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb:
target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md
```

The historical guard must not be reactivated implicitly. A rollback affecting process authority requires a separate explicit Owner decision.
