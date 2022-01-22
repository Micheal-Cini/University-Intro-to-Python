# Lab 8
# Author: Micheal Cini
# Email: cini15@my.yorku.ca
# Student ID: 218672964 <- please do not add spaces
# Section A
import random
import time


class SnailClass:
    sequence = ["__~@", "_~_@", "~__@"]

    def __init__(self, name):
        self.name = name
        assert len(self.name) <= 2, "Snail's initials must be 2 characters."
        self.speed = random.randint(1, 10) / 10
        self.frame = 0
        self.pos = 0.0

    def move(self):
        self.pos = self.pos + self.speed

        self.frame = (self.frame + 1) % 3

    def getIntPos(self):
        return int(self.pos)

    def getName(self):
        return self.name

    def getStr(self):
        return " " * self.getIntPos() + SnailClass.sequence[self.frame] + " " * (40 - self.getIntPos()) + self.getName()


def getSnailList():
    x = []
    N = int(input("How many snails are racing? "))
    for i in range(1, N + 1):
        snailInitials = input(f"Snail {i} two initials: ")
        x.append(SnailClass(snailInitials.upper()))
    return x


def runRace(initials):
    input("Press enter to start race.")
    time_step = 1

    while True:

        for j in initials:
            if j.getIntPos() > 39:
                print(f"Snail {j.getName()} WON!")
                return
        currentTime = (40 * "-") + f"Time {str(time_step)}"
        print(currentTime)
        for i in initials:
            print(i.getStr())
            i.move()

        time.sleep(0.2)
        time_step += 1


def main():
    play = True
    while play:
        print("Snail Race . . . .")
        initials = getSnailList()
        runRace(initials)
        again = input("Play again (Y)?")
        if again.upper() != "Y":
            play = False


if __name__ == "__main__":
    main()
