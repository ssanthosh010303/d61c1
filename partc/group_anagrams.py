# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
from typing import List
from collections import defaultdict

class Solution:
    def generate_map(self, s: str) -> str:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        result = []

        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i + ord('a')), str(count[i])])

        return ''.join(result)

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.generate_map(s)].append(s)

        result.extend(groups.values())

        return result
