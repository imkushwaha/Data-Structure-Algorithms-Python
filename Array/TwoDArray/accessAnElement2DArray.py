
# Two dimensional array
# a[i][j] ---> i is row index and j is column index

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)

def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): # ------> O(1)
        print("Incorrect index")   # --------------------------------> O(1)
    else:
        print(array[rowIndex][colIndex])  # -------------------------> O(1)

accessElement(twoDArray, rowIndex=1, colIndex=2)

# Time complexity: O(1)
# Space Complexity: O(1)


