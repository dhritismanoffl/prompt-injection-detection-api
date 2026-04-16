from typing import Dict, Any, List


class DecisionEngine:
    """
    Public version: decision logic is abstracted.
    """

    def decide(self, score: float, results: List = None) -> Dict[str, Any]:
        return {
            "risk_level": "low",
            "action": "allow"
        }