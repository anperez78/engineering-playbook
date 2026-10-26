# Releases and update pull requests

## Create release asset
The update workflow expects an asset `engineering-playbook-<version>.tar.gz` whose root contains `managed/` and `scripts/`.

```bash
VERSION="$(cat VERSION)"
mkdir -p "dist/engineering-playbook-${VERSION}"
cp -R managed scripts "dist/engineering-playbook-${VERSION}/"
tar -czf "dist/engineering-playbook-${VERSION}.tar.gz" \\
  -C "dist/engineering-playbook-${VERSION}" managed scripts
```

Upload the asset to the GitHub Release tagged `v${VERSION}`. This command puts `managed/` and `scripts/` directly at the archive root, matching the example workflow paths.

## Configure each consumer
1. Add `PLAYBOOK_READ_TOKEN` with read-only access to the private playbook repository.
2. Add `PROJECT_AUTOMATION_TOKEN` (prefer a GitHub App installation token) with contents-write and pull-requests-write for that consuming repository.
3. Replace `YOUR_ORG/engineering-playbook`.
4. Copy the workflow example to `.github/workflows/playbook-update.yml`.
5. Ensure `.engineering-playbook/manifest.json` exists and contains `playbook_version`.
6. Run the workflow manually once and inspect the PR before enabling the schedule.

Prefer a narrowly scoped GitHub App token. Avoid broad personal access tokens. Never expose secrets to untrusted fork PR code.

## Synchronizer contract
The synchronizer copies only paths in `managed/manifest.json`. It intentionally does not perform a three-way merge: listed paths are centrally owned. Use unlisted files for project-specific material. A future enhancement could add merge-base hashes and conflict reporting, but explicit ownership is safer for v1.
