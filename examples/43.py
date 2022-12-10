

numbersDivBySevenAndFive = [
    i
    for i in range(100, 171)
    if i % 7 == 0 and i % 5 != 0

]

num = {
    numbersDivBySevenAndFive.index(i) + 1: i
    for i in numbersDivBySevenAndFive
}

print(numbersDivBySevenAndFive)
print(num)
