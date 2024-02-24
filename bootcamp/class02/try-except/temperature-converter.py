# Temperature Converter
try:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
except ValueError:
    print("Please enter a valid number for the temperature.")