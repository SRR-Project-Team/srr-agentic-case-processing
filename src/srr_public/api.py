from __future__ import annotations

from pydantic import BaseModel

from .pipeline import run_pipeline


class CaseRequest(BaseModel):
    raw_text: str


def create_app():
    from fastapi import FastAPI

    app = FastAPI(
        title="SRR Agentic Case Processing Public Demo",
        version="0.1.0",
        description="Reference API for case extraction, routing, deadline calculation, and quality checks.",
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "mode": "synthetic-public-demo"}

    @app.post("/process-case")
    def process_case(request: CaseRequest) -> dict[str, object]:
        return run_pipeline(request.raw_text)

    return app


app = create_app()
