# What is the runtime of the below code?

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + ", " + array[j])


# 1. Counting the iterations
# 1st --------> n - 1
# 2nd --------> n - 2
#        .
#        .
#        .
#        .
# (n-1)+(n-2)+(n-3)+...........2+1
# n(n-1)/2
# Overall Time Complexity is: O(n^2)
