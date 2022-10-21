# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>
#
# Print ways we can pay up 'bill' with only specified 'change'
# Assume we have infinite coins, and the order doesn't matter.
#
# For a demo just run '$ python3 bill_test.py'

import numpy as np
from typing import List

def solve(change: List[int], bill: int) -> int:

    # Initialize
    done = 0
    results = []
    direction = -1

    # Remove impossible changes of 'zero' and negative
    # Sort so we can go through them in descending order
    # Also, np.unique casts 'change' to a numpy array as well
    sorted_change = np.unique(change)
    sorted_change = np.delete(change, np.argwhere( (change <= 0) ))
    np.sort(sorted_change)

    # Initially use the 'last_element' to start solving the problem
    last_element = len(sorted_change)-1

    # Keep a temporary array of the current situation so we can decide for
    # the next steps. Starting with all zeros, which means, 'zero' number
    # of each change
    temp = np.zeros_like(sorted_change)

    index = last_element
    print(f"\n> Change {bill} bill using {change} bills")
    while done == 0:
        if direction == -1:

            # We're moving left
            remaining = bill-temp.dot(sorted_change)
            temp[index] = remaining // sorted_change[index]
            remaining = bill - temp.dot(sorted_change)
            if remaining == 0:

                # Got an answer, save!
                results.append(temp.copy())
                if index != 0:

                    # We're not at the bottom, decrement this element and move left
                    temp[index] = temp[index] - 1
                    index -= 1
                else:

                    # Zero this element and move right
                    direction = 1
                    temp[index] = 0

            elif index == 0:

                # Reached the bottom, zero this index and move right
                direction = 1
                temp[index] = 0
                index += 1

            else:

                # We can still go left
                index -= 1

        if direction == 1:

            # We're moving right
            if temp[index] != 0:

                # Non-zero value, decrement and move left
                temp[index] = temp[index] - 1
                direction = -1
                index -= 1

            else:

                if index == last_element:
                    # Zero, also, we're all the way to right, can't move, we're done!
                    done = 1
                else:
                    index += 1

    for i, f in enumerate(results):
        print(f'  Solution #{1+i:02d}: {f} . {sorted_change} = '
              f'{f.dot(sorted_change)}')

    return len(results)
