# ex1
# number = 1000
# while number >= 0:
#     print(number)
#     number -= 1

# ex2
# i = 0
# result = 0
# nNumber = int(input("give natural number: "))
# while i <= nNumber:
#     result += i
#     i += 1
# print("sum of ", nNumber, "first natural number equals: ", result)

# ex3
# wynik = 0
#
# """
# i = 0
# while i < 4:
#     x = int(input("Podaj liczbe: "))
#     wynik += x
#     i += 1
#
# print("Wynik dodawania liczb to:", wynik)
# """
#
# for i in range(1200):
#     if (i % 2 == 0 and i % 7 == 0 ):
#         print("Liczba", i, " jest parzysta i podzielna przez 7")
#
# print("Wynik dodawania liczb to:", wynik)
#


# ex5

i = 0

sum: int = 0

while i < 3:

    number = int(input("your number to sum: "))

    if number > 0 and number % 2 == 0:

        sum += number

        i += 1

    else:

        print("wrong input")

        continue

print("sum equals: ", sum)
