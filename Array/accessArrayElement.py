# Access array elemeny

# How can we tell the computer which particular value we would like to access?

# <array>[index]

from array import *

arr1 = array('i', [1,2,3,4,5,6])

def accessElement(array,index):
    if index > len(array):     # O(1)
        print("There is not any element in this index")  # O(1)
    else:
        print(array[index])   # O(1)

accessElement(arr1,2)

accessElement(arr1,9)


# Time and Space Complexity:

# Constant time complexity 

# Space Complexity: constant, no extra space is used here

