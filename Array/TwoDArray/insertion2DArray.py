
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)
print("\n")

newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
print(newTwoDArray)
print("\n")

newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print("\n")

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)  # Here Time Complexity: O(1)
print(newTwoDArray)

# Time Complexity: O(mn), m --> number of rows and n --> number of columns
# if we insert row or column at end of array then time complexity: O(1)
# Space Complexity: O(1)