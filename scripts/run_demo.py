from __future__ import annotations

import json
from pathlib import Path

from srr_public import run_pipeline


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    raw_text = (ROOT / "examples" / "synthetic_case.txt").read_text(encoding="utf-8")
    result = run_pipeline(raw_text)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

