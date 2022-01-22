################
# Lab 4
# Author: Micheal Cini
# Email: cini15@my.yorku.ca
# Student ID: 218672964
# Section A
###############

# you'll need the random module
import random

### Write your functions below ###

def getCardValue():
    return random.randint(2, 14)

def getCardStr(cardValue):
    cardValue = str(cardValue).replace("2", "2")
    cardValue = str(cardValue).replace("3", "3")
    cardValue = str(cardValue).replace("4", "4")
    cardValue = str(cardValue).replace("5", "5")
    cardValue = str(cardValue).replace("6", "6")
    cardValue = str(cardValue).replace("7", "7")
    cardValue = str(cardValue).replace("8", "8")
    cardValue = str(cardValue).replace("9", "9")
    cardValue = str(cardValue).replace("10", "T")
    cardValue = str(cardValue).replace("11", "J")
    cardValue = str(cardValue).replace("12", "Q")
    cardValue = str(cardValue).replace("13", "K")
    cardValue = str(cardValue).replace("14", "A")
    return cardValue


def getHLGuess():
    hl = "null"
    while hl != "H" or hl != "L":
        hl = input("High or Low (H/L)?").upper()
        if hl == "H":
            return "HIGH"
        elif hl == "L":
            return "LOW"


def getBetAmount(maximum):
    betAmount = 0
    while betAmount > maximum or betAmount < 1:
        betAmount = int(input("Input bet amount: "))
    return betAmount

def playerGuessCorrect(card1, card2, betType):
    if betType == "HIGH":
        if card2 > card1:
            return True
        else:
            return False
    elif betType == "LOW":
        if card2 < card1:
            return True
        else:
            return False


### Write your main program below ####
msg = """--- Welcome to High-Low ---
Start with 100 points.  Each round a card will be drawn and shown.
Select whether you think the 2nd card will be Higher or Lower than the 1st card.
Then enter the amount you want to bet.
If you are right, you win the amount you bet, otherwise you lose. 
Try to make it to 500 points within 10 tries."""

print(msg)

round = 1
maximum = 100

while round <= 10:

    print(f"""
-------------------------------------
OVERALL POINTS: {maximum}      ROUND {round}/10""")
    card1 = getCardValue()
    card1Str = getCardStr(card1)
    print(f"First Card is a [{card1Str}]")
    betType = getHLGuess()
    betAmount = getBetAmount(maximum)
    card2 = getCardValue()
    card2Str = getCardStr(card2)
    print(f"Second Card is a [{card2Str}]")
    if playerGuessCorrect(card1, card2, betType):
        wl = "YOU WON"
        maximum = maximum + betAmount
    else:
        wl = "YOU LOST"
        maximum = maximum - betAmount
    print(f"Card1 [{card1Str}] Card2 [{card2Str}] - You bet '{betType}' for {betAmount} - {wl}")
    if maximum >= 500:
        print(f"""-----------------WIN------------------
YOU MADE IT TO *{maximum}* IN {round} ROUNDS!
--------------------------------------""")
        break
    elif maximum <= 0:
        print(f"""-----------------LOSE------------------
YOU HAVE *{maximum}* POINTS AFTER {round} ROUNDS!
---------------------------------------""")
        break
    elif round == 10:
        print(f"""-----------------LOSE------------------
ONLY *{maximum}* POINTS IN {round} ROUNDS!
---------------------------------------""")
        break
    round = round + 1



input("Press enter to exit. ")  # input statement to pause code when finished