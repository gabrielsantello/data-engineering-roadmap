# Asks the user to enter their name
try:
    name = input("Enter your name: ")

    # Checks if the name is empty
    if len(name) == 0:
        raise ValueError("The name cannot be empty.")
        exit()
    # Checks if there are numbers in the name
    elif any(char.isdigit() for char in name):
        raise ValueError("The name should not contain numbers.")
        exit()
    else:
        print("Valid name:", name)
except ValueError as e:
    print(e)
    exit()

# Asks the user to enter the value of their salary and converts it to float
try:
    salary = float(input("Enter the value of your salary: "))
    if salary < 0:
        print("Please enter a positive value for the salary.")
except ValueError:
    print("Invalid entry for salary. Please enter a number.")
    exit()

# Asks the user to enter the value of the bonus received and converts it to float
try:
    bonus = float(input("Enter the value of the bonus received: "))
    if bonus < 0:
        print("Please enter a positive value for the bonus.")
except ValueError:
    print("Invalid entry for bonus. Please enter a number.")
    exit()

received_bonus = 1000 + salary * bonus  # Simple example of KPI

# Prints the information for the user
print(f"{name}, your salary is €{salary:.2f} and your final bonus is €{received_bonus:.2f}.")