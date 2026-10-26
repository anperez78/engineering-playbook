# Python DDD Service Starter

Baseline: Python 3.12+, FastAPI, pytest, Ruff, mypy and OpenSpec.

## Bootstrap
1. Create a repository from this folder.
2. Replace `your_service` and `your-service`.
3. Create a venv and install `pip install -e ".[dev]"`.
4. Run `openspec init`, select Claude Code, review and commit generated files.
5. Install the private engineering-playbook plugin.
6. Add managed files from a trusted playbook release and configure the update workflow/secrets.

## Commands
```bash
ruff format --check .
ruff check .
mypy src
pytest -m "not integration and not e2e"
pytest -m integration
pytest -m e2e
```

Integration and E2E examples are marked; adapt them to actual infrastructure and deployment.
