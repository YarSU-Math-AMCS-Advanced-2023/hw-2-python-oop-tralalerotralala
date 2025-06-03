from SortStrategy import SortStrategy
from typing import List, Dict


class SortContext:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_ads(self, ads: List[Dict]) -> List[Dict]:
        return self._strategy.sort(ads)