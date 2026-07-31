---
target_project_id: meta-agent
artifact_id: META-AGENT-RESEARCH-EVIDENCE-README-002
artifact_role: research_evidence_navigation
status: prepared_for_repository_review
authority_level: navigation_and_evidence_support
target_runtime_truth_source: false
created_by_task: META-AGENT-RESEARCH-EVIDENCE-REPAIR-003
---

# Meta-Agent DR-01–05 Research Evidence

## 1. Role and authority

This directory preserves the first five Meta-Agent Deep Research task prompts, the corresponding complete operator-exported reports, exact reconstruction metadata, and later review artifacts.

Nothing in this directory is Meta-Agent target truth. Research evidence cannot override:

```text
target-projects/meta-agent/current/approved-spec.md
```

The proposed target spec remains inactive until an explicit Owner disposition and a separately authorized activation change.

## 2. Contents

```text
target-projects/meta-agent/research/
  README.md
  archive/
    README.md
    META-AGENT-DR-01-05-EVIDENCE-002.tar.bz2.base64.chunk-001-of-038.txt
    ...
    META-AGENT-DR-01-05-EVIDENCE-002.tar.bz2.base64.chunk-038-of-038.txt
  meta/
    manifest.yaml
  reviews/
    MA-DR-01-05-cross-report-synthesis-v0.1.md
    MA-DR-01-05-gap-analysis-v0.1.md
```

The deterministic archive reconstructs ten logical members:

- five original Deep Research task prompts;
- five complete operator-exported reports.

Owner decision support is stored at:

```text
target-projects/meta-agent/decision-support/Meta-Agent-v0.1-owner-disposition-decision-package.md
```

The repository-process incident and separate Mnemosyne-maintainer intake are stored under:

```text
notes/mnemosyne-maintenance-issues/
```

## 3. Preservation model

The ten source files are stored inside one deterministic GNU tar archive (`mtime=0`, uid/gid 0, empty user/group names, mode `0644`), compressed with bzip2 level 9, Base64-encoded, and split into 38 ordered text chunks.

`meta/manifest.yaml` records:

- each logical member's byte count and SHA-256;
- tar, compressed stream and Base64 identities;
- every physical chunk's size, SHA-256 and Git blob SHA;
- reconstruction order and commands;
- report/task binding and citation-portability limits.

This exact archive is required because the report exports do not all end with a final line feed and must not be silently normalized.

## 4. Evidence roles

- `archive/`: exact source preservation; non-execution-source.
- `meta/manifest.yaml`: identities, task/report binding, run-context limits and reconstruction contract.
- `reviews/`: later synthesis and gap analysis; model-generated review evidence/candidates, not report originals and not target truth.

## 5. Citation-portability limitation

The five report exports contain:

```yaml
opaque_ChatGPT_citation_groups: 283
direct_HTTP_URLs_inside_report_exports: 0
source_panel_or_direct_source_manifest: not_preserved
```

The complete report bodies are independently recoverable. Their original product-native source-panel navigation is not.

The original Deep Research conversations may be archived. Permanent deletion should wait until source metadata is separately exported or the Owner explicitly accepts the loss of citation-link portability.

## 6. Public-repository safety

The repository is treated as public-risk. This package contains public/non-sensitive research prompts and reports only. It contains no credentials, secrets, private source code, raw private chat/voice transcript, customer/confidential material, or invented reconstruction of the lost original Meta-Agent conversation.

Future research material still requires task-local visibility, sensitivity and write-authority preflight.

## 7. Update rule

A later report, review or stronger model may add evidence, challenge conclusions, recompute synthesis or propose target changes. It may not silently overwrite originals, change target truth or promote candidate methods.

Target changes require Owner authorization, versioning, validation and rollback/revision planning.
