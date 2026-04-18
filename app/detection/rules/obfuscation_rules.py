from typing import Tuple, Optional
from app.detection.rules.base import BaseRule


class ObfuscationRule(BaseRule):
    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        return False, 0.0, None