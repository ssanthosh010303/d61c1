# Author: Apache X692 Attack Helicopter
# Created on: 02/07/2024
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ""
        n = len(s)
        num_cycles = numRows * 2 - 2

        for row in range(numRows):
            for i in range(row, n, num_cycles):
                result += s[i]

                if 0 < row < numRows - 1:
                    second_index = i + num_cycles - 2 * row

                    if second_index < n:
                        result += s[second_index]

        return result
