##############################
# Lab3
# Author name: Micheal Cini
# Student ID: 218672964
# Email address: cini15@my.yorku.ca
# Section A
##############################

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")
print(r"(1) One way or (2) round trip?")
trip = input("Enter 1 or 2: ")
tripCost = 3.50
tripType = "round trip"
if trip == "1":
    tripCost = 1.80
    tripType = "one way"

print("Select Age Range:\n(1) Under 12\n(2) 13-64\n(3) 65 or older")
age = input("Enter 1, 2 or 3: ")
ageCost = "full fare"
if age == "1" or age == "3":
    tripCost = tripCost/2
    ageCost = "reduced fare"

print(f"Total Amount Due: ${tripCost:.2f} [{tripType} ({ageCost})]")


# Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")
str = input("Please enter a long string: ")
x = 0
while x < len(str):
    if str[x] == " ":
        print(f"str[{x}] = SPACE")
    else:
        print(f"str[{x}] = {str[x]}")
    x = x + 1
reverseStr = str[::-1].replace(' ', '')
print(f"Reverse no spaces: {reverseStr}")

# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")
print("Keep entering a positive integer\nTo quit, input a negative integer")
number = 0
largestEN = 0
while number >= 0:
    number = int(input("Enter a number: "))
    if number % 2 == 0 and number > largestEN:
        largestEN = number
print(f"Largest Even Number: {largestEN}")


# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")
size = 0
while size < 5 or size > 20:
    size = int(input("Enter size between 5 and 20: "))

for i in range(size):
    print("-"*i + "\\")
print("-"*size + "|")
for j in range(size-1, -1, -1):
    print("-" * j + "/")

input("Press enter to quit.")
