"""Question: What are the multiples of a given set under a target number?

Example: Multiples of 3 and 5, below 10: [3, 5, 6, 9]

Copyright (C) 2022 Pedram Ashofteh-Ardakani <pedramardakani@pm.me>

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.

"""

import unittest

from multi import solve

class TestCases(unittest.TestCase):

    def test_solve_3_and_5_target_10(self):
        self.assertEqual( solve([3,5], 10), [3, 5, 6, 9] )

    def test_solve_3_and_5_target_20(self):
        self.assertEqual( solve([3,5], 20),
                          [3, 5, 6, 9, 10, 12, 15, 18])

    def test_solve_5_and_3_target_30(self):
        self.assertEqual( solve([5,3], 30),
                          [3, 5, 6, 9, 10, 12, 15, 18,
                           20, 21, 24, 25, 27] )

    def test_solve_5_and_7_target_30(self):
        self.assertEqual( solve([5,7], 30),
                          [5, 7, 10, 14, 15, 20, 21, 25, 28])

if __name__ == "__main__":
    unittest.main()
