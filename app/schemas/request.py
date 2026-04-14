from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Prompt to scan for prompt injection/jailbreak attempts."
    )