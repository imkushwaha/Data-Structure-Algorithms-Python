"""
Two Dimensional Array

An array with a bunch of values having been declared with double index.

a[i][j] --> i and j between 0 and n

i for row index and 
j for coumn index

2D array example:

1 33 55 91 20 51 62 74 13
5 4  10 11 8  11 68 87 12

When we create an array, we:
- Assign it to a variable
- Define the type of elements that it will store
- Define its size (the maximum numbers of elements)

Example we are going to use:

Day 1 - 11, 15, 10, 6
Day 2 - 10, 14, 11, 5
Day 3 - 12, 17, 12, 8
Day 4 - 15, 18, 14, 9

"""

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)

# Time Complexit: O(1), creating array in one go
# Time Complexity: O(n), when create an empty array and then assign n values to it
# Space Complexity: O(m*n) m --> row count and n --> column count