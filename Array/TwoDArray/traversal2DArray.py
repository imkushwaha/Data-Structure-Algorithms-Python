# Traversing Two Dimensiona Array

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)

def traverse2DArray(array):             #
    for i in range(len(array)):         # --------------> O(mn)
        for j in range(len(array[0])):  # --------------> O(n)
            print(array[i][j])          # ---------------> O(1)


traverse2DArray(twoDArray)

# Time Complexity: O(mn) if m==n then it will have quadratic (n^2) time complexity
# Space Complexity: O(1)
