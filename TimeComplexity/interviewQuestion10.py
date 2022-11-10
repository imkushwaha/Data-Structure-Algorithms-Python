# What is the runtime of the below code?

def powerof2(n):
    if n < 1:       #
        return 0    #
    elif n == 1:    # -------------------> O(1)
        print(1)    #
        return 1    #
    else:
        prev = powerof2(int(n/2))   # --------------> O(logn)
        curr = prev*2     #
        print(curr)       # -----------------------------------> O(1)
        return curr       #


# Time Complexity : O(logn)
# Because parameter n is divided by two at each step