# Shared engineering baseline

Follow centrally managed rules in `.claude/rules/` and standards in `docs/engineering/`.

## Project-specific context
- Read the project README and architecture docs before changing design.
- For non-trivial behavior changes, use OpenSpec: proposal/specs/design/tasks, implementation, verification, archive.
- Keep project-specific facts in project-owned docs and `openspec/config.yaml`.
- Centrally managed files are not for local editing. Document justified exceptions in `docs/engineering/overrides.md`.

## Required workflow
1. Understand behavior, acceptance criteria and relevant domain model.
2. For significant changes, agree on OpenSpec artifacts before implementation.
3. Respect domain boundaries and dependency direction.
4. Add unit tests; add integration, contract or E2E tests when a boundary or critical journey is affected.
5. Run formatting, lint, typing and tests.
6. Review security, observability, compatibility, migration and rollback.
