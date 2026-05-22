# Architecture Notes

## System Shape

```text
raw case text
  -> extract_fields
  -> validate_fields
  -> repair_fields
  -> calculate_deadlines
  -> route_department
  -> return reviewable state
```

## Design Points

| Point | Why It Matters |
|---|---|
| Shared state object | Keeps a multi-step workflow debuggable |
| Validation before routing | Reduces downstream error propagation |
| Explainable repair log | Makes automated correction reviewable |
| Deadline rules | Turns extracted dates into operational actions |
| Confidence-based routing | Keeps uncertain cases visible |
| Synthetic tests | Protects behavior without external data |

## Module Map

| Module | Responsibility |
|---|---|
| `field_extractor.py` | Extract normalized fields from text |
| `quality_gate.py` | Check missing fields and rule violations |
| `self_repair.py` | Apply deterministic corrections with an audit log |
| `deadline_rules.py` | Calculate reply and completion dates |
| `router.py` | Route cases to review teams |
| `pipeline.py` | Orchestrate the workflow |

