from array import *

arr1 = array('i', [1,2,3,4,5,6])

def searchInArray(array, value):
    for i in array:        # ----------------------------- O(n)
        if i == value:     # ----------------------------- O(1)
            return array.index(value) # ------------------ O(1)

    return "The element does not exist in this array" #--------- O(1)


# Time complexity : O(n)
# Space Complexity: O(1) no extra space used

print(searchInArray(arr1,3))

