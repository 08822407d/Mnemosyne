# Meta-Agent Mechanical Inventory — Codex Startup Prompt

> Run only after the Mnemosyne PR that adds this prompt is merged.

```text
In OpenAI Codex Code mode, connect/select repository:

08822407d/Mnemosyne

Read and execute exactly:

handoff/meta-agent-dedicated-repository-mechanical-inventory-codex-task.md

Task ID:
META-AGENT-DEDICATED-REPOSITORY-MECHANICAL-INVENTORY-001

This is the mechanical E0 prerequisite for migration mapping. Use a full Git checkout and terminal. Do not use ChatGPT GitHub code search as a substitute for recursive Git object enumeration.

At execution time, re-pin latest `master`; it must contain PR #256 merge commit
5bb586c057c228fbb80e37529ed1245e7366f482
as an ancestor or be identical.

Generate the complete recursive tree/blob inventory, deterministic content identities, front-matter extraction, preliminary path-rule classification, closure receipt, reproducibility evidence, one bounded Mnemosyne branch and at most one PR.

Strictly prohibit:
- every write to 08822407d/Meta-Agent;
- target-truth, active-context, handoff, authority, methodology, case or history modification;
- destination initialization, shadow copy or cutover;
- final semantic migration disposition;
- private material;
- a PASS result without complete tree/blob closure.

If full Git-object evidence is unavailable, return
BLOCKED_MECHANICAL_INVENTORY_INCOMPLETE
without creating a misleading PR.

After creating and finalizing the one Mnemosyne PR, stop and return:
- source commit;
- root subtree SHA;
- tree/blob counts;
- manifest paths and hashes;
- preliminary unknown/material-review counts;
- PR number and final head;
- confirmation of zero destination writes.
```
