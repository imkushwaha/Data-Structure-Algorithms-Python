# What is the runtime of the below code

def reverse(array):
    for i in range(0, int(len(array)/2)):   # O(n/2) ---> O(n) , removed constant
        other = len(array) - i - 1          # O(1)
        temp = array[i]                     # O(1)
        array[i] = array[other]             # O(1)
        array[other] = temp                 # O(1)
    print(array)                            # O(1)

# Time Complexity: O(n)

