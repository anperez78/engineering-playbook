# Engineering Playbook

Versioned engineering baseline for Claude Code, Python, DDD, testing, OpenSpec and CI.

## Components
- `plugins/engineering-playbook/`: Claude Code plugin (agents and skills).
- `.claude-plugin/marketplace.json`: private marketplace catalog.
- `templates/python-ddd-service/`: starter project.
- `managed/`: centrally owned files synchronized into projects.
- `scripts/sync_playbook.py`: safe allowlist-based synchronizer.
- `.github/workflows/`: repository CI and cross-repository update workflow example.

## Install
1. Host this repository privately in GitHub and replace `YOUR_ORG`.
2. Publish a release and upload the release archive described in `docs/RELEASES-AND-UPDATES.md`.
3. Create a project from `templates/python-ddd-service/`.
4. Install OpenSpec and run `openspec init` (select Claude Code), then review generated files.
5. Add the private marketplace to Claude Code and install the plugin. Example commands; check current Claude Code syntax and authentication for your version:
   ```
   /plugin marketplace add YOUR_ORG/engineering-playbook
   /plugin install engineering-playbook@engineering-playbook
   ```
6. Copy `.github/workflows/project-playbook-update.yml.example` to each consuming project as `.github/workflows/playbook-update.yml`; configure secrets.

## Ownership model
The files listed in `managed/manifest.json` are centrally owned and overwritten by updates. Do not locally edit those files. Put project-specific context in project-owned docs and `CLAUDE.local.md`/project instructions as supported by your setup. `openspec/config.yaml`, source code, and project settings are intentionally not synchronized.

## Updating projects
Projects pin a release in `.engineering-playbook/manifest.json`. A scheduled workflow downloads the latest release, syncs allowlisted files, and opens a PR. Humans review and merge. There is no auto-merge.

## Versioning
Use SemVer:
- PATCH: clarifications and fixes that don't change behavior/policy.
- MINOR: compatible additions to agents, skills, rules or guidance.
- MAJOR: breaking paths, required workflow or policy changes; include migration notes.

For private cross-repository PRs, prefer a GitHub App installation token with least privilege. Never execute untrusted PR code with secrets. See `docs/RELEASES-AND-UPDATES.md`.
