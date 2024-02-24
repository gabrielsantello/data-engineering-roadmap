# Palindrome Checker
entry = input("Enter a word or phrase: ")
if isinstance(entry, str):
    formatted = entry.replace(" ", "").lower()
    if formatted == formatted[::-1]:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
else:
    print("Invalid entry. Please enter a word or phrase.")