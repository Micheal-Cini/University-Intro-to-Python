####
# EECS1015 - Midterm
# Name: Micheal Cini
# Student ID: 218672964
# Email: cini15@my.yorku.ca
# Section A
##
import random


def task0():
    print("""EECS1015 - Midterm
Name: Micheal Cini
Student ID: 218672964
Email: cini15@my.yorku.ca
Section A""")


def task1():
    firstName = input("Your first name: ").strip().lower().title()
    lastName = input("Your last name: ").strip().upper()
    initialFunds = float(input("Initial funds to invest: $"))
    annualReturn = float(input("Annual return percentage: "))
    print(f"Yearly return for {firstName} {lastName}")
    print(f"Initial Deposit: ${initialFunds:.2f}")
    for i in range(1, 6):
        initialFunds = initialFunds + initialFunds * (annualReturn / 100)
        print(f"Year {i}: ${initialFunds:.2f}")


def task2():
    currentAmount = 0.00
    print("Soda Vending Machine")
    while round(currentAmount, 2) < 1.00:
        print(f"Current amount {currentAmount:.2f} out of $1.00")
        print("""Insert Coin
1. Toonie  ($2.00)
2. Loonie  ($1.00)
3. Quarter ($0.25)
4. Dime    ($0.10)
5. Nickle  ($0.05)""")
        selection = input("Selection [1-5]?")
        if selection == "1":
            currentAmount += 2.00
        elif selection == "2":
            currentAmount += 1.00
        elif selection == "3":
            currentAmount += 0.25
        elif selection == "4":
            currentAmount += 0.10
        elif selection == "5":
            currentAmount += 0.05
        else:
            print("Invalid selection!")
    print(f"Total amount provided: ${currentAmount:.2f}")
    print("Thank you for your purchase.")
    if round(currentAmount, 2) > 1.00:
        print(f"Please take your change ${currentAmount - 1:.2f}")


def task3():
    y = "Y"
    while y == "Y":
        snakeEyes = 0
        dieTotal = 0
        print("Dice Game\nRolling Die 10 Times")
        for i in range(1, 11):
            die = random.randint(1, 7)
            print(f"Roll {i}: [{die}]")
            dieTotal += die
            if die == 1:
                snakeEyes += 1
        if snakeEyes == 2:
            print("+10 Bonus for snake eyes [1][1]!")
            dieTotal += 10
        if dieTotal > 35:
            wL = "OVER 35 POINTS [YOU WIN!]"
        elif dieTotal:
            wL = "TOO FEW POINTS [YOU LOSE!]"
        print(f"Total {dieTotal} -- {wL}")
        y = input("Enter 'Y' to play again").upper()


def countCases(quoteString):
    upperCase = 0
    lowerCase = 0
    for i in range(len(quoteString)):
        if quoteString[i].isupper():
            upperCase += 1
        elif quoteString[i].islower():
            lowerCase += 1
    return upperCase, lowerCase


def flipCase(quoteString):
    caseFlip = ""
    for i in range(len(quoteString)):
        if quoteString[i].isupper():
            caseFlip += quoteString[i].lower()
        elif quoteString[i].islower():
            caseFlip += quoteString[i].upper()
        else:
            caseFlip += quoteString[i]

    return caseFlip


def cutQuotedText(quoteString):
    amount = quoteString.count("\"")
    if amount != 2:
        return "ERROR! No quoted text."
    else:
        firstQuote = quoteString.find("\"")
        secondQuote = quoteString.rfind("\"") + 1
        cutQuote = quoteString.replace(quoteString[firstQuote:secondQuote], "")
        return cutQuote


def task4():
    userStr = input("Enter a string with one word with \"quotes\": ")
    upperCase, lowerCase = countCases(userStr)
    caseFlip = flipCase(userStr)
    cutString = cutQuotedText(userStr)

    print(f"This string has {upperCase} uppercase characters.")
    print(f"This string has {lowerCase} lowercase characters.")
    print(f"Case flip: '{caseFlip}'")
    print(f"Quote removed: '{cutString}'")


# main function for EECS1015 midterm
def main():
    print("\n")
    task0()
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")


if __name__ == "__main__":
    main()
