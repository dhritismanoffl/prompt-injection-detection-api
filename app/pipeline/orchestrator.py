from typing import List, Tuple

from app.detection.rules.contextual_rules import ContextualRule
from app.detection.rules.exfiltration_rules import ExfiltrationRule
from app.detection.rules.jailbreak_rules import JailbreakRule
from app.detection.rules.override_rules import OverrideRule
from app.detection.rules.keyword_rules import KeywordRule
from app.detection.rules.obfuscation_rules import ObfuscationRule

from app.detection.scoring import calculate_score
from app.decision.engine import DecisionEngine

from app.schemas.response import ScanResponse


class DetectionOrchestrator:
    """
    Public-facing simplified orchestrator.
    Executes rules → aggregates score → returns structured response.
    """

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

    def scan_prompt(self, prompt: str) -> ScanResponse:
        text = prompt.strip()

        results: List[Tuple[bool, float, str | None]] = []

        # Run rules
        for rule in self.rules:
            triggered, score, flag = rule.evaluate(text)
            results.append((triggered, score, flag))

        # Aggregate score
        final_score = calculate_score(results)

        # Decision
        decision = self.decision_engine.decide(final_score, results)

        # Extract flags
        flags = [flag for triggered, _, flag in results if triggered and flag]

        return ScanResponse(
            risk_level=decision.get("risk_level", "low"),
            score=final_score,
            flags=flags,
            action=decision.get("action", "allow"),
            logged=False
        )