# Searching Two Dimensional Array

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)

def search2DArray(array, value):
    for i in range(len(array)):         # ------------------> O(mn)
        for j in range(len(array[0])):  # ------------------> O(n)
            if array[i][j] == value:    # ------------------> O(1)
                return 'The value is located at index ' + str(i) + " "+str(j)

    return 'The element is not found'


print(search2DArray(twoDArray, 14))


# Time Complexity: O(mn) if m==n then it will have quadratic (n^2) time complexity
# Space Complexity: O(1)