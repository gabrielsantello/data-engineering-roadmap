def recursive_sum(n):
    # Base case: if n is 0, there's nothing more to add
    if n == 0:
        print("Base case reached: recursive_sum(0) = 0")
        return 0
    else:
        # Recursive case: n plus the sum of numbers up to n-1
        print(f"Calculating recursive_sum({n}): {n} + recursive_sum({n-1})")
        return n + recursive_sum(n-1)

# Example of usage
num = 5
print(f"Calculating the sum of numbers up to {num}:")
result = recursive_sum(num)
print(f"The sum of numbers up to {num} is {result}")

# if __name__:
#     recursive_sum(5)