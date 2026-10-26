import os
import httpx
import pytest

pytestmark = pytest.mark.e2e

@pytest.mark.skipif(not os.getenv("E2E_BASE_URL"), reason="E2E_BASE_URL not configured")
def test_deployed_health_endpoint() -> None:
    response = httpx.get(f"{os.environ['E2E_BASE_URL'].rstrip('/')}/health", timeout=10)
    assert response.status_code == 200
