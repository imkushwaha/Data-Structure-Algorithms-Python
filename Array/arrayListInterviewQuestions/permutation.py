# Question 6 - Permutation
# Given two list is permutation of one another or not (for permutation lists should contain same element irrespective of any order same goes with string also)

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


list1 = ['a', 'b', 'c']
list2 = ['c', 'a', 'd']
print(permutation(list1,list2))
