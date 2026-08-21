# MNEMOSYNE-239 Execution-Surface Pro Adjudication 001

```yaml
adjudication_id: MNE-MNEMOSYNE-239-EXECUTION-SURFACE-PRO-ADJUDICATION-001
source_task: MNEMOSYNE-239
formal_disposition: BLOCKED_CLOSED_NO_RETRY
substantive_publication_set_invalidated: false
payload_identity_invalidated: false
selected_successor: MNEMOSYNE-240
selected_surface: native_Ubuntu_24_04_local_Git
G2A_issued: false
A1_execution_authorized: false
```

## Findings

1. Remote-ref, validation-ref, clone, local-branch, Git identity and pre-materialization manifest checks passed.
2. The first materialization attempt failed on Windows at `git add` with `Filename too long` for a valid manifest path.
3. No commit, push, remote branch or PR was created.
4. The result does not authorize rerunning task ID 239. A new additive successor is required.
5. Native Ubuntu 24.04 removes the observed Windows full-path ceiling while preserving local deterministic Git, exact bytes, one commit, one non-force push and post-push readback.

## Successor requirements

MNEMOSYNE-240 must automatically locate its single operator package, create a fresh short Linux run root, perform a non-mutating surface preflight, and only after that preflight passes start the one-shot formal execution. The operator must not be asked to create directories or run shell commands manually. PR creation remains a separate originating-conversation Phase B after exact branch readback.
