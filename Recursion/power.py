
# How to calculate the power of number using recursion

def power(base, exp):
    assert int(exp) == exp, "The exponent must be integer only"
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * power(base, exp+1)
    return base * power(base, exp-1)


# Driver Code
if __name__ == "__main__":
    base = float(input("Please enter base: "))
    exp = int(input("Please enter exponent: "))
    result = power(base,exp)
    print(f"{base} raise to the power {exp} is {result}")

