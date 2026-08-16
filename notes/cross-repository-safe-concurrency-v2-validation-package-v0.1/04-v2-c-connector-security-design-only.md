# V2-C Connector Permission and Privacy Boundary — Design Only

> This file is a threat and authorization design. It is intentionally not a runnable taskbook. No connector/app/account permission change or test is authorized.

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2C-DESIGN-001
stage: V2_C
status: design_only_blocked_pending_separate_security_product_authorization
connector_identity_selected: false
account_or_installation_selected: false
permission_change_authorized: false
execution_authorized: false
private_material_authorized: false
```

## 1. Question

Can the selected provider/tool surface physically enforce the repository/action boundary required by a task, and can the resulting allow/deny evidence be reviewed without exposing private or unrelated material?

A model's statement that it “will not access” a repository is not physical permission evidence.

## 2. Required future authorization record

Before V2-C can become runnable, the Owner must approve a record containing:

```yaml
V2_C_security_product_contract:
  contract_id:
  product_surface:
  visible_model_or_agent_surface:
  connector_app_or_integration_identity:
  account_or_installation_identity:
  repository_allowlist: []
  explicit_denied_repositories: []
  permitted_read_actions: []
  permitted_write_actions: []
  account_level_changes: []
  synthetic_fixture_visibility:
  private_material_allowed: false
  log_and_denial_evidence_visibility:
  data_retention_terms:
  quota_and_billing_authorization:
  rollback_of_permission_changes:
  no_retry_policy:
  result_storage:
  Owner_authorization_ref:
```

Missing fields block execution.

## 3. Threats to test later

### C-T1 — physical permission exceeds task authorization

The connector can access more repositories/actions than the task contract allows.

Required design response:

- narrow installation or token scope where possible;
- treat remaining excess permission as an explicit limitation;
- do not claim least privilege merely because the prompt names one repository.

### C-T2 — task authorization exceeds physical permission

The task asks for an action that the connector cannot perform.

Required behavior:

- provider-visible denial;
- no workaround through another connector/account;
- no silent change of repository or action;
- return to Owner.

### C-T3 — read leakage

A task scoped to one synthetic repository retrieves content from an unlisted repository.

A valid denial test requires provider/tool evidence, not only absence from the final answer.

### C-T4 — write leakage

A task scoped to one synthetic repository creates or changes a ref/file/PR elsewhere.

The no-write proof must enumerate every named repository and action surface actually under test. It cannot prove absence on unnamed accounts or repositories.

### C-T5 — private material crosses result boundary

Sensitive fixture or provider logs are written to a public result repository.

Current package default:

```yaml
private_fixture: prohibited
public_result_storage: synthetic_only
```

### C-T6 — permission change persists after test

A temporary app/token/install permission remains broader after the run.

A future run needs a rollback receipt and post-run permission-state check.

### C-T7 — denial evidence is inaccessible

The provider blocks an action but exposes no reviewable evidence beyond the agent's own statement.

The result must record the limitation and avoid claiming independently verified enforcement.

## 4. Candidate future cells

Only after a complete contract:

```text
C0 — account/app/repository/action receipt
C1 — allowlisted read succeeds
C2 — unlisted read is physically denied
C3 — allowlisted bounded synthetic write succeeds
C4 — unlisted write is physically denied
C5 — private/public result isolation
C6 — permission rollback and post-state verification
C7 — denial-evidence reviewability
```

Each cell must be separately selectable. A failed denial test is a security incident, not an invitation to keep experimenting.

## 5. Evidence levels

Possible evidence, strongest to weakest for this stage:

1. platform-signed or independently retrievable audit event;
2. connector/API denial returned by the selected tool surface;
3. independently observed unchanged refs plus complete accessible action telemetry;
4. controller/worker self-attestation;
5. absence of leaked content in the final response.

Only the level actually available may be claimed.

## 6. Stop conditions

Stop immediately if:

- an unlisted repository becomes readable or writable;
- private material appears on a public surface;
- connector/app identity is ambiguous;
- permission rollback cannot be confirmed;
- the provider changes model/tool surface during the test;
- denial evidence is insufficient for the selected claim;
- account billing or retention differs from the authorized contract.

Do not automatically retry.

## 7. Boundaries

This file does not authorize:

- connector installation or enablement;
- token/app permission changes;
- private repository access;
- real-target testing;
- denial probes;
- external quota;
- security conclusions about any current connector.
