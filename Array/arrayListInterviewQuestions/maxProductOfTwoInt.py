
# Question 4: How to find maxium product of two integers in the array where all elements are positive

import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 67, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,34])

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) +","+ str(array[j])
    print(pairs)
    print(maxProduct)


# Driver Code
if __name__ == "__main__":
    findMaxProduct(myArray)
    