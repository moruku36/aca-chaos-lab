# Azure Container Apps Chaos Lab

[English](README.md) | [日本語](README.ja.md)

A controlled chaos-engineering lab for Azure Container Apps and Azure SRE Agent experiments, combining FastAPI, Redis, fault injection, Locust load tests, and Application Insights.

## Local development

```bash
cd src
pip install uv
uv sync --extra dev
REDIS_ENABLED=false uv run uvicorn app.main:app --reload
```

The local no-Redis mode supports initial tests. The deployed Redis endpoint is private to the VNet; use a local Redis instance to exercise Redis behavior from your workstation.

The lab includes fault-injection APIs, infrastructure fault scripts, Locust load scenarios, distributed tracing, and monitoring. Azure deployment, environment variables, API endpoints, alert configuration, and operational limits are documented in the Japanese guide and `docs/`. Fault-injection actions are intended for the controlled lab environment.


## Contents

- [docs/](docs)
- [infra/](infra)
- [scripts/](scripts)
- [src/](src)

## Detailed documentation

The [Japanese guide](README.ja.md) retains the complete original setup instructions, configuration, examples, project status, and limitations. Supporting documents keep their existing language.
