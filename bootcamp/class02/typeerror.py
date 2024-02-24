# Example that causes TypeError
try:
    result = len(5)
except TypeError as e:
    print(e)  # Prints the error message