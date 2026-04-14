from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.schemas.request import ScanRequest
from app.schemas.response import ScanResponse
from app.pipeline.orchestrator import DetectionOrchestrator
from app.core import config
from app.logging.logger import log_risk_event

import traceback  # added

router = APIRouter()
orchestrator = DetectionOrchestrator()


@router.post("/scan", response_model=ScanResponse)
async def scan_prompt(
    request: ScanRequest,
    background_tasks: BackgroundTasks
) -> ScanResponse:
    try:
        result = orchestrator.scan_prompt(request.prompt)

        if result.score >= config.settings.MEDIUM_RISK_THRESHOLD:
            background_tasks.add_task(
                log_risk_event,
                request.prompt,
                result
            )
            result.logged = True

        return result

    except Exception as e:
        print("=== DETECTION ERROR ===")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )