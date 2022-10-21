# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>
#
# Test for the following question:
#
# Print ways we can pay up 'bill' with only specified 'change'
# Assume we have infinite coins, and the order doesn't matter.

import unittest
from bill import solve

class TestBillBasic(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(solve([1, 3, 5], 8), 5)
        self.assertEqual(solve([1, 2, 3, 5], 8), 13)

    def test_tricky(self):
        self.assertEqual(solve([5, 1, 3], 8), 5)
        self.assertEqual(solve([3, 5, 2, 1], 8), 13)

    def test_very_tricky(self):
        self.assertEqual(solve([5, 1, 1, 3], 8), 5)
        self.assertEqual(solve([3, 5, 5, 2, 1, 3], 8), 13)
        self.assertEqual(solve([3, 5, 0, 2, 1, 3], 8), 13)


if __name__ == "__main__":
    unittest.main()