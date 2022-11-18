from array import *

arr1 = array('i', [1,2,3,4,5,6])

def deleteAnElement(array, value):
    array.remove(value)
    return array


print(deleteAnElement(arr1,3))


# Time Complexity: O(n) because in deletion of element, after deletion all element shifts right or left acccordinly.
# Space Complexity: O(1)