# What is the runtime of the below code?

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

# b = len(arraB)
# a - len(arrayA)

# Time Complexity: O(ab)

# If both array A and B have equal number of elements then the time complexity would be quadratic i.e O(n^2)