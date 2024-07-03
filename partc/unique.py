# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        current_row = [1] * n

        for _ in range(1, m):
            new_row = [1]

            for j in range(1, n):
                new_row.append(new_row[-1] + current_row[j])

            current_row = new_row

        return current_row[-1]
