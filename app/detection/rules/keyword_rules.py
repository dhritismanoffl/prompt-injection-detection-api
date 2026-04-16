from typing import Tuple, Optional
from app.detection.rules.base import BaseRule


class KeywordRule(BaseRule):
    def __init__(self):
        # Detection logic is not exposed in the public version
        pass

    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        """
        Public version: keyword-based detection logic is abstracted.
        """
        return False, 0.0, None