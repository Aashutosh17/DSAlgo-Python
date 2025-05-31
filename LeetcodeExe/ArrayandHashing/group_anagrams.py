from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs:
            SortedS = ''.join(sorted(s))
            result[SortedS].append(s)
        return list(result.values())

