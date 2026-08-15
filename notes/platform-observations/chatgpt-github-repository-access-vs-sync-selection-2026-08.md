# ChatGPT / GitHub Repository Access vs Sync Selection — 2026-08 Observation

```yaml
observation_id: MNE-PLATFORM-GITHUB-ACCESS-SYNC-2026-08-001
task_id: MNEMOSYNE-212
status: current_official_documentation_plus_mechanical_observation
observed_at: 2026-08-14
execution_source: false
provider_sources:
  - publisher: OpenAI
    title: Connecting GitHub to ChatGPT
    url: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
    accessed_at: 2026-08-14
  - publisher: GitHub
    title: Installing a GitHub App from a third party
    url: https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party
    accessed_at: 2026-08-14
mechanical_observation:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  repository_visibility: public
  repository_id: "1334713395"
  connector_reported_permissions:
    pull: true
    push: true
    maintain: true
    admin: true
  owner_reported_ChatGPT_sync_checkbox: not_selected
  owner_reported_GitHub_installation_scope: all_repositories
  read_access_observed: true
  write_access_observed: true
  V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
backend_status: unknown_or_not_attestable
```

## Conclusion

The GitHub-side installation authorization and the ChatGPT-side repository sync selection are separate controls.

OpenAI's current help article explicitly states that the sync selection used to improve speed and quality is separate from GitHub repository access: ChatGPT can still access repositories permitted in GitHub even when they are not selected for sync.

GitHub's installation documentation separately describes the underlying app-access choice as `All repositories` or `Only select repositories`.

The observed V0 run is consistent with the Owner's recollection that the relevant ChatGPT/Codex GitHub installation was granted all-repository access:

- the newly created repository was not selected in the ChatGPT sync/settings list;
- the current connector nevertheless resolved the exact repository and reported read/write-capable permissions;
- it successfully wrote and later read the V0 evidence bundle.

The strongest claim supported for this run is therefore:

> The relevant GitHub-connected installation had effective access to the new repository, while the ChatGPT sync selection was not required for that access.

The Owner's all-repositories installation choice is the most direct explanation. This record does not independently expose the installation ID or its raw GitHub configuration page, so it does not claim to mechanically attest that configuration beyond the Owner report and observed repository permissions/effects.

## Important distinctions

### 1. GitHub repository access

- controlled through the GitHub-side app installation/repository-access configuration;
- determines whether the app installation can access a repository;
- GitHub exposes `All repositories` and `Only select repositories` choices;
- organization/enterprise approval or later permission changes may further restrict access.

### 2. ChatGPT repository sync selection

- a separate choice intended to improve speed and quality for frequently used repositories;
- not required for access when GitHub has already permitted the repository;
- may affect when a new repository appears in search/index-oriented product views;
- OpenAI documents a normal display delay and possible GitHub indexing delay for new repositories.

### 3. Read versus write capability

- the ordinary ChatGPT GitHub app described in the OpenAI help article is presented as a read/search integration;
- repository mutation in the current environment is exposed through a GitHub/Codex-capable connector surface;
- actual write capability for this run is established by connector-reported permissions and successful commits, not by assuming every ChatGPT GitHub surface has identical permissions.

### 4. Task authority

- platform access is not task authorization;
- the connector's ability to write a repository never substitutes for an exact Owner-approved write scope.

### 5. Backend identity

- this observation establishes product-surface permission behavior and repository effects;
- it does not establish the hidden served-model/backend identity.

## Limits and revalidation rule

This is a current product/platform observation, not a permanent invariant.

Recheck when:

- the relevant GitHub App installation changes from all repositories to selected repositories;
- an organization or enterprise administrator introduces an approval restriction;
- repository ownership or visibility changes;
- ChatGPT/Codex GitHub is disconnected, reinstalled or granted a different installation;
- a later product surface cannot resolve a repository that GitHub appears to authorize;
- OpenAI changes the documented relationship between access and sync.

A missing repository in ChatGPT search does not by itself prove missing GitHub permission; indexing and display delay should be considered separately. Conversely, successful access to one repository does not prove universal access to every repository or authorize any future write.