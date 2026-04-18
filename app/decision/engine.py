from typing import Dict, Any, List
from app.schemas.response import RiskLevel, Action


class DecisionEngine:
    """
    Public decision logic:
    Simplified fixed-threshold policy.
    """

    HIGH_THRESHOLD = 0.65
    MEDIUM_THRESHOLD = 0.4

    def decide(self, score: float, results: List = None) -> Dict[str, Any]:

        if score >= self.HIGH_THRESHOLD:
            return {
                "risk_level": RiskLevel.HIGH,
                "action": Action.BLOCK
            }

        if score >= self.MEDIUM_THRESHOLD:
            return {
                "risk_level": RiskLevel.MEDIUM,
                "action": Action.FLAG
            }

        return {
            "risk_level": RiskLevel.LOW,
            "action": Action.ALLOW
        }