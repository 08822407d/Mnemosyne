# Run Scope and Owner Decision Gate

```yaml
package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
file_role: pre_execution_owner_decision
status: prepared_unanswered
```

## 1. No implicit run authorization

Candidate v0.2, validation v0.2 and this package are prepared artifacts only. No validation repository, branch, fixture, scenario, model run, quota use or result ingestion is authorized until the Owner explicitly answers the decisions below.

## 2. Required decisions before V0

### D1 — Validation repository/store

Select one:

- create a new temporary public/synthetic GitHub repository;
- use another named temporary store whose version/diff evidence is mechanically available;
- revise/defer/stop.

Required fields:

```yaml
validation_repository_decision:
  disposition: RUN | REVISE | DEFER | STOP
  repository_or_store:
  visibility:
  creation_authorized: true | false
  repository_write_authorized: true | false
  allowed_paths_or_scope:
  prohibited_repositories:
    - 08822407d/Mnemosyne
    - Meta_Agent_repository
    - real_business_targets
```

A public repository may contain only public/synthetic material. No credentials may be committed under any visibility.

### D2 — Execution surface and visible selection

Record exactly what the Owner selects at execution time:

```yaml
execution_surface_decision:
  product_surface:
  visible_model_or_mode_verbatim:
  reasoning_setting_verbatim:
  exact_backend_status: unknown_or_not_attestable
```

Do not normalize or infer the backend unless an exact-request provider-attested field and contract exist.

### D3 — Phase authorization

Select one:

- `V0_ONLY` — repository/material/identity/no-write sentinel; no substantive scenario;
- `V0_THEN_STOP_FOR_REVIEW` — equivalent explicit wording;
- `V0_AND_V1_IF_V0_PASSES` — only if the Owner intentionally pre-authorizes both phases;
- `REVISE_PACKAGE`;
- `DEFER`;
- `STOP`.

Default is `V0_ONLY`.

### D4 — Tool and network boundary

State whether the executor may use:

- GitHub read/write actions on the synthetic repository;
- local code execution for mechanical checks;
- web access;
- other connected applications.

Recommended V1 default:

- synthetic GitHub repository read/write: allowed within exact scope;
- local/mechanical tools: allowed;
- web/research: prohibited as unnecessary;
- other apps/connectors: prohibited.

### D5 — Quota and paid execution

```yaml
quota_decision:
  paid_or_external_quota_authorized: true | false
  exact_surface_or_budget:
```

Default is `false`.

### D6 — Result storage and ingestion

Choose where raw run outputs live and whether a later reviewed summary may be written to Mnemosyne.

Preparation of this package does not authorize raw output ingestion. Before any Mnemosyne write, a later task must review:

- material class;
- repository visibility;
- exact file identities;
- provenance completeness;
- whether raw outputs contain unsafe or unnecessary content;
- which summary/result paths are allowed.

### D7 — Retention and cleanup

Record:

- who owns the temporary repository;
- how long it should be retained;
- whether branches may be deleted after results are preserved;
- whether the repository itself may be archived/deleted;
- which artifact identities must survive cleanup.

## 3. Required authorization object

A valid run decision should provide or be normalized into:

```yaml
validation_run_authorization:
  package_id: MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002
  candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
  validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
  disposition:
  phase_scope:
  repository_or_store:
  visibility:
  product_surface:
  visible_selection_verbatim:
  allowed_actions: []
  prohibited_actions: []
  material_class: public_synthetic_only
  quota_authorized:
  output_location:
  retention_plan:
  decision_ref:
  expires_with_run: true
  not_future_precedent: true
```

If any required field affecting repository, material safety, write authority or phase scope is unknown, return `BLOCKED_MISSING_OWNER_DECISION` and do not create the repository or run V0.

## 4. Decisions not bundled with validation

Even a complete V0/V1 authorization does not authorize:

- candidate adoption;
- Meta-Agent modification/activation;
- business-target modification;
- private material ingestion;
- execution-source change;
- backup provider configuration for real targets;
- PR/merge in Mnemosyne;
- Deep Research/Fable.
