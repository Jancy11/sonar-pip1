# Program to check if a number is odd or even

# Input: User provides a number
number = int(input("Enter a number: "))

# Check if the number is even
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")
