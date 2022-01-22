#########################
# Lab 5
# Author: Micheal Cini
# Email: cini15@my.yorku.ca
# Student ID: 218672964
# Section A
#########################

import random
import pyttsx3


def generateRandomList(listSize, maximumIntegerValue):
    x = []
    for i in range(listSize):
        x.append(random.randint(0, maximumIntegerValue))
    return x


def computeAverage(rndList):
    averageSum = 0
    for i in range(len(rndList)):
        averageSum += rndList[i]
    return averageSum / len(rndList)


def task1():
    listSize = int(input("Input list size: "))
    maximumIntegerValue = int(input("Input max int: "))
    rndList = generateRandomList(listSize, maximumIntegerValue)
    print(f"Generated list\n{rndList}")
    print(f"Average value = {computeAverage(rndList):.4f}")


def stringToCharLst(phoneNumber):
    x = []
    for i in range(len(phoneNumber)):
        x.append(phoneNumber[i])
    return x


def charsToWord(charLst):
    y = []
    x = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
         "9": "nine", "0": "zero", "-": "dash"}
    for i in range(len(charLst)):
        y.append(x[charLst[i]])
    return y


def sayWordList(wordLst):
    engine = pyttsx3.init()
    engine.say(wordLst)
    engine.runAndWait()


def task2():
    phoneNumber = input("Enter phone number as XXX-XXX-XXXX\nType Here: ")
    charLst = stringToCharLst(phoneNumber)
    print(charLst)

    wordLst = charsToWord(charLst)
    print(wordLst)

    separator = "->"
    print(separator.join(wordLst))

    answer = input("Say word list? (Y/N)").upper()
    if answer == "Y":
        sayWordList(wordLst)
    return


def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    task2()

    input("Press enter to exit.")


if __name__ == "__main__":
    main()
