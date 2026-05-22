# Public Scope

## Purpose

This repository provides a compact reference implementation of the SRR case-processing workflow.

It uses synthetic examples and public-facing documentation so the core engineering pattern can be reviewed without relying on external systems.

## Included

| Category | Purpose |
|---|---|
| Architecture image | Show system-level design |
| Reference modules | Show workflow decomposition |
| Unit tests | Show expected behavior |
| Synthetic examples | Make the demo runnable |
| API wrapper | Show a clean service boundary |

## Not Included

| Category | Reason |
|---|---|
| Real operational records | Data privacy |
| Cloud deployment settings | Environment-specific configuration |
| Credentials or secret files | Security |
| Prompt templates | Project-specific implementation detail |
| Internal workflow notes | Operational context |

## Principle

```text
Expose the engineering pattern.
Keep data, credentials, and environment-specific configuration out of scope.
```

