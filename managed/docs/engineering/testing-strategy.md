# Testing strategy

| Layer | Purpose | Typical tools | Dependencies |
|---|---|---|---|
| Unit | Domain invariants and use cases | pytest | None; use fakes |
| Integration | Persistence and adapters | pytest, disposable services | Test infrastructure |
| Contract | API/event compatibility | schema checks, Schemathesis or Pact | Provider/consumer contracts |
| E2E | Critical journey through running system | HTTP client or Playwright | Test deployment |

Prefer many unit tests, fewer integration tests, and a small critical E2E suite. Test failure behavior, idempotency, retries, authorization and observability—not only happy paths.

CI policy: unit tests on every PR; integration tests on every PR where practical; E2E on a test deployment or release gate. Tests must be deterministic and isolated.
