# Runtime-Guidance Profile V0 Source Mapping v0.1

> Static/mechanical mapping for `MNEMOSYNE-RUNTIME-GUIDANCE-PROFILE-VALIDATION-001`. It does not change active guidance or authorize V1 behavior runs.

```yaml
mapping_id: MNEMOSYNE-RUNTIME-GUIDANCE-V0-MAPPING-001
task_id: MNEMOSYNE-199
repository_ref: 08822407d/Mnemosyne@37a4bb62239c03c0cf42a63386e25079d11b732f
loader_ref: commands/load-mnemosyne-guidance.md
candidate_ref: notes/runtime-guidance-load-profile-candidate-v0.1.md
status: PASS_STATIC_MAPPING_WITH_NONBLOCKING_REPAIRS
execution_source_modified: false
```

## 1. Loader-rule mapping

| Loader rule | Compact meaning | Canonical source(s) | Candidate module |
|---|---|---|---|
| 1 | do not use old conversation/model memory as repository truth | `current/human-approved-spec.md` §§2, 4, 7–8 | CORE |
| 2 | sole Mnemosyne execution source | `current/human-approved-spec.md` §4 | CORE |
| 3 | objective, neutral, evidence-bound engineering | `current/human-approved-spec.md` §11 | CORE |
| 4 | opening user-operation/no-operation section | `current/human-approved-spec.md` §12; `current/user-operation-next-step-capability-and-intent-guard.md` §2.1 | CORE |
| 5 | closing next-step section | `current/user-operation-next-step-capability-and-intent-guard.md` §2.2; clarification guard §1 | CORE |
| 6 | explicit next-stage capability estimate | user-operation guard §3 | CORE |
| 7 | reassess capability after material change/failure | user-operation guard §3.5 | CORE |
| 8 | separate Deep Research and independent frontier assessment | user-operation guard §4.1; clarification guard §§7–8 | CORE; CLARIFICATION when material |
| 9 | auto-deliver a ready research task only after research gate | user-operation guard §4.2; clarification guard §7 | CORE; EXTERNAL_FLOW/EXTERNAL_RESEARCH when task delivered |
| 10 | Owner retains provider/surface/quota/run trigger | user-operation guard §§4.1–4.3; clarification guard §7 | CORE |
| 11 | do not fabricate a research report | user-operation guard §4.3 | CORE |
| 12 | route owner/fact/design/missing-artifact uncertainty correctly | user-operation guard §5.3; clarification guard §§2, 5, 7 | CORE; CLARIFICATION when material |
| 13 | user wording is evidence, not automatically complete spec | user-operation guard §5 | CORE |
| 14 | risk-adaptive clarification routing | clarification guard §2 | CLARIFICATION |
| 15 | contextualized material-question contract | clarification guard §3 | CLARIFICATION |
| 16 | recommendations separated from facts/values | clarification guard §4 | CLARIFICATION |
| 17 | visible/correctable answer ledger for dependent questions | clarification guard §6 | CLARIFICATION |
| 18 | one canonical Deep Research report plus supported export | `current/deep-research-report-delivery-correction-guard.md` §§1–5; execution source §13 | DEEP_RESEARCH |
| 19 | conditional complete-response transfer file for non-Deep-Research | artifact-delivery guard §3A | ARTIFACT |
| 20 | file-first delivery; no invented artifact/path | execution source §13; artifact-delivery guard §§3–6 | ARTIFACT |
| 21 | same-response complete operator flow for external tasks | artifact-delivery guard §3B | EXTERNAL_FLOW; ARTIFACT when file delivered |
| 22 | explicit cross-conversation execution intent and dedicated flow | cross-conversation guard §§2–4 | EXTERNAL_FLOW |
| 23 | local artifact generation separated from external actions | artifact-delivery guard §§2, 4, 9; execution source §18 | ARTIFACT; REPOSITORY_WRITE when external write |
| 24 | dependency-aware staged task/prompt generation | execution source §17; user-operation guard §4 | CORE; EXTERNAL_FLOW/EXTERNAL_RESEARCH when applicable |
| 25 | product/model/tool facts are time-sensitive | execution source §11; run-context guard §§2, 6 | CORE; REPOSITORY_WRITE when recorded in PR/result |
| 26 | preserve local mainline; do not infer handoff/live route | loader purpose/boundary; execution source §§7, 15 | CORE; EXTERNAL_FLOW when handoff involved |
| 27 | single-active PR lineage | `current/github-single-active-pr-lineage-guard.md` | BRANCH_PR |
| 28 | important-write run context and PR provenance | `current/run-context-and-pr-provenance-guard.md` | REPOSITORY_WRITE |
| 29 | missing required files are explicit; do not invent state | loader rule/boundary; execution source §§11, 15; user-operation guard §5.3 | CORE |
| 30 | registered compact external research display name | `current/external-research-display-name-guard.md`; registry | EXTERNAL_RESEARCH |
| 31 | prominent PR retention only when required; explicit release | `current/pr-merge-branch-disposition-guard.md`; PR-lineage guard §8 | PR_MERGE |
| 32 | honest exact/normalized/source preservation level | `current/source-artifact-preservation-and-design-rationale-guard.md` §§2–7, 11 | SOURCE_AND_RATIONALE |
| 33 | compact external engineering rationale; no hidden chain-of-thought | source-preservation/rationale guard §§8–10 | SOURCE_AND_RATIONALE |
| 34 | preserved cold originals are default on-demand | source-preservation/rationale guard §7; execution source §§7–8 | SOURCE_AND_RATIONALE; CORE retains trigger summary |

## 2. Guard reachability

| Active guard | Triggered candidate module | Reachable | Notes |
|---|---|---|---|
| artifact delivery | ARTIFACT | yes | also loaded with external flow when a transfer artifact is generated |
| cross-conversation execution intent | EXTERNAL_FLOW | yes | required for analysis/preparation as well as launch |
| external research display name | EXTERNAL_RESEARCH | yes | registry read is part of the module |
| Deep Research delivery correction | DEEP_RESEARCH | yes | must be loaded for every Deep Research task/report operation |
| source preservation and design rationale | SOURCE_AND_RATIONALE | yes | this task itself triggers it because architecture is selected |
| user operation/capability/intent | CORE | yes | broadest guard; remains always loaded in candidate v0.1 |
| frontier clarification adjudication | CLARIFICATION | yes | loaded on material ambiguity/research-routing decisions |
| run context and PR provenance | REPOSITORY_WRITE | yes | important write/publication only |
| single-active PR lineage | BRANCH_PR | yes | extends REPOSITORY_WRITE |
| PR merge/branch disposition | PR_MERGE | yes | merge/review/release trigger only |

No active guard listed by the current loader is unreachable.

## 3. Fail-closed path checks

| Path | Required module(s) | Candidate failure rule | Static result |
|---|---|---|---|
| important repository write | REPOSITORY_WRITE | missing guard blocks write/publication claim | pass |
| branch/PR creation | REPOSITORY_WRITE + BRANCH_PR | missing lineage/provenance source blocks branch/PR | pass |
| PR merge instruction | PR_MERGE; BRANCH_PR when state changes | unknown retention or duplicate lineage blocks instruction | pass |
| Deep Research task/report | EXTERNAL_FLOW + EXTERNAL_RESEARCH + DEEP_RESEARCH; ARTIFACT when transfer file | correction guard missing blocks delivery/launch | pass |
| material source attachment | SOURCE_AND_RATIONALE; REPOSITORY_WRITE if stored | exactness cannot be upgraded without byte/hash proof | pass |
| high-impact ambiguity | CLARIFICATION | affected action stops/escalates if module missing | pass |
| cold source use | SOURCE_AND_RATIONALE | source must be named in receipt with trigger; existence alone insufficient | pass |

## 4. Nonblocking repairs discovered

### R1 — Stale status wording in the broad user-operation guard

The guard front matter still says `active_user_approved_behavior_guard_pending_MNEMOSYNE_178_merge`, although the repository has advanced far beyond that merge. This is stale metadata, not a finding that the guard is inactive.

Recommended repair: update the status in a separate bounded active-guidance task or the eventual profile-adoption task.

### R2 — Deep Research complete-response wording remains in broader historical guards

The broad user-operation guard and artifact-delivery guard retain wording that can be read as requesting an auxiliary complete-response file for Deep Research. The more specific `current/deep-research-report-delivery-correction-guard.md` explicitly supersedes those interpretations and does not require an arbitrary second model-generated file.

The current loader states the corrected rule. Candidate consequence: every Deep Research trigger must load the correction guard before task delivery. A later cleanup may amend the broader guards to point directly to the correction rather than restating older behavior.

### R3 — No exact section-level machine index

The mapping uses file paths plus human-readable section headings. This is adequate for V0, but anchors may drift after edits.

Recommended response: do not create hundreds of IDs now. If behavioral validation reveals source-mapping ambiguity, add a compact generated section index later.

## 5. V0 disposition

```yaml
V0_disposition:
  source_mapping_complete: true
  all_current_loader_rules_mapped: true
  all_active_loader_guards_reachable: true
  critical_fail_closed_paths_present: true
  blocking_defect_found: false
  nonblocking_repairs:
    - stale_user_operation_guard_status
    - broader_Deep_Research_wording_should_reference_specific_correction
    - exact_section_index_deferred
  result: PASS_STATIC_MAPPING_WITH_NONBLOCKING_REPAIRS
  V1_authorized: false
```

A separate Owner decision is still required before any V1 model comparison or active loader change.
