# Question 1 - Missing Number


def findMissing(list):
    if list[0] == 0:
        n = len(list)
    else:
        n = max(list)
    sum_of_n_natural_number = (n*(n+1))/2
    actual_sum_of_array = sum(mylist)
    missing_number = sum_of_n_natural_number - actual_sum_of_array
    return missing_number


# Driver Code
mylist = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25]
missingNumber = findMissing(mylist)
print("The Missing Number is: ", missingNumber)