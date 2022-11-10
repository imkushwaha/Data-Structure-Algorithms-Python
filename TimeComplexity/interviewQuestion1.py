def foo(array):
    sum_ = 0  # Constant Time Complexity: O(1)
    product = 1  # Constant Time Complexity: O(1)

    for i in array:  # Linear Time Complexity O(n)
        sum_ += i     # Constant Time Complexity: O(1)

    for i in array:  # Linear Time Complexity O(n)
        product *= i # Constant Time Complexity: O(1)
    print("sum = " + str(sum_) + ", Product = " + str(product))  # # Constant Time Complexity: O(1)


arr = [1, 2, 3, 4,  5, 6, 7, 8, 9]
print(foo(arr))

# Overall Time Complexity is : O(n)