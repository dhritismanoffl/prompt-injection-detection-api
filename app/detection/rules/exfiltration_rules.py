from typing import Tuple, Optional
from app.detection.rules.base import BaseRule
from app.core.constants import FLAG_PROMPT_LEAK


class ExfiltrationRule(BaseRule):
    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        t = text.lower()

        if (
            "reveal the system prompt" in t
            or "show hidden instructions" in t
            or "print the system prompt" in t
        ):
            return True, 0.75, FLAG_PROMPT_LEAK

        return False, 0.0, None