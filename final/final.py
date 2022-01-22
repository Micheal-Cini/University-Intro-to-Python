###########################################
# EECS1015 - Final exam (final.py)
# Name: Micheal Cini
# Student ID: 218672964
# Email: cini15@my.yorku.ca
# Section A
###########################################

# import the approriate items from utilities.py and other modules may you require
import random
from utilities import studentsInfo as stuInfo, SeaLife, students as stu
import time


def task0():
    print("Final Exam - EECS1015\n"
          "Name: Micheal Cini\n"
          "Student ID: 218672964\n"
          "Email: cini15@my.yorku.ca\n"
          "Section A")


def task1():
    print("Rock, Paper, Scissors!")
    playGame = True
    while playGame:
        print("Make your selection. . .")
        valid = False
        while not valid:
            userSelection = int(input("(1) rock, (2) paper, (3) scissors? "))
            if userSelection == 1:
                userSelectionx = "rock"
                valid = True
            elif userSelection == 2:
                userSelectionx = "paper"
                valid = True
            elif userSelection == 3:
                userSelectionx = "scissors"
                valid = True
            else:
                print("Invalid selection. Try again.")
        HAL = random.randrange(1, 4)
        if HAL == 1:
            HALx = "rock"
        elif HAL == 2:
            HALx = "paper"
        elif HAL == 3:
            HALx = "scissors"
        print(f"You: {userSelectionx}")
        print(f"HAL: {HALx}")
        printOutcome(userSelection, HAL)
        x = input("Play again (Y/N)? ")
        if not x.lower() == "y":
            playGame = False


def printOutcome(userSelection, computerSelection):
    if (userSelection == 1 and computerSelection == 3) or \
            (userSelection == 2 and computerSelection == 1) or \
            (userSelection == 3 and computerSelection == 2):

        print("You win!")
    elif (userSelection == 1 and computerSelection == 2) or \
            (userSelection == 2 and computerSelection == 3) or \
            (userSelection == 3 and computerSelection == 1):
        print("You lose!")
    elif (userSelection == 1 and computerSelection == 1) or \
            (userSelection == 2 and computerSelection == 2) or \
            (userSelection == 3 and computerSelection == 3):
        print("A tie!")


def task2():
    inputString = input("Input two or more chars separated by spaces: ")
    alist = list(inputString.split(" "))
    print(f"Initial list\n{alist}")
    strAlist = ""
    for i in alist:
        strAlist = strAlist + i
    print(f"String version: '{strAlist}'")
    print("Modified list")
    swapAdjacentElements(alist)
    print(alist)
    strModifiedAlist = ""
    for i in alist:
        strModifiedAlist = strModifiedAlist + i
    print(f"String version: '{strModifiedAlist}'")


def swapAdjacentElements(alist):
    assert len(alist) >= 2, "Must enter two or more characters!"
    if len(alist) % 2 == 0:
        for i in range(0, len(alist), 2):
            alist[i], alist[i + 1] = alist[i + 1], alist[i]
    else:
        for i in range(0, len(alist) - 1, 2):
            alist[i], alist[i + 1] = alist[i + 1], alist[i]


def task3():
    studentsAndInfo = {}
    for i in range(len(stu)):
        if contains(stuInfo["Year 1"], i):
            year = "Year 1"
        elif contains(stuInfo["Year 2"], i):
            year = "Year 2"
        elif contains(stuInfo["Year 3"], i):
            year = "Year 3"
        else:
            year = "Year 4"

        if contains(stuInfo["CS"], i):
            program = "CS"
        elif contains(stuInfo["DM"], i):
            program = "DM"
        elif contains(stuInfo["BZ"], i):
            program = "BZ"
        else:
            program = "SE"

        if contains(stuInfo["On Campus"], i):
            housing = "On Campus"
        else:
            housing = "Off Campus"

        studentsAndInfo[stu[i]] = f"{stu[i]:>10s} ({year}) Program: {program} Housing: {housing}"

    for i in sorted(studentsAndInfo):
        print(studentsAndInfo[i])


def contains(alist, i):
    for value in alist:
        if value == i:
            return True
    return False


def task4():
    input("\nPress enter to start aquarium.")
    time_step = 1

    sLife = []

    for i in range(5):
        direction = random.randint(0, 1)
        position = random.randint(1, 38)
        x = SeaLife(direction, position)
        sLife.append(x)

    for i in range(50):
        print((40 * "-") + f"Time: {str(time_step)}")
        for j in sLife:
            print(j.getStr())
            j.move()
        time.sleep(0.3)
        time_step += 1



def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()
