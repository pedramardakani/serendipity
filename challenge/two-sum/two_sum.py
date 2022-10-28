# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>
#
# My solution to LeetCode 'Two Sum' problem:
#     https://leetcode.com/problems/two-sum
#
# For some examples, see the test file, and to run it use:
#     $ python3 test_two_sum.py


from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    for i, n in enumerate(nums):

      # Instead of blindly adding numbers in brute force, let's
      # see if we can find the complement in the same 'nums'
      test = target - n

      try:

        # Check if we can find the complement index in the 'nums'
        # list.
        j = nums.index(test)

      except ValueError as err:
        # If we can't find the number in list, 'index' throws a
        # ValueError, let's catch that and try with the next
        # number
        continue

      # Check if we're reading the exact same position in the list
      if i == j:

        try:

          # Clip the previous part of the list so that 'index'
          # can find the other instances.
          j = nums[i+1:].index(test)

          # The list was clipped, so take the clipped length into
          # account as well.
          j += i+1

        except ValueError as err:

          # Can't find another number in the 'nums' list that can
          # satisfy the criteria. So let's go to the next number.
          continue

      return [i, j]
