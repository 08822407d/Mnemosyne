NON_AUTHORIZING_CANDIDATE — DO NOT SEND TO A CONTROLLER UNTIL A LATER PRO REVIEW AND SEPARATE OWNER G2A.

# Adversarial Review — Composite Controller G2A/Startup Candidate

```yaml
review_id: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-ADVERSARIAL-REVIEW-001
subject_file: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-composite-g2a-candidate.md
subject_sha256: e51af7f7c175bf9ce43171a56921f77a51dfe5d05cff973ae4f05ceadf3a2516
method_honesty_label: independent_passes_not_distinct_agents
method_note: >-
  All four passes were produced by the same Fable 5 instance in the same conversation, separated by concern and
  executed against the composed artifact and the content-address-verified source blobs. They are structured
  re-examinations, not independent agents, and cannot substitute for the later fresh Pro review.
```

## Pass 1 — Identity and precedence

Checks performed: every path/blob pair in candidate sections 1–3 compared byte-for-byte against the input manifest and against the live Mnemosyne master tree at `e726dea818dca9418181775d0e7dcd62eb6c464a` (all 40-hex values in the candidate matched the 20-value whitelist derived from verified sources — mechanical scan, zero unexpected, zero missing); precedence statements compared against the three 00-delta contracts and the Package 004 manifest's inheritance paragraph; the per-scope control map [C-06] checked against pkg004 00-delta ("controls only…"), pkg003 00-delta ("controls only where predecessors would permit 1–5"), pkg002 00-delta §2/§3.

Scenario tests:

1. Controller reads only Package 002. Defense: [C-05] makes reading all four candidate/manifest pairs and package files mandatory before any write and names partial reading (explicitly including "only Package 002") a `CONTROLLER_BLOCKED` condition; [C-10] repeats the four-layer identity set inside the preflight list. Residual risk: none at candidate level; enforcement depends on the future controller actually honoring [C-05], which Pro verifies at execution-time review. PASS.
2. Candidate 004 / manifest 004 omitted. Defense: [C-03] binds both with exact blobs; [C-05]/[C-10] make a missing or mismatched pair blocking; Package 004's six-file count and the controlling archive blob `6e90c8f1…` are separate preflight items, so an execution set that silently lacks 004 cannot pass preflight. PASS.
3. Candidate 003 / manifest 003 omitted. Defense: same mechanism via [C-04]/[C-05]/[C-10]; additionally the wrapper templates of §6 name their source blob `20ca5ceb…`, so a 003-less reading cannot verify the templates' provenance and blocks. PASS.
4. Precedence ambiguity (both old and canonical wrappers appear; authority unclear). Defense: [C-06] gives an explicit per-scope map; [C-12] declares the §6 blocks "the only valid A1 runtime-wrapper templates"; [C-13] declares the Package 002 §4/§5 prose wrappers and the §3 pointer sentence historical, not to be frozen, not to be sent. A controller holding both texts has a single written rule choosing the canonical block. PASS.

Pass 1 verdict: PASS, no identity or precedence defect found. Flag F5 noted: the 16-ref V1 inventory is bound by reference to pkg001 manifest §4 rather than re-listed inline (deliberate single-sourcing; live heads were spot-verified equal to that inventory during this task).

## Pass 2 — Exact message and placeholders

Mechanical evidence recorded during composition:

```yaml
alpha_block_cmp_vs_source_blob_extract: BYTE_IDENTICAL
beta_block_cmp_vs_source_blob_extract: BYTE_IDENTICAL
alpha_block_canonical_sha256: 8d82d785612bd1a42a284e23b80cc22b14b1b89ec2528d0382da1c7e1cd0b210
beta_block_canonical_sha256: 798f8ba658430559e479c5244806edf2d22894b49de9a70bfd92349de013b445
launch_instruction_block: EMBEDDED_EXACT_SUBSTRING_OF_CANDIDATE
owner_return_format_block: EMBEDDED_EXACT_SUBSTRING_OF_CANDIDATE
candidate_cr_bytes: 0
candidate_bom: absent
candidate_trailing_space_lines: 0
hex40_scan: 20 values found, all on the verified whitelist, none unexpected
placeholder_inventory:
  g2a_issuance: [PROTECTED_MNEMOSYNE_MASTER_AT_G2A, PROTECTED_META_AGENT_MASTER_AT_G2A,
                 CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL, CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL,
                 ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL, BETA_OWNER_AUTHORIZED_VISIBLE_LABEL,
                 EXECUTION_WINDOW_START_UTC, G2A_TIMESTAMP_UTC]
  wrapper_fill_before_freeze_only: [ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL, BETA_OWNER_AUTHORIZED_VISIBLE_LABEL]
  wrapper_fill_at_launch_only: [__MNE_ALPHA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__, __MNE_BETA_OPERATOR_SELECTED_VISIBLE_LABEL_AT_LAUNCH__]
  superseded_pkg002_tokens_present_only_inside_supersession_clause_C13: confirmed_single_occurrence_each
  format_markers_from_pkg003_return_block: "<ROLE> x5 (verbatim source text, not fillable candidate fields)"
filled_dynamic_values_found: none (no concrete model label, no ISO timestamp, no execution-time master)
```

Scenario tests:

5. Selected-label placeholder filled too early. Defense: [C-09] `at_exact_worker_launch.only` plus the explicit rule "a selected-label placeholder resolved before its worker's actual launch is a mismatch and blocks"; [C-17] requires exactly one substitution relative to the frozen template, so an early-filled template makes the three-way comparison fail with a second substitution or a pre-resolved frozen form. Double-covered (freeze gate + comparison arithmetic). PASS.
6. Authorized-label placeholder unresolved at template freeze. Defense: [C-09] "Template freeze is blocked if an authorized-label placeholder is still unresolved"; independently, a frozen template still containing `<…_OWNER_AUTHORIZED_VISIBLE_LABEL>` cannot yield `G2A_authorized_label_match: PASS` in the [C-17] schema. PASS.
7. Newline/BOM/trailing-space normalization. Source blocks verified: LF-only, no BOM, no trailing spaces, pure ASCII, exactly one LF after `END` (last byte 0x0a). Candidate whole-file verified with the same properties. [C-12] carries the canonical-serialization rule verbatim in substance, including "exactly one LF after the END line" and the no-normalization sentence. Residual risk (real, not a candidate defect): chat-surface copy/paste can normalize whitespace invisibly; the [C-17] SHA-256 triple over canonical representations is the designed detector, and the Pro brief recommends file-level transport of the blocks where the surface allows. PASS with noted transport risk.
8. Accidental G2A-like wording in a non-authorizing artifact. Grep of the candidate for authorizing constructions: the banner is line 1; `G2A_authorized: false` appears as a fixed property; every occurrence of "authorize/authorization" is either negated, attributed to the *future issued message*, or quotes a package rule. [C-01] explicitly prevents promotion by "review, quotation, transmission or lapse of time"; [C-24] repeats it. The candidate never says "is authorized"; the closest construction, "Scope granted by the future issued message is exactly…" ([C-02]), attributes authority strictly to the future message. PASS.

Pass 2 verdict: PASS. Findings F1 (the composite is written in English while the pkg002 §3 message body was Chinese — semantics carried by exact tokens/values; presentation choice flagged for Pro, who may commission a Chinese parallel rendering) and F2 (state spelled `NOT_YET_OBSERVED_UNTIL_*_LAUNCH` in the message layer and `not_yet_observed` in the yaml layer — both spellings originate in Package 002 itself (03 §3 vs 02 §2); candidate [C-08] declares the rendering relation explicitly).

## Pass 3 — Operator flow and fail-closed behavior

Walked the full future flow against the candidate: G2A receipt → [C-10] read-only preflight (blocks on any missing/unknown/mismatch; branch/PR inventory observed fresh, never pre-asserted — this also answers the task's "branch-state observations" dynamic class: they are duties, not fillable G2A fields) → [C-11] three exact branch creations, 00/01/02, payload + template freeze before Alpha, stop-and-hand-over → [C-14]/[C-15] one-substitution launch, pre-write gates → [C-16] two-object returns → [C-17] three-way comparisons + Git checks → [C-18] orders and ten outputs → [C-22] stop conditions → [C-23] retention.

Scenario tests:

9. Controller freezes the old prose wrappers. Defense: [C-13] prohibits freezing or sending them; [C-11] requires freezing "both canonical wrapper templates of [C-12]"; if it happened anyway, the [C-17] comparison against the *expected frozen canonical template* fails on every line, producing CELL_FAIL / no order construction, and [C-22] routes to fresh Pro. Fail-closed both ex ante and ex post. PASS.
10. Worker receives an altered fixed field. Defense: worker-side [C-15] full-wrapper reconstruction and exact comparison → `WORKER_BLOCKED_BEFORE_WRITE` before any write; controller-side [C-17] `task_path_blob_repository_branch_base_profile_match` and byte-equality of all three representations catch anything the worker missed; [C-19] maps the phase to the correct stop token. PASS.
11. Partial object creation with unmoved ref. Defense: [C-20] verbatimly carries the rule that `ref_not_moved` cannot support `zero_repository_side_effect`, requires returned object SHAs when available and an explicit unknown-unenumerable-risk record when ambiguous, and prohibits retry/rollback/reset/cleanup; [C-19] `PRESERVE_PARTIAL_STATE_STOP_NO_RETRY`. PASS.
12. Alpha self-PASS but controller comparison FAIL. Defense: [C-17] final sentence makes worker self-report never substitute for the controller comparison; pkg003/03's allowance (self-PASS may permit isolated Beta launch) is retained, and the false positive then prevents order construction (`CELL_FAIL_NO_ORDER_CONSTRUCTION`); Beta evidence, if any, is preserved under [C-19]/[C-20]. PASS.

Pass 3 verdict: PASS. One deliberate composite behavior confirmed as intended, not a defect: the candidate does not add any repair path for any failure class — every failure routes to preserve-and-stop plus fresh Pro, matching the no-retry inheritance.

## Pass 4 — Lead disagreement synthesis

13. Execution-time master or branch drift. Two layers: (a) at this composition task's own level, the execution-time gate required start == end for both repositories and the absence of the five A1 branch names, any drift returning `COMPOSITION_BLOCKED_EXECUTION_TIME_STATE` — results recorded in the complete response (start and end snapshots equal; all five names absent; zero open PRs); (b) at future A1 level, the candidate makes protected-master values issuance-time placeholders ([C-08]), requires the no-competing-route confirmation and fresh inventory at preflight ([C-10]), and lists protected-ref movement as an immediate stop ([C-22]), with post-G2A refresh prohibited. PASS at both layers.

Disagreements between passes and their resolution:

- Pass 2 initially treated the five `<ROLE>` tokens as candidate placeholders; Pass 1 classified them as verbatim source-format markers inside the mechanically copied pkg003 return block. Resolution: source-format markers (they are part of the byte-exact quoted format, not fields of this candidate). Agreed.
- Pass 3 questioned whether [C-08]'s `<G2A_TIMESTAMP_UTC>` invents a field no package defines. Resolution: it implements this task's own §6 dynamic class "timestamps"; it adds no authority and is flagged (F4) for Pro to keep or drop at issuance-template time. Agreed, keep with flag.
- Pass 1 questioned binding the V1 inventory by reference (F5) versus inline re-listing. Resolution: single-sourcing to pkg001 manifest §4 avoids a second copy that could drift; live heads were verified equal during this task; Pro may still demand inline listing in the issued message. Agreed, keep with flag.
- No pass found a material conflict between packages that the stated precedence fails to resolve, and no pass found a clause in the candidate without a controlling source or task-contract basis.

```yaml
scenario_results:
  controller_reads_only_package_002: DEFENDED_C05_C10
  controller_freezes_old_prose_wrappers: DEFENDED_C13_C11_C17
  both_wrappers_present_authority_ambiguous: DEFENDED_C06_C12_C13
  candidate_004_or_manifest_004_omitted: DEFENDED_C03_C05_C10
  candidate_003_or_manifest_003_omitted: DEFENDED_C04_C05_C10
  selected_label_filled_too_early: DEFENDED_C09_C17
  authorized_label_unresolved_at_freeze: DEFENDED_C09_C17
  newline_bom_trailing_space_normalization: DEFENDED_C12_C17_plus_mechanical_scans; transport_risk_noted_for_pro
  worker_receives_altered_fixed_field: DEFENDED_C15_C17_C19
  partial_object_creation_unmoved_ref: DEFENDED_C20_C19
  alpha_self_pass_controller_fail: DEFENDED_C17_C19
  accidental_g2a_like_wording: DEFENDED_banner_C01_C24_grep_clean
  execution_time_master_or_branch_drift: DEFENDED_task_gate_plus_C08_C10_C22
findings_for_pro: [F1_language_presentation, F2_state_token_spelling, F3_new_composite_candidate_id,
                   F4_g2a_timestamp_field_task_added, F5_v1_inventory_bound_by_reference]
material_defects_found: 0
lead_recommendation: CANDIDATE_COMPOSITION_READY_FOR_PRO
```
