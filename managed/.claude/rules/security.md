---
description: Secure-by-default development requirements
---
- Apply least privilege and deny by default for authorization.
- Validate untrusted input at boundaries; use parameterized queries.
- Never commit credentials, tokens, private keys, production data or secrets in fixtures.
- Avoid logging secrets and sensitive personal data.
- Consider authorization, tenant isolation, injection, SSRF, unsafe deserialization, dependencies and data retention.
- Security-sensitive changes require tests for allowed and denied behavior.
- Do not run destructive commands or modify production systems without explicit authorization.
