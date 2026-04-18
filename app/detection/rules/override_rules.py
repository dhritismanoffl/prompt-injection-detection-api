from typing import Tuple, Optional
from app.detection.rules.base import BaseRule
from app.core.constants import FLAG_INSTRUCTION_OVERRIDE


class OverrideRule(BaseRule):
    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        t = text.lower()

        if (
            "ignore previous instructions" in t
            or "disregard previous instructions" in t
            or "forget all prior instructions" in t
        ):
            return True, 0.7, FLAG_INSTRUCTION_OVERRIDE

        return False, 0.0, None