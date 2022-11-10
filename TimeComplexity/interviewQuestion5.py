# What is the runtime of the below code

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + ", " + str(arrayB[j]))

# a = len(arrayA)
# b = len(arrayB)

# 100000 units of work is still constant

# Time Complexity: O(ab)

