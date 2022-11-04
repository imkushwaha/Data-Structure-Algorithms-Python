
def factorial(n: int)-> int:
    assert n >= 0 and int(n) == n, "The number must be positive integer only!"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


# Driver Code
if __name__ == "__main__":
    number = int(input("Please enter your number: "))
    result = factorial(number)
    print(f"Factorial of {number} is {result}")

