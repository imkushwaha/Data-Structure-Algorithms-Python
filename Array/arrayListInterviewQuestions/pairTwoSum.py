# Array List Interview Questions: 2
# Wrtie a program to find all pairs of integers whose sum is equal to a given number.
# [2, 6, 3, 9, 11]   9 -----------------> [6,3]

"""
Few questions one should ask before jump to coding................

- Does array contain only positive or negative numbers?
- If the reverse of the pair is acceptable e.g. can we print both (4,1) and (1,4) if the given sum is 5.
- What if the same pair repeats twice, should we print it every time?
- Do we need to print only distinct pairs? does (3,3) is a valid pair for given sum of 6
- How big is the array?

"""
# LeetCode 1 - Two Sum ((2,2) and (3,3) is not accepted)

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

# Driver Code

myList = [1,2,3,2,3,4,5,6]
findPairs(myList,6)

