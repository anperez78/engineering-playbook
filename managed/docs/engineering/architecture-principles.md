# Architecture principles

Default to a modular monolith with explicit domain/application/infrastructure/API boundaries until scale, deployment, ownership or reliability requirements justify another topology.

Suggested package structure:
```text
src/<package>/
  domain/          # entities, value objects, events, domain services
  application/     # use cases and ports
  infrastructure/ # persistence, messaging, external adapters
  api/             # HTTP/API adapters
```

DDD guidelines:
- Use ubiquitous language in names, code and specs.
- Entities have identity; value objects compare by value and should be immutable where practical.
- Aggregates enforce invariants within explicit transaction boundaries.
- Repository interfaces are application/domain-facing ports; implementations live in infrastructure.
- Domain events represent meaningful business facts, not arbitrary internal calls.
- Avoid forcing tactical DDD patterns onto simple CRUD behavior.

ADRs should record context, decision, alternatives and consequences.
