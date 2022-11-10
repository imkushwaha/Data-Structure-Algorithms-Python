# What is the runtime of the below code

def factorial(n):    # ------------------> F(n)
    if n < 0:        #
        return -1    # ------------------> O(1)
    elif n == 0:     #
        return 1     #
    else:
        return n * factorial(n-1)  # -------------------> F(n-1)


# n! = 1*2*3*4.......*n
# 3! = 1*2*3 = 6

# F(n) = O(1) + F(n - 1)
# F(0) = O(1)

# F(n - 1) = O(1) + F((n - 1) - 1)
# F(n - 2) = O(1) + F((n - 2) - 1)

# F(n) = 1 + F(n - 1)
#      = 1 + (1 + F((n - 1) - 1))
#      = 2 + F(n - 2)
#      = 2 + (1 + F((n - 2) - 1))
#      = 3 + F(n - 3)


#      = a +F(n - a)
#   Put a = n because F(0) = 1
#      = n + F(n - n)
#      = n + 1
#      = n

# Time Complexity: O(n)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#