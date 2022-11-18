
import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]], np.int64)
print(twoDArray)
print("\n")

new2DArray = np.delete(twoDArray, 0, axis = 0)
print(new2DArray)

# Time Complexity: O(mn)
# if we delete last column or last row then time complexity will be O(1) because in this case we are not moving column or row either right or left
# Space Complexity: O(1)