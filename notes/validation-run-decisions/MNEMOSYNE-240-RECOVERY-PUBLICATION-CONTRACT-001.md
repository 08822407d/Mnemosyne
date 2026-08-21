# MNEMOSYNE-240 — Ubuntu-native recovery publication contract

```yaml
task_id: MNEMOSYNE-240
task_class: additive_successor_after_terminal_MNEMOSYNE_239_surface_block
base_commit: e726dea818dca9418181775d0e7dcd62eb6c464a
base_tree: de6474d8c4d75f9b445048129d862e190837f0a4
new_branch: mnemosyne-240-f2-g2a-and-handoff-audit-closeout
historical_branch_untouched: mnemosyne-235-f2-g2a-and-handoff-audit-closeout
failed_239_branch_expected_absent: mnemosyne-239-f2-g2a-and-handoff-audit-closeout
execution_surface: native_Ubuntu_24_04_with_VS_Code_Codex_extension_or_Codex_CLI
operator_manual_shell_required: false
surface_preflight_before_formal_start: required
formal_retry: false
cleanup: false
merge: false
G2A: false
A1: false
```

## Execution model

The operator downloads one self-contained Python zipapp. The agent locates it in `~/Downloads` or the current workspace, verifies its published SHA-256, reads the embedded task, and runs it with `python3 ... --auto`. The launcher creates all directories automatically.

Preflight verifies Linux/Ubuntu, embedded resources, Python, Git, Git identity, DNS, primary and validation refs, new-branch absence, related open PR absence, path-component/full-path support and authenticated dry-run push. A failed preflight does not start or consume the formal task. Once the launcher writes the formal-start marker, the embedded executor runs exactly once.

Phase A uses only the embedded manifest and payload ZIP, creates one verified commit and performs one non-force push. It does not use `gh`, the Git object API or Contents API and does not create the PR. The originating Pro conversation performs Phase B after exact live readback.

MNEMOSYNE-235 through 239 remain closed and are not retried. Their branches/objects are not reused or cleaned. No command, active guard, execution source, validation repository, Meta-Agent or real target is modified. No HVAL fixture is published or executed. No G2A or A1 is authorized.
