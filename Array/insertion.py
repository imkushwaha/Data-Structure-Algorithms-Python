from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.5,1.6])

print(arr1)     

arr1.insert(6,7)

print(arr1)

arr1.insert(0,0)

print(arr1)

arr1.insert(2,9)

print(arr1)

# Time Complexity of array insertion

# In begning: O(n)
# At last: O(1)
# In middle: O(n)
# If array is full: O(n)