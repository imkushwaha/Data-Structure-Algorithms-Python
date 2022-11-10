# What is the runtime of the below code

def allFib(n):
    for i in range(n):
        print(str(i) + ":, " + str(fib(i)))


def fib(n):                       #
    if n <= 0:                    #
        return 0                  #
    elif n == 1:                  # --------------Time Complexity: branches^depth = O(2^n)
        return 1                  #
    else:                         #
        fib(n - 1) + fib(n - 2)   #



# Now, Time Complexity of first block:
# fib(1) ----------> 2^1 steps  .
# fib(2) ----------> 2^2 steps  .
# fib(3) ----------> 2^3 steps  .
# fib(4) ----------> 2^4 steps  .----------------Total Work = 2^1 + 2^2 + 2^3 + .....2^n
#                                                           = 2^n+1 = 2^n
#                                                Time Complexity: 2^n
#                               .
#                               .
# fib(n) -----------> 2^n steps .