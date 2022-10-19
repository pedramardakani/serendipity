# Pedram Ashofteh-Ardakani <pedramardakani@pm.me>
#
# Print ways we can pay up 'target' amount with coins of only 'change'.
# Assume we have infinite coins.

import numpy as np

target = 8
change = np.array([5,1,2])

if __name__ == "__main__":

    # Initialize
    done = 0
    results = []
    change.sort()
    direction = -1
    last_element = len(change)-1
    temp = np.zeros_like(change)

    index = last_element
    print(f"Question:\n\t{change}, {target}")

    while done == 0:
        if direction == -1:

            # We're moving left
            remaining = target-temp.dot(change)
            temp[index] = remaining // change[index]
            remaining = target - temp.dot(change)
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

    print("Solutions:")
    for i, f in enumerate(results):
        print('\t', i, f)