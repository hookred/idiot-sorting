#!/usr/bin/env python3

import random

unsortedList = [10, 5, 3, 8, 12, 11, 4, 21, 3, 7]

def maxWithIndex(checkList):
    currentIndex = 0
    result = ((0, checkList[0]))

    while (currentIndex < len(checkList)):
        if (checkList[currentIndex] > result[1]):
            result = ((currentIndex, checkList[currentIndex]))

        currentIndex += 1

    return result

def sortList(unsortedList):
    tempList = unsortedList.copy()
    currentIndex = 0

    sortedList = []

    while (currentIndex < len(unsortedList)):
        print(currentIndex, len(unsortedList))
        (maxIndex, maxValue) = maxWithIndex(tempList)
        tempList.pop(maxIndex)
        sortedList.append(maxValue)

        currentIndex += 1

    return sortedList[::-1]

def shuffleList(currentList):
    newList = currentList.copy()
    listSize = len(currentList)
    resultList = []

    while (listSize > 0):
        elementIndex = random.randint(0, listSize - 1)
        resultList.append(newList.pop(elementIndex))
        listSize -= 1

    return resultList

def checkIfListSorted(currentList):
    currentIndex = 1
    listSize = len(currentList)

    while (currentIndex < listSize):
        if (currentList[currentIndex] < currentList[currentIndex - 1]):
            return False

        currentIndex += 1

    return True

def idiotSortList(currentList):
    sortedList = shuffleList(currentList)
    count = 0

    while (not checkIfListSorted(sortedList)):
        sortedList = shuffleList(sortedList.copy())
        count += 1

    return (sortedList, count)


(sortedList, count) = idiotSortList(unsortedList)

print("Unsorted list : ", unsortedList)
print("Sorted list : ", sortedList)
print("Loop : ", count)
