# Type Conversion with Validation
entry_list = input("Enter a list of numbers separated by a comma: ")
numbers_str = entry_list.split(",")
numbers_int = []
try:
    for num in numbers_str:
        numbers_int.append(int(num.strip()))
    print("List of integers:", numbers_int)
except ValueError:
    print("Error: make sure all elements are valid integers.")