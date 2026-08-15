# ChatGPT / GitHub Repository Access vs Sync Selection — 2026-08 Observation

```yaml
observation_id: MNE-PLATFORM-GITHUB-ACCESS-SYNC-2026-08-001
task_id: MNEMOSYNE-212
status: current_official_documentation_plus_mechanical_observation
observed_at: 2026-08-14
execution_source: false
provider_source:
  publisher: OpenAI
  title: Connecting GitHub to ChatGPT
  url: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
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
  read_access_observed: true
  write_access_observed: true
  V0_final_head: e8e3296922185b4b70997c2351d6f39423f2cd4f
backend_status: unknown_or_not_attestable
```

## Conclusion

The GitHub-side installation authorization and the ChatGPT-side repository sync selection are separate controls.

OpenAI's current help article states that, after GitHub is connected, ChatGPT may ask which repositories the user most often uses so they can be synchronized for speed and quality. It explicitly states that this sync selection is separate from GitHub repository access: ChatGPT can still access repositories permitted in GitHub even when those repositories are not selected for sync.

The observed V0 run is consistent with that documentation:

- the Owner reported that the newly created repository was not selected in the ChatGPT sync/settings list;
- the current GitHub connector nevertheless resolved the exact repository and reported read/write-capable permissions;
- the connector successfully wrote and later read the V0 evidence bundle.

The most likely operational explanation is therefore that the relevant GitHub App installation was authorized for all repositories, or otherwise already included the newly created repository. A GitHub installation configured for all repositories normally includes subsequently created repositories under that installation scope. The ChatGPT-side sync choice affects synchronization/indexing preference and may affect visibility, latency, or search quality, but it is not the underlying repository permission grant.

## Important distinctions

1. **GitHub repository access**
   - controlled through the GitHub-side app installation/repository-access configuration;
   - determines whether the connected app can access a repository at all;
   - can be configured for all repositories or selected repositories.

2. **ChatGPT repository sync selection**
   - a separate selection intended to improve speed and quality for frequently used repositories;
   - is not required for access when GitHub has already authorized the repository;
   - may still affect when a newly created repository appears in some search/index-based product views.

3. **Read versus write capability**
   - the ordinary ChatGPT GitHub app described in the cited help article is presented as a read/search integration;
   - repository mutation in the current environment is exposed through the GitHub/Codex-capable connector surface;
   - actual access for this run is established by connector permissions and successful repository writes, not by assuming every ChatGPT GitHub surface has identical mutation capability.

4. **Backend identity**
   - this observation establishes product-surface permission behavior and repository effects;
   - it does not establish the hidden served-model/backend identity.

## Limits and revalidation rule

This is a current product/platform observation, not a permanent invariant.

Recheck when:

- the GitHub App installation is changed from all repositories to selected repositories;
- an organization or enterprise administrator introduces an approval restriction;
- the repository becomes private or changes ownership;
- the ChatGPT/Codex GitHub connection is disconnected or reinstalled;
- a later product surface cannot resolve a repository that GitHub appears to authorize;
- OpenAI changes the documented relationship between access and sync.

A missing repository in ChatGPT search does not by itself prove missing GitHub permission; indexing and display delay should be considered separately. Conversely, platform permission does not constitute Owner authorization for a particular task or write.