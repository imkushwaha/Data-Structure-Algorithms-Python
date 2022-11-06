# Greatest Common Divisior
# GCD is the largest positive integer that divides the numbers without a remainder
# we will be using Euclidean algorithm

def gcd(a,b):
    assert int(a) == a and int(b) == b, "The numbers must be integer only"
    if a < 0:
        a = 1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

# Driver Code
result = gcd(48,18)
print(result)

