"""Fibonacci numbers - Recursion
Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones and the sequence starts from 0 to 1
>>>> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonnaci number cannot be negative number or non integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Driver Code
if __name__ == "__main__":
    number = int(input("Please enter your number: "))
    result = fibonacci(number)
    print(result)

