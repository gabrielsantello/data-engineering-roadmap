# Example that causes TypeError
try:
    result = len(3)
    print(result)
except TypeError as e:
    print(e)
else:
    print("everything went well")
finally:
    print("the important thing is to participate")

number = int(input("Enter a number:"))
if isinstance(number, int):
    print("The variable is an integer.")
else:
    print("The variable is not an integer.")