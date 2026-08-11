# Provider, Model and Product-Surface Capability Catalogue — Candidate v0.1

> Non-execution-source catalogue design for time-sensitive AI-provider capabilities, product settings and operating procedures. It is deliberately separate from `notes/reusable-agent-capability-catalog-v0.1.md`. This file does not assert that a current model, plan, price, quota, setting, Skill or connector capability exists unless a future entry cites current evidence.

```yaml
catalog_design_id: MNEMOSYNE-PROVIDER-PRODUCT-CAPABILITY-CATALOG-001
task_id: MNEMOSYNE-200
version: 0.1.0
status: schema_and_use_design_not_populated_current_fact_catalog
execution_source_modified: false
current_product_facts_verified_in_this_task: false
provider_or_plan_selection_authorized: false
```

## 1. Why this catalogue is separate

A portable Agent capability describes **what the Agent must be able to do**, for example:

- continue work across fresh conversations;
- preserve original requirements;
- distinguish truth, evidence and candidate ideas;
- stop and escalate on missing authority.

A provider/product capability describes **how a current product may implement or constrain that behavior**, for example:

- a Project or workspace memory setting;
- a file-upload limit;
- a connector’s read/write scope;
- a model’s supported context or tools;
- a Claude Skill, ChatGPT instruction surface or another packaging mechanism;
- quota, plan, privacy or export behavior.

Mixing these layers would turn current product behavior into permanent Agent law. The portable catalogue should survive provider changes; this catalogue is expected to change frequently.

## 2. Intended uses

The catalogue should help the user and Agent designers:

1. discover which subscribed products and visible model options are available for a task;
2. compare documented strengths, limits, tools and settings;
3. select an implementation surface for a portable Agent capability package;
4. record exact operating steps and recheck triggers;
5. avoid relying on human memory for product settings, quotas and UI behavior;
6. distinguish official facts, operator observations, task evidence and unverified claims.

It is not intended to rank models by vague overall intelligence or infer hidden backend identity from style, speed or self-report.

## 3. Record types

### 3.1 Provider/product surface record

```yaml
product_surface_record:
  record_id:
  provider:
  product:
  plan_or_subscription:
  surface:
    web | desktop | mobile | CLI | API | coding_agent | research | other
  region_or_account_scope:
  observed_or_verified_at:
  official_source_refs: []
  operator_observation_refs: []
  freshness:
    time_sensitive: true
    recheck_before: []
  privacy_and_data_use_refs: []
  known_limitations: []
```

### 3.2 Visible model or mode record

```yaml
model_mode_record:
  record_id:
  provider:
  product_surface_ref:
  operator_visible_name_verbatim:
  provider_normalized_name:
  reasoning_or_effort_setting:
  documented_capabilities: []
  observed_task_capabilities: []
  observed_failures: []
  suitable_task_classes: []
  unsuitable_or_unverified_task_classes: []
  tool_access: []
  context_or_file_limits:
  quota_or_rate_limit:
  latency_or_cost_notes:
  exact_served_backend:
    status: unknown_or_not_attestable | provider_attested_for_exact_request
    evidence_refs: []
  verified_at:
  recheck_trigger:
```

A consumer UI name is preserved verbatim but does not attest the exact backend that served a particular response.

### 3.3 Setting or feature record

```yaml
setting_feature_record:
  record_id:
  provider:
  product_surface_ref:
  visible_setting_name:
  purpose:
  practical_effect:
  default_state:
  scope:
    account | project | conversation | task | device | repository | other
  setup_or_change_steps: []
  verification_steps: []
  persistence_behavior:
  privacy_or_sharing_effect:
  interaction_with_memory_files_apps_or_tools:
  rollback_or_disable_steps: []
  official_source_refs: []
  operator_observation_refs: []
  verified_at:
  recheck_trigger:
  limitations: []
```

### 3.4 Tool, connector or repository-action record

```yaml
tool_connector_record:
  record_id:
  provider:
  product_surface_ref:
  tool_or_connector:
  supported_actions: []
  unsupported_or_unverified_actions: []
  read_write_scope:
  authorization_layers:
    account_connection:
    app_or_repository_permission:
    per_chat_or_per_task_invocation:
    current_task_authority:
  sync_or_index_behavior:
  completeness_limits:
  audit_or_result_evidence:
  setup_steps: []
  verification_steps: []
  official_source_refs: []
  observed_at:
  recheck_trigger:
```

Persistent platform permission never substitutes for current task-local authority.

### 3.5 Skill, prompt or instruction-packaging record

```yaml
packaging_mechanism_record:
  record_id:
  provider:
  product_surface_ref:
  mechanism_name_verbatim:
  mechanism_type:
    system_instruction | project_instruction | skill | command | prompt | agent_config | other
  documented_purpose:
  loading_or_activation_model:
  applicable_scope:
  file_or_format_contract:
  precedence_and_conflict_behavior:
  tool_or_repository_access_relation:
  context_cost_or_retrieval_behavior:
  versioning_and_update_method:
  portability_limitations:
  security_or_injection_considerations: []
  official_source_refs: []
  verified_at:
  recheck_trigger:
```

A mechanism called “Skill” on one provider must not be assumed equivalent to another provider’s instruction, command or plugin system. The reusable Agent catalogue records portable semantics; this record describes one current adapter.

## 4. Evidence and claim classes

Every load-bearing field should identify one or more of:

- official provider documentation;
- provider-returned exact-request metadata;
- organization admin/audit evidence;
- operator-observed UI state;
- operator-reported selection or experience;
- mechanically verified task/repository result;
- controlled behavior evaluation;
- model self-report, explicitly untrusted;
- unknown/not attested.

Official documentation and current web verification establish provider claims at an access date. Controlled task evidence establishes bounded observed behavior. Neither alone proves a permanent capability.

## 5. Freshness rules

Recheck an entry before it influences a decision when any of these occurs:

- plan, price, quota or model list may have changed;
- product UI or setting names changed;
- a tool/connector gained or lost write actions;
- privacy, retention or data-use policy changed;
- a model or mode is used for a new task class;
- the last observation is older than the target decision tolerates;
- observed behavior conflicts with the stored entry;
- the user switches provider, account type, region or product surface.

Historical entries remain preserved with their observation date; they are not silently rewritten as if the old run occurred under the new product.

## 6. Human-readable view

The user-facing catalogue should normally display a concise comparison such as:

| Product/surface | Useful for | Important limits | Settings to check | Last verified |
|---|---|---|---|---|
| current verified entry | bounded task classes | material limitations | exact visible names | date |

Detailed schemas, citations, exact UI steps and run receipts remain linked and on demand. Avoid presenting a large machine-oriented record when the user only needs to choose among a few current options.

## 7. Initial information needs for the first three systems

### Meta-Agent

Verify only when preparing a bounded Meta-Agent pilot or packaging task:

- which frontier and next-tier surfaces can access the target repository;
- how reusable prompts/instructions/Skills are installed and versioned;
- whether the product can load target-local files deterministically;
- how task-local repository writes and review evidence work;
- context, file and tool limitations relevant to Agent design packages.

### Work/business-function code library

Verify when selecting the execution toolchain:

- repository read/write and branch/PR capabilities;
- local or cloud code execution/test support;
- file size, repository indexing and context behavior;
- secrets/private-source handling;
- model/tool suitability for frozen code changes versus architecture work.

### Long-term language teacher/practice Agent

Verify when selecting text/voice surfaces:

- conversation/project memory and isolation settings;
- text, voice, file and structured-output capabilities;
- transcript/export availability and speech-recognition limitations;
- private learner-record storage and data-use boundaries;
- ability to load a target-local teaching/memory package;
- cost, quota, latency and interruption behavior for sustained practice.

## 8. Population strategy

Do not attempt to populate every provider/product field before real use.

Use this sequence:

1. identify the target decision that needs current product facts;
2. select the smallest relevant set of products/surfaces;
3. verify official current facts and record the access date;
4. run a bounded behavior check when documentation cannot establish actual task reliability;
5. use the result in a target-specific selection record;
6. revisit only on the stated freshness trigger.

This prevents the catalogue from becoming a costly, constantly stale encyclopaedia.

## 9. Relationship to model reliability validation

Issue #265 TODO 3 should create controlled task observations linked to this catalogue, including:

- visible model/surface selection;
- frozen task contract and source ref;
- correctness and scope adherence;
- authority and unknown handling;
- escalation behavior;
- human rework and review burden;
- cost, latency and quota observations when available;
- exact backend status as unknown unless independently attested.

A successful run becomes bounded evidence for that task class, not a universal provider ranking.

## 10. Boundaries

This design does not:

- claim current Claude, ChatGPT, Fable or other Skills/model/product behavior;
- bind a named model permanently to frontier or next-tier work;
- authorize a subscription, purchase, quota use, connector activation or repository write;
- treat UI labels as hidden backend attestation;
- replace target-specific privacy and authority decisions;
- automatically inject provider records into normal Agent runtime context;
- turn product settings into portable Agent capabilities.

## 11. Design rationale

The provider/product catalogue is separated from the reusable Agent capability catalogue because the two evolve at different rates and have different evidence rules. Portable capability semantics should remain stable enough to reuse; provider adapters must be reverified and may be replaced without redefining the target Agent’s purpose.
