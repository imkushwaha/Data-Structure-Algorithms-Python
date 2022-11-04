
def sumofDigits(n:int):
    assert n >= 0 and int(n) == n , "The number has to be a positive integer only"
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(n//10)

# Driver Code
if __name__ == "__main__":
    number = int(input("Please enter your number: "))
    result = sumofDigits(number)
    print(f"Sum of digits of number {number} is {result}")
