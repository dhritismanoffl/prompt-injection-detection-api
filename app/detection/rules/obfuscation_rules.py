from typing import Tuple, Optional
from app.detection.rules.base import BaseRule


class ObfuscationRule(BaseRule):
    def __init__(self):
        # Detection logic is not exposed in the public version
        pass

    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        """
        Public version: obfuscation detection logic is abstracted.
        """
        return False, 0.0, None