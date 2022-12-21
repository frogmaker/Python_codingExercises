
listOfNumbers = [1, 2, 4, -10, 0, -100, 5, 19, 1, 1, 9]

def sumOfListAllNum(list):
    total = 0
    for number in list:
        total += number
    return total


print(sumOfListAllNum(listOfNumbers))


def sumOfListOnlyPositive(list):
    total = 0
    for number in list:
        if number > 0:
            total += number
    return total


print(sumOfListOnlyPositive(listOfNumbers))


def sumOfListOnlyPositive2(list):
    return sum([number for number in list if number > 0])


print(sumOfListOnlyPositive2(listOfNumbers))
