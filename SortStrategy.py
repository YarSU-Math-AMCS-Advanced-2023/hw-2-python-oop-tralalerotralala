from abc import ABC, abstractmethod
from typing import List, Dict


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, ads: List[Dict]) -> List[Dict]:
        pass