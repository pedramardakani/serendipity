import unittest
from two_sum import twoSum

class TestTwoSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual( twoSum([3,2,4],6), [1,2] )
        self.assertEqual( twoSum([2,7,11,15],9), [0,1] )

    def test_with_duplicate_values(self):
        self.assertEqual( twoSum([3,3],6), [0,1] )


if __name__ == "__main__":
    unittest.main()
