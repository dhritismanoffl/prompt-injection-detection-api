from enum import Enum
from typing import List

from pydantic import BaseModel


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Action(str, Enum):
    ALLOW = "allow"
    FLAG = "flag"
    BLOCK = "block"


class ScanResponse(BaseModel):
    risk_level: RiskLevel
    score: float
    flags: List[str]
    action: Action
    logged: bool