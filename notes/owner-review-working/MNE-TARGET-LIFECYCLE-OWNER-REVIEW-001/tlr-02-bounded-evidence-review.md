# TLR-02 Bounded Evidence Review — Open-Source Change/Migration Documentation

> Review evidence only for `MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001`. This is not execution source, candidate v0.2, validation, or target adoption.

## Scope

Bounded review of official primary documentation from mature open-source ecosystems to inform how a code-library Agent should describe its own changes so downstream project Agents can assess rebuild/upgrade impact on demand.

Sources sampled:

- NumPy official release notes, NumPy 2.0 migration guide, and downstream-package guidance;
- Django official release notes, deprecation timeline, and upgrade guide;
- OpenSSL official migration guide and deprecated-function mappings;
- Kubernetes official deprecation policy and deprecated-API migration guide;
- Semantic Versioning 2.0.0 as a reference convention, not as a universal rule.

## Verification note

```yaml
verification:
  verified_at: 2026-08-14
  verification_scope: current accessibility and stated migration/deprecation/change-documentation behavior of the named official sources
  source_class: official_primary_documentation
  result: verified_for_current_TLR_02_bounded_use
  limitations:
    - this is a small illustrative sample, not an empirical census of open-source ecosystems
    - common-pattern conclusions are engineering synthesis, not a claim that every project follows the same policy
```

The current official pages support the bounded observations used below: NumPy exposes release notes, a dedicated 2.0 migration guide, and downstream-package guidance; Django release notes explicitly call out backwards-incompatible changes and its upgrade guide tells users to read intervening release notes and deprecation timelines; OpenSSL publishes a migration guide including deprecated-function mappings; Kubernetes publishes a deprecation policy and deprecated-API migration guide. NumPy's current downstream guidance also explicitly states that NumPy does not use Semantic Versioning, which is why version numbers alone are not treated as a universal compatibility signal.

## Observed common pattern

1. The library/project primarily documents its own public interface, version, compatibility state, deprecations, removals, and migration path.
2. Major or materially incompatible changes receive a dedicated migration guide rather than being buried only in a generic changelog.
3. Deprecation information is made explicit and often linked to a future removal version or timeline.
4. Breaking changes are grouped or highlighted so downstream users do not have to infer them from an undifferentiated commit list.
5. Migration documentation frequently states the old form, the new/replacement form, and required downstream action.
6. Downstream users/projects are expected to inspect the release/migration information relevant to the versions they move across; the upstream project does not normally maintain an authoritative complete list of every consumer and its exact usage.
7. Version numbers are useful signals but are not sufficient as the only machine-readable compatibility signal because major projects do not all follow the same versioning convention; NumPy explicitly states that it does not use Semantic Versioning.

## Implication for an Agent-oriented library change record

A useful first candidate should preserve normal human-readable release notes but add a stable, consistently structured change summary for downstream Agents. For each material change, record at least:

- stable change ID;
- library version / release;
- change category: compatible feature, behavior change, deprecation, removal, API break, ABI/build break, security-related change, or migration-only note;
- exact affected public symbols / interfaces / configuration / data format where known;
- previous behavior or contract;
- new behavior or contract;
- compatibility statement and which prior versions/usages are affected;
- deprecation and removal version/timeline when applicable;
- replacement or migration action;
- concise before/after example where useful;
- source evidence such as issue/PR/spec/test/documentation refs;
- verification or test guidance for downstream projects.

For a major migration, additionally provide a version-to-version migration guide organized around required downstream actions, not just a chronological list of commits.

## Architectural consequence for TLR-02

The evidence supports the Owner's OR-04/TLR-02 direction:

- library Agent owns accurate, detailed documentation of its own changes;
- downstream project Agent owns project-specific usage discovery, rebuild/upgrade decisions, migration, and tests;
- no default authoritative library-maintained exhaustive consumer reverse index is required;
- an automatically derived consumer-impact view is optional convenience, not required truth, and is not necessary to preserve the Owner's preferred on-demand rebuild model;
- narrowly scoped proactive registration/notification remains an exception candidate for security, fixed migrations, contractual support, or cases where dependency usage cannot be reliably rediscovered.

## Research-depth assessment

`Deep Research` is not required for the current TLR-02 decision. The question is narrow, the Owner's architectural direction is already fixed, and several mature primary-source examples converge on the same documentation pattern. Deep Research would become valuable only if a later task needs a broad empirical comparison across many ecosystems, quantitative evidence about missed migrations, or controlled testing of how different change-record formats affect Agent comprehension and migration accuracy.

## Primary sources

- https://numpy.org/devdocs/release/2.0.0-notes.html
- https://numpy.org/devdocs/numpy_2_0_migration_guide.html
- https://numpy.org/doc/stable/dev/depending_on_numpy.html
- https://docs.djangoproject.com/en/5.2/releases/
- https://docs.djangoproject.com/en/dev/howto/upgrade-version/
- https://docs.djangoproject.com/en/dev/internals/deprecation/
- https://docs.openssl.org/3.6/man7/ossl-guide-migration/
- https://kubernetes.io/docs/reference/using-api/deprecation-policy/
- https://kubernetes.io/docs/reference/using-api/deprecation-guide/
- https://semver.org/
