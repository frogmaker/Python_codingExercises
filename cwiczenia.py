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
#
# i = 0
#
# sum: int = 0
#
# while i < 3:
#
#     number = int(input("your number to sum: "))
#
#     if number > 0 and number % 2 == 0:
#
#         sum += number
#
#         i += 1
#
#     else:
#
#         print("wrong input")
#
#         continue
#
# print("sum equals: ", sum)
#

# ex_listyin

# in
# not in
# Operacje na listach

imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian", "Wojtek"]
liczby = [3, 12, 24, 7, -8]

print("Arkadiusz" in imiona) #True

if ("Wojtek" in imiona):
    print("Hi Wojtek")

if (2 not in liczby):
    print("there is not 2 in list")
else:
    print("list liczby contains number 2")

print(3 * liczby)      # [3, 12, 24, 7, -8, 3, 12, 24, 7, -8, 3, 12, 24, 7, -8]

print([4, 8, 16, 32] + liczby)

print(liczby + [4, 8, 16, 32])
print(liczby + ["one", "two", "ten"])

matrix = ["jeden", "dwa", "trzy",
"one", "two", "three",
"ein", "zwei", "drei"
]

print(matrix[8]) #drei


#len() - długość - length
#.append - dodać
#.extend - rozszerzyć
#.insert(index, co) - wstawić
#.index - indeks danego el.
#sort(reverse=False) - sortuj rosnąco
#max()
#min()
#.count - ile razy coś wystąpi
#.pop - usuń ostatni el.
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyść liste
#.reverse - zamień kolejność


lista1 = [54, 1, -2, 20, 1]
lista2 = ["Arkadiusz", "Wioletta"]

print(len(lista1))
lista1.append(4)
print(lista1)
lista1.extend([-4, -66, -33, -1000])
print(lista1)

lista2.insert(1, "kuba")
print(lista2)

print(lista1.index(54)) #0

lista1.reverse()
print(lista1)

lista1.sort(reverse=True)
print(lista1)

ileOne = lista1.count(1)
print(ileOne)

listtest = [0, 1, 2, [30, 31, 32]]
print(listtest)
print(listtest[3])
print(listtest[3][1]) #działa!

