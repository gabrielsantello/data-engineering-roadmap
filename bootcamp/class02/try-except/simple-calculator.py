# Simple Calculator
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/' and num2 != 0:
        result = num1 / num2
    else:
        print("Invalid operator or division by zero.")
    print("Result:", result)
except ValueError:
    print("Error: Invalid entry. Make sure to enter numbers.")
