NON_AUTHORIZING_CANDIDATE — DO NOT SEND TO A CONTROLLER UNTIL A LATER PRO REVIEW AND SEPARATE OWNER G2A.

# WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001 — Complete Response

```yaml
task_id: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001
canonical_route: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 G2A组合
executed_by: Fable 5, Work mode, Ultra effort, Research off, fresh Project
run_window_utc: 2026-08-19T06:19:02Z .. 2026-08-19T06:37:41Z (end ref snapshot; page/REST corroboration to ~06:39Z; final post-resume confirmation snapshot 2026-08-19T06:41:13Z, identical — see §3)
verdict: CANDIDATE_COMPOSITION_READY_FOR_PRO
repository_writes_performed: none
G2A_issued: false
A1_executed: false
```

## 1. Input-integrity gate — PASS

```yaml
inputs_present: 2 (exactly)
task_file_bytes: 8183 (expected 8183)
task_file_sha256: a69851497a33e1065ed09d2394824fe064adb868b8b24835e1f64023d2767cac (exact match)
input_manifest_bytes: 3412
input_manifest_sha256: 5ab28f86bc34e39532524411d4681894c349c5cdf4bec183748410ae78af7eb4 (recorded for evidence)
task_id_route_display_name_agreement: exact
repository_name_agreement: exact (08822407d/Mnemosyne; 08822407d/mnemosyne-target-lifecycle-validation-002)
research_off: confirmed (no web_search, no Research feature used at any point)
github_access: read-only (unauthenticated GET/ls-remote/clone only; no credentials in environment)
```

## 2. Execution-time GitHub gate — PASS (start == end everywhere)

```yaml
Mnemosyne:
  default_branch: master
  master_start: e726dea818dca9418181775d0e7dcd62eb6c464a   # 06:19:17Z REST + 06:20:35Z ls-remote, identical
  master_end:   e726dea818dca9418181775d0e7dcd62eb6c464a   # 06:37:41Z ls-remote
  heads_start_end: identical (1 ref: master)
  pull_ref_set_start_end: identical (297 refs/pull/*/head, historical closed PRs)
  open_PRs_start: 0   # pulls page numeric count "0 Open / 297 Closed" at 06:21:49Z
  open_PRs_end: 0     # pulls page numeric count "0 Open / 297 Closed" at ~06:38Z
mnemosyne-target-lifecycle-validation-002:
  default_branch: master
  master_start: e8e3296922185b4b70997c2351d6f39423f2cd4f   # == validation_hard_pins.master
  master_end:   e8e3296922185b4b70997c2351d6f39423f2cd4f
  heads_start_end: identical (18 refs: master + 16 tlr-v1-* + v2a-sentinel-001-controller)
  pull_ref_set_start_end: identical (0 pull refs — no PR has ever existed)
  open_PRs_start: 0   # REST returned [] at 06:19:17Z; page "0 Open / 0 Closed" at 06:21:49Z
  open_PRs_end: 0
five_A1_branch_names: absent in both repositories at start and at end
G2A_or_A1_started_state: none (F2 status file confirms G2A_issued: false, A1_branches_created: false)
static_identities: 15 of 15 manifest path→blob pairs MATCH on live master (see §4)
hard_pins_verified_locally:
  validation_master_pin: match
  fixture_commit_81f18eb5…: present; its tree == f1e221ce8aef404579b96adb3ab01319016889db (recomputed from clone)
  fixture_branch_head: tlr-v1-fixture-base == fixture_commit (live)
  A0_controller_head_d936cd2d…: present; == live v2a-sentinel-001-controller head
  sixteen_tlr_v1_refs: live heads byte-equal to pkg001 manifest §4 inventory (all 16)
  wrapper_task_contract_blobs: pkg001/03 == 9cb67f6e8b00…, pkg001/04 == 9544963bc40f… on live master (match canonical blocks)
final_confirmation_snapshot_end2: 2026-08-19T06:41:13Z  # post-resume, at actual task completion
  ls_remote_both_repositories: byte-identical to start (diff empty; masters e726dea… / e8e3296… unchanged)
  five_A1_branch_names: still absent in both
  open_PRs_pages: Mnemosyne 0 Open, validation 0 Open (REST still rate-limited at end2; disclosed)
```

## 3. Evidence-access method adaptation (full disclosure)

Unauthenticated GitHub REST on this environment's shared egress IPs hit the 60/hr pool mid-enumeration (403s observed from three distinct rotating IPs: 34.23.141.224, 34.23.109.184, 34.138.70.217; /rate_limit showed 54 remaining seconds before exhaustion, i.e. the pool is consumed by co-tenants). REST calls that succeeded: Mnemosyne repo metadata + branch list; validation-repo open-PR list (`[]`). All remaining reads were completed through equally read-only, explicitly permitted GitHub fetch channels that are not REST-quota-bound: `git ls-remote` (full ref enumeration with SHAs, start and end), depth-1 bare `git clone` of both repositories (content-addressed object store; every extracted blob's SHA-1 was recomputed locally and asserted equal to its pin), and the public `github.com/<repo>/pulls` pages for numeric open/closed counts (start and end). No call was retried after a gate block; the channel substitution was a transport adaptation, not a rerun. Open-PR state for Mnemosyne therefore rests on page counts at start and end plus the invariant 297-element pull-ref set, and for the validation repository on REST `[]` plus page counts plus the zero pull-ref set. Assessed as complete enumeration through permitted operations; disclosed here for Pro.

Session continuity, disclosed for the same reason. The composing session was interrupted twice by assistant-side context-window compaction (once before composition began, once after the six outputs were drafted but before final verification, manifest sealing and presentation). Each time, work resumed from the preserved container state and transcript; no gate ever returned a blocked state, and no blocked or failed operation was re-attempted, so the task's no-retry rule was never triggered — these were continuations of one run, not reruns. On the final resume, every already-written output was re-verified mechanically before sealing (banner placement, byte-identical embedded blocks via `cmp` against the pinned-blob extracts, canonicalization scans, placeholder census, matrix-recorded candidate SHA-256 re-hashed and equal), and one additional read-only end-state snapshot ("end2", 06:41:13Z, recorded in §2) was taken to extend the verified start==end window through actual completion. It was byte-identical to start for both repositories.

## 4. Read register

Pinned files read (all 15; every blob SHA-1 recomputed locally from content and asserted equal to the manifest pin):

```text
01f64a82  current/human-approved-spec.md  (structure + §19 validation/provenance principle read in targeted form)
87f110c5  …/MNE-…-V2A-A1-RUN-DECISION-CANDIDATE-004.md
8a978e1a  …/execution-package-004/01-package-and-source-manifest.md
28da6ab6  …/MNE-…-V2A-A1-RUN-DECISION-CANDIDATE-003.md
7611773d  …/execution-package-003/01-package-and-source-manifest.md
a8b627b8  …/MNE-…-V2A-A1-RUN-DECISION-CANDIDATE-002.md
1f54f471  …/execution-package-002/01-package-and-source-manifest.md
bb140196  …/MNE-…-V2A-A1-RUN-DECISION-CANDIDATE-001.md
12a48044  …/execution-package-001/01-package-and-source-manifest.md
fd125ff3  …/execution-package-002/03-revised-operator-flow-and-startup-messages.md
20ca5ceb  …/execution-package-003/02-canonical-runtime-wrapper-transport-and-comparison-contract.md
a8447a57  …/execution-package-003/03-revised-worker-launch-return-and-controller-resume-flow.md
5a148859  …/execution-package-003/04-result-mapping-tool-side-effect-and-integrity-checklist.md
8dcc7cba  …/execution-package-004/03-corrected-handoff-publication-and-receive-rehearsal-contract.md
0e02aab3  current/fable5-cross-repository-safe-concurrency-research-status.md  (F2 status + execution source identity: 37074 bytes / sha256 6e639f7b…)
```

Additional non-cold files read because directly necessary to compose or verify the candidate (task §5 register; blobs from live master, locally recomputed):

```text
a8c70040  …/execution-package-004/00-delta-precedence-and-source-identity-correction-contract.md   # the Package 004 delta named by task §5
5ce64f2b  …/execution-package-003/00-delta-precedence-and-readiness-defect-contract.md             # precedence scopes for [C-06]
85855f2e  …/execution-package-002/00-delta-precedence-and-defect-contract.md                       # precedence scopes + evidence separation
935f19c9  …/execution-package-002/02-staged-model-binding-contract.md                              # staged model-label timing (comp. req. 6)
543b4c77  …/execution-package-001/00-owner-gates-and-surface-contract.md                           # future exact Owner G2A hierarchy (task §7)
9b19d470  …/execution-package-001/07-operator-flow-and-startup-messages.md                         # original G2A hierarchy for the comparison
6da0b44d  …/execution-package-001/02-branch-task-and-effect-map.md                                 # branch/task/effect + order + ten-output terms
```

Cold sources: the live tree contains zero cold-labelled paths; no cold original of any kind was read, and no path outside the 22 files above was read as content (name-level tree enumeration only, required for identity verification). The raw/validation-reviews archive parts were not read; their identities were carried by reference only.

## 5. What was composed

One complete non-authorizing composite controller G2A/startup candidate, `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-COMPOSITE-G2A-CANDIDATE-001` (file 2; sha256 `e51af7f7c175bf9ce43171a56921f77a51dfe5d05cff973ae4f05ceadf3a2516`; 26,377 bytes; clause anchors C-01..C-24). It satisfies the fourteen composition requirements as follows: (1)(2) exact blob bindings for candidate/manifest 004 and inherited 003/002/001 at [C-03]/[C-04]; (3) mandatory 004→003→002→001 reading with partial-reading block at [C-05]; (4) Package 004's narrow archive-tuple + handoff-closure scope at [C-06]; (5) canonical wrapper transport, exact Owner-sent/worker-received preservation and the three-way comparison at [C-12]/[C-16]/[C-17]; (6) Package 002 staged label timing at [C-08]/[C-15]; (7) Package 001 fixture/branch/task-effect/blob-tree/order/ten-output/no-PR/no-retry/evidence-ceiling and retention terms at [C-07]/[C-11]/[C-18]/[C-21]/[C-23]; (8) both Package 003 canonical `BEGIN…END` blocks mechanically incorporated byte-exactly at §6.1/§6.2 (cmp PASS against blob `20ca5ceb…`; canonical SHA-256 `8d82d785…` Alpha / `798f8ba6…` Beta); (9) the exclusive fill schedule — authorized-label placeholders only before template freeze, selected-label placeholders only at the exact worker launch, exactly one substitution per sent wrapper — at [C-09]; (10) Package 002's §4/§5 prose wrappers and §3 pointer sentence declared historical/superseded, never to be frozen or sent, at [C-13]; (11) preflight-before-write and all phase-specific stop rules at [C-10]/[C-19]; (12) `ref_not_moved` ≠ `zero_repository_side_effect` with object-SHA and unknown-risk recording at [C-20]; (13) the full during-A1 prohibition union (Web, Research, Fable, other Apps, private material, external quota, repair, retry, reset, rollback, cleanup, and the remaining Package 001/003 items) at [C-21]; (14) `G2A_authorized: false` fixed in the artifact, with the required banner as line 1 and non-promotion language at [C-01]/[C-24]. All dynamic values remain explicit placeholders: eight G2A-issuance fields (protected Mnemosyne and Meta-Agent masters, controller authorized+selected labels, Alpha/Beta authorized labels, execution window start, G2A timestamp), the two wrapper selected-label tokens, and worker selected labels expressed as the Package 002 `not_yet_observed` state — no Owner-authorized value, operator-selected value, execution-time master, branch-state observation or timestamp was filled or invented, and branch/PR inventory is defined as a fresh preflight observation duty rather than a pre-asserted field.

## 6. Comparison work

The clause-source matrix (file 3) maps all 26 load-bearing clause entries (C-01..C-24 plus the two block entries) to controlling source path/blob/section with inheritance-or-supersession reason, dynamic/static class, exactness class and conflict status; carries the five explicit comparisons required by task §7 (Package 002 §3 vs its old §4/§5 wrappers; Package 003 canonical wrapper contract; Package 003 revised flow; Package 004 candidate/manifest and narrow delta; the future exact Owner G2A hierarchy in Package 001 including the pkg001/07 asserted-selected-label defect that Package 002 superseded); and lists all thirteen Package 002 sentences (S1–S13) that the composite replaces, qualifies or renders non-authoritative, each with its disposition and receiving clause. Material unresolved conflicts: zero; seven clauses carry conflicts resolved by the stated precedence; five presentation-level items are flagged for Pro (F1 language, F2 state-token spelling, F3 new composite ID, F4 task-added timestamp field, F5 V1 inventory bound by reference).

## 7. Adversarial audit

Four separated same-provider passes, honestly labelled `independent_passes_not_distinct_agents` (file 4): identity/precedence, exact-message/placeholder, operator-flow/fail-closed, and lead disagreement synthesis. All thirteen mandated scenarios were tested and are defended by named clauses, several with mechanical evidence (byte-identical cmp of both embedded blocks and both operative Package 003 text blocks; 20-value 40-hex whitelist scan with zero unexpected values; zero CR/BOM/trailing-space; placeholder inventory exact; superseded Package 002 tokens present only inside the supersession clause; grep-level absence of any unconditional authorizing sentence). Material defects found: zero. Lead recommendation: READY for Pro, with F1–F5 and the chat-surface whitespace-transport risk explicitly handed to Pro.

## 8. Verdict and rationale

```text
CANDIDATE_COMPOSITION_READY_FOR_PRO
```

All input and execution-time gates passed with start==end repository states; all fifteen pinned identities and every cross-checked hard pin matched; the candidate is complete, fully placeholder-disciplined, mechanically exact where exactness is load-bearing, and internally conflict-free under the stated precedence; the audit found no material defect. READY means suitable only for the later Pro review in the sequence Handoff-003 rehearsal acceptance → fresh Pro execution-time review of Packages 004/003/002/001 → separate Owner G2A. It is not, and never becomes, G2A or A1 authorization; no repository, package, expected value, command or status record was modified by this run, and no branch, PR, worker, controller or validation cell was created, launched or executed.

## 9. Output inventory

```text
1  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-complete-response.md        (this file)
2  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-composite-g2a-candidate.md  (the candidate; banner line 1)
3  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-clause-source-matrix.yaml
4  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-adversarial-review.md
5  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-pro-adjudication-brief.md
6  WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001-output-manifest.yaml        (bytes + sha256 of 1–5; omits only its own recursive hash, with explanation)
```

Final status: WORK-ULTRA-FABLE-MNE-DR-005-G2A-COMPOSITE-CLOSURE-001_READY_FOR_PRO
