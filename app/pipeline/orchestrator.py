from app.preprocessing.cleaner import TextCleaner
from app.detection.rules.override_rules import OverrideRule
from app.detection.rules.exfiltration_rules import ExfiltrationRule
from app.detection.rules.jailbreak_rules import JailbreakRule
from app.detection.rules.obfuscation_rules import ObfuscationRule
from app.detection.rules.contextual_rules import ContextualRule
from app.detection.rules.keyword_rules import KeywordRule
from app.detection.scoring import ScoringEngine
from app.decision.engine import DecisionEngine
from app.schemas.response import ScanResponse


class DetectionOrchestrator:
    """
    Coordinates the full prompt detection pipeline.
    """

    def __init__(self):
        self.cleaner = TextCleaner()
        self.scoring_engine = ScoringEngine()
        self.decision_engine = DecisionEngine()

        self.rules = [
            OverrideRule(),
            ExfiltrationRule(),
            JailbreakRule(),
            ObfuscationRule(),
            ContextualRule(),
            KeywordRule(),
        ]

    def scan_prompt(self, prompt: str) -> ScanResponse:
        """
        Execute detection pipeline:
        Clean -> Detect -> Score -> Decide -> Format
        """
        cleaned_text = self.cleaner.clean(prompt)

        detection_results = [
            rule.evaluate(cleaned_text)
            for rule in self.rules
        ]

        scoring = self.scoring_engine.aggregate(detection_results)

        decision = self.decision_engine.determine(
            scoring["score"],
            scoring["flags"]
        )

        return ScanResponse(
            risk_level=decision["risk_level"],
            score=scoring["score"],
            flags=scoring["flags"],
            action=decision["action"],
            logged=False
        )