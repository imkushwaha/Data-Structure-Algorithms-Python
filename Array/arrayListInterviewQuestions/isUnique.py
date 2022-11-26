# Question 5 - Is Unique: Implement an algorithm to determine if a list has all unique characters, using python list

myList = [1,2,3,45,23]

"""Tips:
step 1: Create empty list
Step 2: Loop through given list
Step 3: In each visit check if the visited element is in our newly created list and save the visited

"""

def isUnique(myList):
    temp = []
    for i in myList:
        if i in temp:
            print("Repeated Element is:", i)
        else:
            temp.append(i)

    if temp == myList:
        print("Given list has all unique values..")

# Driver Code
isUnique(myList=myList)