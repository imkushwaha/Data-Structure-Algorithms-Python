
def printPairs(array):
    for i in array:      # O(n^2)
        for j in array:  # O(n)
            print(str(i) + "," + str(j))  # O(1)

# Overall Time Complexity: O(n^2)