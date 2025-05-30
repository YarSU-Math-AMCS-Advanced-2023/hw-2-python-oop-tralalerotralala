from SortStrategy import SortStrategy
from typing import List, Dict


class SortByCost(SortStrategy):
    def __init__(self, ascending=True):
        self.ascending = ascending

    def sort(self, ads: List[Dict]) -> List[Dict]:
        return sorted(ads, key=lambda x: float(x['cost']),
                      reverse=not self.ascending)