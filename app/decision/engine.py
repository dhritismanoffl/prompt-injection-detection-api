from typing import Dict, Any, List

from app.core import config, constants
from app.schemas.response import RiskLevel, Action


class DecisionEngine:
    """
    Maps risk scores + flags to final risk/action decisions.
    """

    def determine(self, score: float, flags: List[str] = None) -> Dict[str, Any]:
        conf = config.settings
        flags = flags or []

        # --- HARD BLOCK (high confidence attack patterns) ---
        if (
            constants.FLAG_INSTRUCTION_OVERRIDE in flags
            and constants.FLAG_PROMPT_LEAK in flags
        ):
            return {
                "risk_level": RiskLevel.HIGH,
                "action": Action.BLOCK
            }

        # --- SCORE-BASED DECISION ---
        if score >= conf.HIGH_RISK_THRESHOLD:
            return {
                "risk_level": RiskLevel.HIGH,
                "action": Action.BLOCK
            }

        if score >= conf.MEDIUM_RISK_THRESHOLD:
            return {
                "risk_level": RiskLevel.MEDIUM,
                "action": Action.FLAG
            }

        return {
            "risk_level": RiskLevel.LOW,
            "action": Action.ALLOW
        }