# Similarities
# 1. Both data structures are mutable.
# 2. Both can be indexed and iterated through.
# 3. They can be both sliced.

# Difference
# 1. List contain different data types but array contain a single data type
# 2. Array supports arithmetic operation but list does not support.

import numpy as np

array = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]

# Array contain only single data type
array1 = np.array([1,2,3,4,5,6,7,"a"])  # you will see that all int element will also get converted to string data type
print("Array:",array1)
print("\n")
mylist1 = [1,2,3,4,5,6,7,"q"]
print("List:",mylist1)
print("\n")

# Array support arithmetic operation
print("Array Support arithmetic operation:", array/2)
print("\n")

# But List does not support arithmetic operation
#print(myList/2)


a=[1,2,3,4,5]
print(a[3:0:-1])