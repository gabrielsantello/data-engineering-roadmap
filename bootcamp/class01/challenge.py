CONSTANT_BONUS = 1000

# 1) Prompt the user to enter their name
user_name = input("Enter your name: ")

# 2) Prompt the user to enter their salary
# Convert the input to a floating-point number
user_salary = float(input("Enter your salary: "))

# 3) Prompt the user to enter the bonus received
# Convert the input to a floating-point number
user_bonus = float(input("Enter your bonus: "))

# 4) Calculate the final bonus value
bonus_value = CONSTANT_BONUS + user_salary * user_bonus

# 5) Print a personalized message including the user's name and bonus value
print(f"The user {user_name} has a bonus of {bonus_value}")

# Bonus: How many bugs and risks can you identify in this program?