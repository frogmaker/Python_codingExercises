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
#
# imiona = ["Arkadiusz", "Wioletta", "Karol", "Kuba", "Adrian", "Wojtek"]
# liczby = [3, 12, 24, 7, -8]
#
# print("Arkadiusz" in imiona) #True
#
# if ("Wojtek" in imiona):
#     print("Hi Wojtek")
#
# if (2 not in liczby):
#     print("there is not 2 in list")
# else:
#     print("list liczby contains number 2")
#
# print(3 * liczby)      # [3, 12, 24, 7, -8, 3, 12, 24, 7, -8, 3, 12, 24, 7, -8]
#
# print([4, 8, 16, 32] + liczby)
#
# print(liczby + [4, 8, 16, 32])
# print(liczby + ["one", "two", "ten"])
#
# matrix = ["jeden", "dwa", "trzy",
# "one", "two", "three",
# "ein", "zwei", "drei"
# ]
#
# print(matrix[8]) #drei


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

#
# lista1 = [54, 1, -2, 20, 1]
# lista2 = ["Arkadiusz", "Wioletta"]
#
# print(len(lista1))
# lista1.append(4)
# print(lista1)
# lista1.extend([-4, -66, -33, -1000])
# print(lista1)
#
# lista2.insert(1, "kuba")
# print(lista2)
#
# print(lista1.index(54)) #0
#
# lista1.reverse()
# print(lista1)
#
# lista1.sort(reverse=True)
# print(lista1)
#
# ileOne = lista1.count(1)
# print(ileOne)
#
# listtest = [0, 1, 2, [30, 31, 32]]
# print(listtest)
# print(listtest[3])
# print(listtest[3][1]) #działa!

# ex30_krotki

# krotka = (1, 42, 12, -4) # od listy różni się nawiasami: [] vs. () lub brak nawiasów; krotki nie da się zmienić
#
# print(krotka[1])
# krotka[1] = 0  # błąd TypeError: 'tuple' object does not support item assignment

# ex31_słownik
# dictionary - słownik KLUCZ - WARTOŚĆ
# pokoje = {49: 'Arkadiusz Włodarczyk', 69: 'Wioletta Włodarczyk'}
#
# a = {'imie': 'Arkadiusz', 'nazwisko': 'Włodarczyk'}
#
# print(pokoje[49])
# print(pokoje.get(49))
# pokoje[50] = 'Jan Kowalski'
# print(pokoje)
#
# pokoje.update({30: 1000000000})
# print(pokoje)
#
# del(pokoje[30])
# print(pokoje)
#
# autor = pokoje.pop(49)
# print(pokoje)
# print(autor)
#
# ostatni = pokoje.popitem()
# print(pokoje)
# print(ostatni)
#
# print(len(pokoje))

#32.sets/zbiory
#
# """
#      czy:   el. unikalne | kolejność | zmiana konkretnego el. | nowe elementy
# listy          NIE           TAK             TAK                   TAK
# krotki         NIE           TAK             NIE                   NIE
# słowniki       TAK           NIE             TAK                   TAK
# zbiory         TAK           NIE             NIE                   TAK
#
#         ZBIORY: BONUS w postaci | & - ^
# """
#
# A = {1, 4, 20, -4, 20}
# print(A) #posortowany i unikalny
#
#
# B = {1, 4, 30, 48}
#
# print(A.issubset(B))
#
# print(A & B)
# print(A | B)
# print("/////")
# print(A - B)
# print(B - A)
# print("/////")
# print(A ^ B) #wyklucza wspólne wartości (alternatywa wykluzająca)
#
# C = [1, 22, 22, 4, 0, -1]
# d = set(C)
# print(C)
# print(d)
# print(A & d)
#
# print(A)
# A.discard(4)
# print(A)

## 33# TYPY ZAGNIEŻDZONE

# imie = "Arkadiusz"
# wiek = 29
# plec = "mężczyzna"
#
# imie2 = "Wioletta"
# wiek2 = 23
# plec2 = "kobieta"
#
#
# osoba1 = ('Arkadiusz', 29, 'mężczyzna')
# osoba2 = ('Wioletta', 23, 'kobieta')
# osoba3 = ('Kuba', 33, 'mężczyzna')
#
# listaGosci = {
#                 ('Arkadiusz', 28, 'mężczyzna'),
#                 ('Wioletta', 22, 'kobieta'),
#                 ('Kuba', 32, 'mężczyzna')
#              }
# listaGosci2 = {
#                 ('Arkadiusz', 28, 'mężczyzna'),
#                 ('W', 22, 'kobieta'),
#                 ('K', 32, 'mężczyzna')
#              }
#
# listaGosci3 = listaGosci & listaGosci2
#
# print(listaGosci3)
#
# for name, age, sex in listaGosci:
#     print(name)
#     print(age)
#     print(sex)
#     print()

## 35. słownik w liście, słownik w słowniku

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
        "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
        "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
        "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
        "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
        "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}
         }

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
        ]



oceny = {
        "Arkadiusz": (2,1,2,3,2,3),
        "Wiola": (4,2,1,3,4)
    }



"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]
for name, age, sex in ppllist2:
    print(name)

"""

ratings1 = {
    "Arkadiusz": (2, 1, 2, 3, 2, 3),
    "Agness": (4, 2, 1, 3, 4)
}
ratings2 = [
    {'name': "Arkadiusz", 'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
    {'name': "Agness", 'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
]

ratings3 = {
    "Arkadiusz": {'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
    "Agness:": {'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
}

print()

print(people["IcFDG2bO9AYDF651DoyH"])

print()
for key in ratings1:
    print(key, "oceny", ratings1[key])

print()
for dictionary in people2:
    for key in dictionary:
        print(key, ":", dictionary[key])
print("end")

print(people.items())

print()

for id, dictionary in people.items():
    print(dictionary)

print()
# #dwa przykłady na to samo: .items działa tylko na słownikach
for id, dictionary in people.items():
    print("id: ", id)
    for key in dictionary:
        print(key, ":", dictionary[key])

print()
for key in people:
    print("ID:", key)
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])

