
# Question 3 - How to check if any array contains a number in Python

import numpy as np
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)
        
    print("Number is not present!!")

# driver Code
findNumber(myArray,21)