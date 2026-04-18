from typing import Tuple, Optional
from app.detection.rules.base import BaseRule
from app.core.constants import FLAG_JAILBREAK


class JailbreakRule(BaseRule):
    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        t = text.lower()

        if (
            "bypass restrictions" in t
            or "ignore safety guidelines" in t
            or "do not follow previous rules" in t
        ):
            return True, 0.65, FLAG_JAILBREAK

        return False, 0.0, None