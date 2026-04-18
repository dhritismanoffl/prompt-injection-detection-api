from fastapi import APIRouter, HTTPException

from app.schemas.request import ScanRequest
from app.schemas.response import ScanResponse
from app.pipeline.orchestrator import DetectionOrchestrator

import traceback


router = APIRouter()
orchestrator = DetectionOrchestrator()


@router.post("/scan", response_model=ScanResponse)
async def scan_prompt(request: ScanRequest) -> ScanResponse:
    try:
        return orchestrator.scan_prompt(request.prompt)

    except Exception:
        print("=== DETECTION ERROR ===")
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Internal detection error"
        )