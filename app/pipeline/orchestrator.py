from typing import Dict, Any

from app.schemas.request import ScanRequest

from app.detection.rules.contextual_rules import ContextualRule
from app.detection.rules.exfiltration_rules import ExfiltrationRule
from app.detection.rules.jailbreak_rules import JailbreakRule
from app.detection.rules.override_rules import OverrideRule
from app.detection.rules.keyword_rules import KeywordRule
from app.detection.rules.obfuscation_rules import ObfuscationRule

from app.detection.scoring import calculate_score
from app.decision.engine import DecisionEngine


class Orchestrator:
    def __init__(self):
        self.rules = [
            OverrideRule(),
            JailbreakRule(),
            ExfiltrationRule(),
            ContextualRule(),
            KeywordRule(),
            ObfuscationRule(),
        ]
        self.decision_engine = DecisionEngine()

    def run(self, request: ScanRequest) -> Dict[str, Any]:
        text = request.prompt

        results = []

        # Execute all rules
        for rule in self.rules:
            triggered, score, flag = rule.evaluate(text)
            results.append((triggered, score, flag))

        # Calculate score (stubbed in public version)
        final_score = calculate_score(results)

        # Decision (stubbed behavior expected)
        decision = self.decision_engine.decide(final_score, results)

        # Return standardized response
        return {
            "risk_level": decision.get("risk_level", "low"),
            "score": final_score,
            "flags": [],
            "action": decision.get("action", "allow"),
        }