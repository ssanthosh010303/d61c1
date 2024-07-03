# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = 0
        n = len(nums)

        for i in range(n):
            if i > last_position:
                return False

            last_position = max(last_position, i + nums[i])

            if last_position >= n - 1:
                return True

        return last_position >= n - 1
