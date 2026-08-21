# WORK-ULTRA-FABLE-MNE-DR-006 — Guidance-Loading Architecture Comparison

```yaml
artifact_id: WORK-ULTRA-FABLE-MNE-DR-006-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001-guidance-architecture-comparison
decision_owner: human_Owner
this_document_selects_nothing: true    # recommendation provided, explicitly rejectable
relates_to: HO-GUIDANCE-001 (which stays open; the target-project mnemosyne_guidance yes/no question is NOT decided here)
```

Scope note: this compares **how** required guidance gets selected and loaded during a handoff receive. It does not decide **whether** a target-project business conversation should also load Mnemosyne guidance — that is HO‑GUIDANCE‑001 and remains task-local `yes | no | unknown_requires_user_decision`.

---

## Option A — Current: separate Owner follow-up guidance message

Receiver receives + reports + stops; Owner sends `加载 Mnemosyne 指导约束` as a distinct message; receiver loads the execution-time-latest guard list from the load command and reports `mnemosyne_guidance_refresh`.

- **Authority**: cleanest. The Owner's explicit message is direct user instruction; guidance load is visibly Owner-triggered; nothing self-authorizes. The rehearsal-acceptance gate naturally sits between receive and guidance.
- **Observability**: high — two separate reports (`mnemosyne_handoff_receive`, `mnemosyne_guidance_refresh`) at two message boundaries.
- **Failure containment**: good on the receive side (a bad receive stops before guidance). Weak on the guidance side: the step depends on the Owner remembering it, sending the exact phrase, and in the right conversation — an unmonitored manual dependency. TODO‑001 (direct Owner instruction) calls this pattern fragile.
- **Task contamination**: the two-message boundary is itself a mild protection (guidance arrives after the task is fixed and reported), plus the existing report fields. No archived contamination incident.
- **Owner burden**: highest — one extra mandatory message per handoff, plus the wait/relay choreography; the current Handoff 003 flow already costs ≈8 Owner operations.
- **Pro-turn cost**: one extra receiver turn per handoff (the guidance turn), always.
- **Migration**: zero — it is the status quo; every existing package assumes it.
- **Product-surface limits**: none; works on any chat surface.

## Option B — One startup prompt, two explicit internal phases, two reports

A single startup message instructs: Phase 1 = receive + emit receive report; Phase 2 = (only if Phase 1 internally passes its own identity checks, or after an in-message gate token) load guidance + emit refresh report. Both reports appear, clearly separated, in one or two receiver responses.

- **Authority**: acceptable **only if** Phase 2 remains conditional on the same acceptance authority as today. Two sub-variants matter: **B1** (Phase 2 auto-proceeds when Phase 1 self-checks pass) weakens the external rehearsal-acceptance gate — the receiver self-certifies before guidance; **B2** (Phase 2 proceeds only after the Owner relays `REHEARSAL_ACCEPTED…`, but the *instructions* for Phase 2 were pre-loaded in the startup) preserves authority and removes only the "Owner must compose the right phrase" fragility. B2 is the defensible form for rehearsed handoffs; B1 is defensible only where the Owner explicitly accepts self-checked receives (low-stakes routes).
- **Observability**: high if the contract mandates two named reports and forbids merging them; slightly worse than A because both can land in one long response where truncation/ordering issues are possible.
- **Failure containment**: Phase‑2 failure must fail closed without poisoning the Phase‑1 result (validation scenario HV‑N‑024). The single-message design must state: a failed Phase 2 never invalidates a passed Phase 1, and never triggers retry.
- **Task contamination**: the startup itself carries the task; guidance arrives inside the same instruction stream — contamination risk is *structurally* slightly higher than A, mitigated by the mandatory task-ID echo in the refresh report.
- **Owner burden**: lowest of the compliant options — removes one mandatory Owner message (B2 reduces it to relaying the acceptance token, which the Owner already does today).
- **Pro-turn cost**: can merge receive+guidance into fewer billed turns; at worst equal to A.
- **Migration**: startup-prompt template change + receive/prepare command amendments; existing packages remain valid under A (immutable history); new packages opt in.
- **Product-surface limits**: needs a surface that reliably executes a longer multi-phase instruction and produces long structured output in order; degraded surfaces should fall back to A. This is a time-sensitive product fact to verify per run.

## Option C — Source-selected exact guidance manifest + receiver self-load

The **source** conversation freezes a guidance manifest (exact guard path + blob per entry, per-guard applicability note); the receiver loads exactly that manifest's files, verifies each blob, and fails closed on any mismatch. Orthogonal to A/B: the manifest defines *what* to load; A or B defines *when*.

- **Authority**: strong and honest — guidance selection becomes a frozen, reviewable source-side decision instead of an implicit "whatever the load command lists at receive time". But it introduces a **staleness trade**: a blob-pinned manifest blocks when a guard was legitimately updated after preparation. The manifest therefore needs a per-entry policy field: `pin: exact_blob | current_at_path`, chosen by the source per guard (exact for authority-critical guards, current-at-path for style guards) — that policy choice is itself Owner-reviewable.
- **Observability**: best — the refresh report can list expected vs actual blob per guard, `exact_match` style; missing/stale/wrong guidance becomes mechanically visible (validation scenarios HV‑N‑017/018/019).
- **Failure containment**: excellent; fail-closed is well-defined per entry.
- **Task contamination**: reduced — the receiver never browses for guidance, so decoy/maintenance files are structurally out of reach.
- **Owner burden**: none at receive time; small at prepare time (the source generates the manifest — automatable inside the prepare command).
- **Pro-turn cost**: neutral.
- **Migration**: additive — new field block in packages; the load command gains a "manifest mode"; legacy packages without a manifest fall back to the current list.
- **Product-surface limits**: none beyond ordinary file reads.

## Option D — Task-local guidance bundle

The package (or a companion file) embeds the required constraint text itself (or a frozen snapshot directory), with exact identities; the receiver loads the bundle, not `current/`.

- **Authority**: hazardous by default. A bundle is a *copy* of guards frozen at prepare time; if a guard is corrected between prepare and receive, the receiver runs on superseded constraints while believing itself compliant. It also creates a second place where guard text lives — exactly the dual-source-of-truth shape that produced FC‑03. Acceptable only for short-lived handoffs with an explicit expiry and a mandatory bundle-vs-current diff check at load.
- **Observability**: good (bundle identities are pinned) but the *divergence from current* is what needs surfacing, requiring an extra comparison step.
- **Failure containment**: fail-closed is easy; fail-*stale* is the problem.
- **Task contamination**: low (self-contained), same benefit as C.
- **Owner burden**: none at receive; moderate at prepare (bundle build).
- **Pro-turn cost**: neutral to slightly higher (diff check).
- **Migration**: heaviest — bundle build tooling, expiry semantics, diff-check contract; conflicts with the repository's "one canonical location" discipline.
- **Product-surface limits**: none; works even if `current/` were unreachable (its one genuine advantage: survivability when the canonical repo is unavailable — not a current Mnemosyne constraint).

## Option E — Human gate retained only for high-impact ambiguity

Baseline flow automates guidance (B2+C); the Owner is inserted as a mandatory gate only when defined triggers fire (mirrors the frontier guard's escalation categories): authority/trust-boundary change, target-project `mnemosyne_guidance: unknown_requires_user_decision`, manifest mismatch, first use of a new template generation, or any adjudication anomaly.

- **Authority**: preserves Owner control where it matters; codifies what the guards already say about escalation.
- **Observability**: trigger firing must itself be visible (the report states which trigger fired or `none`).
- **Failure containment / contamination**: inherits B2+C properties.
- **Owner burden**: near-minimum on clean runs; unchanged on risky runs.
- **Pro-turn cost**: minimum on clean runs.
- **Migration**: the trigger list must be written, reviewed, and validated — it is the riskiest artifact here, because an under-inclusive list silently removes human oversight. Not adoptable before the validation package measures trigger behavior.
- **Product-surface limits**: as B.

---

## Comparison table (summary judgments, `REPOSITORY_SUPPORTED_INFERENCE` + `DESIGN_RECOMMENDATION`)

| criterion | A (current) | B2 (two-phase startup) | C (source manifest) | D (bundle) | E (gated human) |
|---|---|---|---|---|---|
| authority integrity | ++ | + (B2) / − (B1) | ++ (with pin policy) | − by default | + (if trigger list sound) |
| observability | + | + | ++ | + | + (needs trigger visibility) |
| failure containment | receive ++ / guidance − | + (needs HV‑N‑024) | ++ | fail-stale risk | inherits B2+C |
| task-contamination resistance | + | ○ (needs task-ID echo) | ++ | ++ | inherits |
| Owner burden | − (highest) | ++ | ++ (receive-time) | + | ++ clean / = risky |
| Pro-turn cost | − (always +1 turn) | + | ○ | ○/− | ++ clean |
| migration cost | none | moderate | low (additive) | high | high (trigger design) |
| surface dependence | none | moderate, time-sensitive | none | none | as B |

## Recommendation (explicitly rejectable; nothing is selected by this document)

`DESIGN_RECOMMENDATION`: adopt **C now, B2 next, E later; keep A as the universal fallback; reject D as a default.**

1. **C (source-selected exact guidance manifest)** is the highest-value, lowest-risk step: additive, surface-independent, directly closes FC‑08, and strengthens A immediately without changing who triggers guidance.
2. **B2 (single startup, two phases, two reports, Owner acceptance token still gating Phase 2)** then removes the fragile free-form Owner message that TODO‑001 objects to, while preserving today's acceptance authority. Adopt only after MNE‑HVAL‑001 scenarios HV‑P‑003, HV‑N‑017/018/019/020, and HV‑N‑024 pass.
3. **E** is the eventual steady state but must wait for measured trigger behavior; its trigger list requires its own Owner review.
4. **A remains valid** for any surface, any degraded run, and all existing immutable packages.
5. **D** only as an explicit-expiry exception for handoffs that must survive canonical-repo unavailability — not a Mnemosyne default.

**Assumptions this recommendation depends on** (each falsifiable): (i) the execution surface reliably executes a two-phase startup and byte-faithful pastes — a time-sensitive product fact; (ii) the Owner wants to reduce per-handoff manual operations (stated in TODO‑001); (iii) guard files continue to live canonically under `current/`; (iv) blob-pinning granularity per guard is acceptable review overhead at prepare time; (v) rehearsal-acceptance remains the release gate (B2, not B1).

**Reject-premise path**: if the Owner values the explicit human guidance message as a deliberate attention checkpoint (a legitimate reading of the current design), then keep A, still adopt C underneath it (manifest inside the existing separate message), and drop B/E entirely — C is beneficial under every premise. If the Owner instead judges that even B2's pre-loaded Phase‑2 instructions concentrate too much in one message, a middle form exists: keep two Owner messages but make the second a fixed one-token acceptance relay whose full semantics live in the merged rehearsal contract (removes composition fragility, keeps the checkpoint).

Per-route override: any route may pin its own architecture in its package; a task-local choice is not a global precedent (same rule HO‑GUIDANCE‑001 already applies).
