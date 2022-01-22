#########################
# EECS1015 - York University
# Lab #7 - Starting Code
# Author: Micheal Cini
# Email: cini15@my.yorku.ca
# Student ID: 218672964
# Section A
#  Writing test cases
#  Make sure you install PyTest (see lecture notes)
#  NOTE - You can only run this in PyCharm for a project that has installed PyTest
#  You cannot double click on this file.  That is fine, we can test it once you submit it.
#########################

import pytest
from typing import List


# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:  # given
    myList.sort()


def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()


def getMinMax(myList: List[int], minormax: str) -> int:  # given -- but requires additional assert
    assert myList != [], "List must not be empty"
    assert minormax.upper() == "MAX" or minormax.upper() == "MIN", "2nd argument must be 'Min' or 'Max' "
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result


# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1():
    a = [15, 3]
    initializeMinMaxList(a)
    min1 = getMinMax(a, "MIN")
    assert min1 == 3, "Min should be 3"
    max1 = getMinMax(a, "MAX")
    assert max1 == 15, "Max should be 15"


def test_getMinMaxCase2():
    a = [15]
    initializeMinMaxList(a)
    min1 = getMinMax(a, "MIN")
    assert min1 == 15, "Min should be 15"
    insertItem(a, 15)
    max1 = getMinMax(a, "MAX")
    assert max1 == 15, "Max should be 15"


def test_getMinMacCase3():
    a = []
    initializeMinMaxList(a)
    insertItem(a, 3)
    insertItem(a, 15)
    min1 = getMinMax(a, "MIN")
    assert min1 == 3, "Min should be 3"
    max1 = getMinMax(a, "MAX")
    assert max1 == 15, "Max should be 15"


def test_getMinMaxRequestError():
    a = [3, 10, 15]
    initializeMinMaxList(a)
    with pytest.raises(AssertionError) as e:
        getMinMax(a, "MID")
    assert e.typename == "AssertionError", "Should raise AssertionError!"


def test_getMinMaxEmptyError():
    a = []
    initializeMinMaxList(a)
    with pytest.raises(AssertionError) as e:
        getMinMax(a, "MAX")
    assert e.typename == "AssertionError", "Should raise AssertionError!"
