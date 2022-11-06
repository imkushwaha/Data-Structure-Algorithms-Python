
def decimalToBinary(n):
    assert int(n) == n, "The Parameter must be integer only"
    if n == 0:
        return 0
    else:
        return (n%2) + 10 * decimalToBinary(n//2)

# Driver Code
result = decimalToBinary(10)
print(result)
