# FABLE5 Independent Greenfield Reconstruction — Task Charter

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
track_name: independent_greenfield_reconstruction_of_persistent_memory_meta_agent
charter_status: proposed_awaiting_user_approval_to_run_step_1
author_model: Fable 5
authority_level: non_execution_source_advisory_evidence
repository: 08822407d/Mnemosyne
relationship_to_existing_design: contrastive_reference_track_not_review_not_replacement
```

## 1. Objective

Independently design, from the user's original/near-original need materials and the research-input layer, a persistent-memory meta-agent serving the same broad purpose as Mnemosyne — an agent-and-repository system that designs, evolves, and delivers external persistent memory systems for other AI-agent projects while remaining model-replaceable, auditable, and human-gated.

The finished independent design is a **contrastive reference**: a second, independently derived solution to the same original problem, produced without reading the current GPT-produced design, so that a later, clearly separated comparison phase can surface omissions, blind spots, weak assumptions, overfitting, and enhancement opportunities in either design. It is explicitly **not** a review of the current design, not a candidate replacement for `current/human-approved-spec.md`, and not authorization for any repository change.

## 2. Source Policy

```yaml
source_tiers:
  allowed_primary_design_inputs:
    - raw/concept-origin-extract-001.md            # near-original user needs, motivations, reasoning, assistant responses at concept time
    - raw/research-reports/current/research-report-index.md    # index of RC-2026Q2-initial (7 reports) + supplemental cycles
    - raw/research-reports/current/current-research-prompts.md # research INPUTS (user questions), the least-contaminated intent signal
  allowed_on_demand_evidence_inputs:
    - raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/*   # verbatim user research questions
    - raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md  # why research was commissioned (use for motivation only; skip sections that describe current template packs — see contamination notes)
    - raw/research-reports/cycles/2026Q2-initial/originals/*                    # research REPORT contents, as capability-boundary evidence only
    - raw/research-reports/current/current-report-summaries.md                  # entry index; if summary vs original conflicts, original wins
    - other raw/chatgpt-discussion-* files ONLY when they contain original user need statements, retrieved by need-keywords, never by design-keywords
  prohibited_during_design_phases:
    - current/human-approved-spec.md
    - current/active-context.md, current/todo.md, current/open-questions.md
    - handoff/**
    - notes/**  (including candidate-requirements, decision-log, templates, codex-task-results, cross-model-review-results)
    - commands/**
    - FABLE5 review results and triage records
    - MNEMOSYNE task records generally, including MNEMOSYNE-095..100
    - anything whose filename or content declares it a GPT-produced design, decision, template, or task result
  prohibited_always_in_this_track:
    - inventing repository state; using web search as a substitute for repository raw materials
  authority_note: >
    All inputs are evidence, not execution source. The track's outputs are
    likewise non-execution-source. current/human-approved-spec.md remains
    Mnemosyne's only execution source throughout; this track never reads it
    during design and never competes with it.
```

Rationale for the tier split: the concept-origin extract preserves needs *with their reasons*; the research **prompts** are the user's own questions (input-side, minimally model-shaped); the research **reports** are external evidence usable for capability boundaries without revealing the GPT design. The prohibited tier is where the current design actually lives.

## 3. Anti-Contamination Method

1. **Input firewall.** During design phases (Steps 1–4), only the allowed tiers above are retrieved. Retrieval queries are formulated from need-language (e.g., 记忆/需求/动机/反馈/迁移/查重) — never from design-artifact language (spec sections, task IDs, template names, file layouts of the current design).
2. **Incidental-exposure ledger.** Retrieval is chunk-based and may surface prohibited-tier text uninvited (this session's seed check already surfaced fragments of `notes/candidate-requirements.md` and `notes/decision-log.md`, and the concept extract itself names the layered raw/candidate/spec model as the assistant's concept-time response — that response is legitimately part of the origin record). Every incidental exposure is logged in the step output: file, what was seen, whether it was used. Seen-but-unused is acceptable; used-from-prohibited-tier invalidates the affected design element and must be flagged.
3. **Derivation discipline.** Every design element in the independent spec must cite its source: a quoted need from the origin extract, a quoted research prompt/report finding, or an explicitly labeled `independent_design_choice` with its own rationale. Elements with no citation and no rationale are not allowed.
4. **Known-contamination disclosure (standing).** This reviewer (Fable 5, this conversation) has extensive prior exposure to the current GPT design from the FABLE5 review series. Perfect clean-room conditions are impossible; the mitigation is disclosure plus derivation discipline: (a) this fact is recorded in every step output; (b) where a design choice matches the current design, the citation trail shows whether it was independently forced by the origin materials or is potentially memory-echo, marked `possible_prior_exposure_echo: true` when honesty requires; (c) the later comparison phase treats echo-marked elements with reduced novelty weight. This makes the track "independent by derivation and disclosure" rather than pretending "independent by amnesia" — and preserves exactly the contrast value the user wants: convergence points become *stronger* validation when the derivation is forced by the origin materials, and divergence points remain genuine alternatives.
5. **Phase firewall.** The comparison phase (Step 5) is a separate step with separate outputs; no comparison content is drafted during Steps 1–4. Only in Step 5 does the current GPT design enter scope, and then only read-only.

## 4. Atomicity Assumptions

```yaml
atomicity:
  assumption: repository_may_not_be_updated_between_steps
  consequences:
    - every step output is self-contained: it restates its charter linkage, source policy, exposure ledger, and boundary statement inside the output file itself
    - no step depends on a prior step's output having been stored in the repository; each step's prompt re-supplies or re-derives what it needs (the user may paste or attach the prior output file)
    - no step depends on any repair, spec update, or storage task having occurred, unless the user explicitly confirms it in the step prompt
    - step outputs are downloadable Markdown files suitable for later verbatim ingestion under notes/cross-model-review-results/-style conventions, but ingestion is optional and never assumed
    - if a later model treats the whole track as one atomic unit (charter + step outputs concatenated), nothing breaks: steps are ordered, self-labeled, and carry no hidden cross-references
  interruption_tolerance: >
    Steps are sized for the limited Fable 5 usage window; any step can be
    resumed or re-run from its prompt plus the prior outputs the user supplies.
```

## 5. Multi-Step Plan

```yaml
steps:
  - step_id: GF-STEP-1
    name: independent_need_model_reconstruction
    inputs: concept-origin extract (full targeted read); current-research-prompts (verbatim originals as needed)
    work: >
      Reconstruct the user's need model from origin materials only: enumerate
      needs, motivations, fears, constraints, and priorities as a structured
      need inventory (each item: near-original quote, interpreted need,
      stability assessment, open questions the origin record leaves).
      Deliberately re-derive rather than copy the concept-time assistant
      responses: where the origin record contains assistant proposals, extract
      the underlying USER need, not the proposed mechanism.
    output: FABLE5-GREENFIELD-001-STEP1-need-model.md (need inventory + unclear-needs question list for the user)
    workload_estimate: medium (roughly one focused session; ~8-12 retrieval batteries + one long output file)
    value: highest — everything downstream derives from this; also independently valuable as a need-coverage checklist even if the track stops here
    defer_ok: false_this_is_the_anchor

  - step_id: GF-STEP-2
    name: independent_capability_boundary_baseline
    inputs: research prompts (user questions) + research report originals/summaries as evidence, on demand
    work: >
      From the research layer, derive the capability-boundary facts an
      independent designer must respect (what conversation-only memory can/
      cannot do; what file/Git-based memory affords; write-back and audit
      constraints; platform-memory vs project-truth separation), each cited to
      report evidence and marked with a freshness caveat (reports are 2026Q2
      evidence, capabilities drift).
    output: FABLE5-GREENFIELD-001-STEP2-capability-boundaries.md
    workload_estimate: medium (report retrieval is chunky; PDFs summarized already — originals only where load-bearing)
    value: high — prevents the independent design from being science fiction
    defer_ok: partially (Step 3 can start from prompts-only boundaries, but Step 3 quality drops)

  - step_id: GF-STEP-3
    name: independent_architecture_design
    inputs: Step 1 + Step 2 outputs (user-supplied if not stored)
    work: >
      Design the greenfield persistent-memory meta-agent: information
      architecture (truth layers, evidence flows), authority model (who may
      change what, human gates), lifecycle (need intake → design → delivery →
      evolution → model migration), multi-project model, self-memory
      (bootstrap) model, and failure/drift defenses. Every element cited per
      the derivation discipline; alternatives considered recorded inline.
    output: FABLE5-GREENFIELD-001-STEP3-independent-design.md (the contrastive-reference design)
    workload_estimate: large (the biggest single step; may be split 3a architecture / 3b lifecycle+operations if the window demands)
    value: highest alongside Step 1 — this is the deliverable the comparison needs
    defer_ok: false_but_splittable

  - step_id: GF-STEP-4
    name: self_critique_and_assumption_register
    inputs: Step 3 output
    work: >
      Adversarial pass on the independent design itself before any comparison:
      unsupported assumptions, single-point failures, cost hotspots, places
      where the design quietly assumed capabilities Step 2 does not support,
      and a register of independent_design_choice items that most need user
      confirmation. Keeps the comparison honest by pre-marking the greenfield
      design's own weaknesses.
    output: FABLE5-GREENFIELD-001-STEP4-self-critique.md
    workload_estimate: small-medium
    value: medium-high — cheap insurance against the comparison becoming greenfield-flattering
    defer_ok: yes_but_before_step_5

  - step_id: GF-STEP-5
    name: contrastive_comparison_against_existing_design
    inputs: Steps 1-4 outputs + (NOW permitted, read-only) current/human-approved-spec.md and directly relevant current-design structure
    work: >
      Structured comparison: need-coverage matrix (which Step-1 needs each
      design addresses, how, and at what cost), divergence analysis
      (mechanism-level differences with trade-offs), omission/blind-spot
      candidates in EACH direction, overfitting candidates (current-design
      elements that look shaped by tool-availability or model-era accidents
      rather than needs), enhancement opportunities, and a Deep-Research-topic
      list per Section 8 criteria. Echo-marked convergences weighted per the
      anti-contamination method. Findings are advisory candidates for user
      triage, never repairs.
    output: FABLE5-GREENFIELD-001-STEP5-contrastive-comparison.md
    workload_estimate: large
    value: highest end-value — but only meaningful after 1-3 exist
    defer_ok: yes_and_should_wait_for_user_go
```

Priority order under a shrinking window: **1 → 3 → 2 → 5 → 4** if forced to choose (Step 2 folded into Step 3 at reduced depth); recommended order when the window allows: **1 → 2 → 3 → 4 → 5**. Steps 1 and 3 are the irreducible core.

## 6. Per-Step Storage and Raw Preservation

```yaml
storage_after_each_step:
  what_to_store_in_mnemosyne: >
    The step's single Markdown output file, verbatim, via a user-approved task
    only — recommended home: notes/cross-model-review-results/FABLE5-GREENFIELD-001/
    with a manifest following the existing canonical_copy_stored convention,
    authority_level: non_execution_source_advisory_evidence. Storage is
    OPTIONAL per the atomicity assumption; the track functions user-carried.
  raw_preservation_verbatim:
    - each step's exact prompt as sent (the user should keep the prompt text with the output)
    - each step's full output file, unsummarized
    - any user answers to a step's question list (original language, verbatim)
    - the incidental-exposure ledger entries (inside each output)
  never_stored_as: execution source, spec candidate, repair authorization, or template replacement
```

## 7. Criteria: When to Compare Against the Existing GPT Design

Comparison (Step 5) begins only when **all** of the following hold: (a) Steps 1 and 3 outputs exist and the user has had the chance to answer Step 1's unclear-needs questions (unanswered items are carried as explicit unknowns, not guessed); (b) the user explicitly authorizes the comparison step, since it lifts the read firewall on the current design; (c) the independent design's self-critique exists or the user waives it, so both sides enter the comparison with known weaknesses. Comparison is deliberately **not** triggered by partial completion — comparing a half-derived greenfield design against the mature current design would systematically flatter the incumbent.

## 8. Criteria: New Deep-Research Topics vs Overlap

```yaml
deep_research_topic_criteria:
  genuinely_new_when:
    - the question is load-bearing for a Step-3/Step-5 conclusion AND
    - no RC-2026Q2 report (per index/summaries, confirmed against originals when close) answers it AND
    - it is not answerable from repository raw materials AND
    - it concerns capability, practice, or theory facts (not user preferences — those go to the user question list instead)
  overlap_not_new_when:
    - an existing report answers it (cite the report instead)
    - it re-asks an existing prompt with cosmetic rewording (note as refresh candidate only if staleness is the issue)
    - it is really a design decision disguised as research
  staleness_refresh_rule: >
    If an existing report answers the question but the answer is
    capability-drift-sensitive and materially older than the decision it must
    support, propose a refresh/delta topic per the repository's research-cycle
    convention (new cycle, delta report, never overwriting old motivation) —
    labeled refresh, not new.
  output_form: each proposed topic ships as {question, why_load_bearing, overlap_check_result, proposed_cycle_label, priority}
```

## 9. What This Track Explicitly Avoids

Reading any prohibited-tier file during Steps 1–4; imitating or paraphrasing the current design's artifacts; writing any repository file; generating Codex tasks or executable repair prompts; updating or drafting execution-source content; resuming or closing the paused post-handoff route; treating its own outputs as review findings about the current design (that is the separate FABLE5 review track) or as truth voting; authorizing target workspace creation, target material ingestion, target repository writes, regression formalization, or operational builds; and claiming clean-room purity it cannot have (Section 3.4 governs instead).

## 10. Boundary Statement

This charter and all FABLE5-GREENFIELD-001 step outputs are non-execution-source advisory evidence. They authorize no repository writes, no Codex tasks, no execution-source updates, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post_084_handoff_validation_and_migration route. `current/human-approved-spec.md` remains Mnemosyne's only execution source; where any output of this track conflicts with it, the execution source prevails and the conflict is reported, never silently reconciled. All storage of track outputs into the repository requires explicit user approval and a user-approved task.

## 11. Next Prompt to Run Step 1

Send this (optionally attaching this charter file) when ready:

```text
Run FABLE5-GREENFIELD-001 GF-STEP-1 (independent need model reconstruction) per the stored charter.

Constraints: design-phase input firewall active — read only raw/concept-origin-extract-001.md and raw/research-reports/current/current-research-prompts.md (plus prompt originals under raw/.../research-prompts/originals/ as needed). Do not read current/, handoff/, notes/, commands/, or any GPT-design artifact. Log incidental exposures. Apply the derivation discipline and known-contamination disclosure.

Deliverable: FABLE5-GREENFIELD-001-STEP1-need-model.md as a downloadable file — structured need inventory (near-original quote, interpreted need, stability assessment, origin-record gaps) plus a question list for me on unclear or conflicting needs. Self-contained per the atomicity rules; end with the boundary statement. Read-only; no repository writes; no Codex tasks; stop after the file.
```
