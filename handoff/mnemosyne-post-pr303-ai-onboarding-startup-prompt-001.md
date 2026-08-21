
@GitHub

Receive the Mnemosyne post-PR303 AI-onboarding handoff.

Use:

handoff/mnemosyne-post-pr303-ai-onboarding-handoff-package-001.md

Expected package blob on execution-time latest 08822407d/Mnemosyne@master:

<PACKAGE_BLOB_FROM_MERGED_MNEMOSYNE_242>

Read `commands/receive-mnemosyne-handoff.md`, then the exact handoff package and only its minimum receive evidence.

Return a compact receive report containing:

- package path, package ID and observed blob;
- execution-time master at start and end;
- transferred task ID and role;
- authority and forbidden-action preservation;
- required separate guidance-refresh phase;
- branch-retention obligations;
- whether the receiver is ready to stop after receive.

Do not load Mnemosyne guidance in this receive operation. Do not continue MNEMOSYNE-243, modify repositories, issue G2A, execute A1/HVAL, delete branches, import another route, or infer a task from `handoff/handoff-current.md`.

Stop after the receive report.
