# MNEMOSYNE-032 Memory-System Design Draft

> Draft only, not execution source. Current execution source remains `current/human-approved-spec.md`.

## Project identity
Mnemosyne is a memory-system meta-Agent work repository for designing, reviewing, delivering, and evolving AI Agent external persistent memory systems.

## Execution source
`current/human-approved-spec.md` is the only execution source. Promotion into it requires user confirmation.

## Non-execution sources
Raw records, research evidence, summaries, review records, user restatements, candidate requirements, decision logs, active context, handoff, task results, templates, and dry-run outputs support reasoning but do not directly constrain execution when they conflict with the approved spec.

## Raw input layer
Store original user inputs, task records, research originals, and restatements with provenance and role labels. Preserve raw intent while allowing privacy/redaction exceptions.

## Evidence layer
Use research reports, summaries, evidence maps, capability boundaries, review records, and verification packages to constrain feasibility and modernization claims. PDF visual evidence remains pending until manually reviewed.

## Candidate requirements
Extract possible requirements from raw/evidence/review material into candidate form with status, source, risk, confidence, and required user decision.

## Decision log
Record accepted/rejected/deferred user-confirmed decisions. Decision records are audit/history unless promoted into the human-approved spec.

## Active context
Maintain current phase, current work set, latest safe continuation point, and route options. It is startup context, not law.

## Todo
Track actionable work by stage and status. TODO entries must not silently become execution rules.

## Open questions
Capture conflicts, uncertainties, research-refresh needs, and approval gates. Conflicts with execution source should be recorded here or in a risk log.

## Handoff
Provide a compact cross-session continuation card with read order, do-not-do list, current route, and local recovery notes. Handoff-local exceptions require explicit promotion before becoming global rules.

## Delivery manifest / task result records
For real target projects, use delivery manifests and task result records to audit intended files, actual files, diffs, protected-file checks, unsupported assumptions, and follow-up needs. MNEMOSYNE-032 does not create a real target package.

## Refresh / review loop
Periodically run research refresh cycles and delta reports, review candidate requirements, inspect drift, and request user confirmation for high-impact updates.

## Public/private/scratch boundaries
Separate public project memory rules, private/sensitive raw material, and task-local scratch work. Ordinary Agents may update authorized content but must not redesign shared memory structure without authorization.

## Update workflow
Input → raw/evidence record → candidate extraction → similarity/conflict check → capability-boundary check → user decision → approved spec/status update where authorized → task result record.

## Drift detection
Compare active context, handoff, todo, decision log, candidate requirements, and task results against the execution source and latest confirmed checkpoints. Flag outdated phase claims, over-promoted evidence, and stale assumptions.

## Failure recovery
Use handoff and task result records to recover local context; use Git diffs and protected-file checks to verify actual changes; use raw records and research originals only for targeted evidence checks.

## Unsupported assumptions
Current models may not reliably maintain permission boundaries; GitHub/Markdown may not scale indefinitely; automated memory testing is unverified; ordinary Agents may over-edit; privacy policy remains underspecified.

## Acceptance criteria
A future Agent can identify source authority, distinguish evidence/candidate/audit/history layers, preserve traceability, avoid unreviewed PDF/missing-prompt claims, generate candidate/open-question/risk outputs, and hand off auditable results without modifying protected files.
