# 2125. Number of Laser Beams in a Bank

# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Return the total number of laser beams in the bank.
from unittest import TestCase, main
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row = 0
        total = 0
        for row in bank:
            row = row.count("1")
            total += prev_row * row
            if row:
                prev_row = row
        return total

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.cases = [
            (["11100000000", "11100000000", "11100000000", "11111111111"], 51),
            (["1111", "1111", "1111"], 32),
            (["101", "010", "101"], 4),
            (["111", "111", "111"], 18),]
        
    def test_numberOfBeams(self):
        for case, expected in self.cases:
            with self.subTest(msg=case):
                self.assertEqual(self.solution.numberOfBeams(case), expected)
            
            
if __name__ == "__main__":
    main()
    