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

import numpy as np
from typing import List

def solve(roots: List[int], target: int) -> List[int]:

    # initialize
    result = []

    # Go through all asked roots (i.e. 2 and 3)
    for j in roots:

        # Create a range starting from the root itself up to the target
        # itself (exclusive) with a step by size of the target.
        for i in range(j, target, j):

            # Put in results
            result.append(i)

    # Make sure to remove duplicates
    result = np.unique(result)

    # We must return a sorted 'list'
    np.sort(result)
    return list(result)
