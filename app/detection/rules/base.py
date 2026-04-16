from abc import ABC, abstractmethod
from typing import Tuple, Optional


class BaseRule(ABC):
    @abstractmethod
    def evaluate(self, text: str) -> Tuple[bool, float, Optional[str]]:
        """
        Returns:
            (triggered, score, flag)
        """
        raise NotImplementedError