# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

var1, var2, var3 = "arek", 3, '3'



print(var3)
print(int(var3)+var2)    #rzutowanie na intiger
print(var3+str(var2))    #rzutowanie na stringa
print(var1[0])
var4 = var1[3]+var1[2]+var1[1]+var1[1]+var1[0]
print(var4)

name: str = "jurek"
age: int = 35

print_hi(name)
print("your age is ", age)


test1 = bool (age != 35)
print (str(test1)[0])
print (int(test1))

"""
instrukcje warunkowe
"""
a,b= 10,5
if (10>5):
    print("warunek spełniony") #wcięcia to 4 spacje!
elif(10<5):
    print("Tab to nie zawsze 4 spacje!")
else:
    print("coś innego")

"""
INSTRUKCJA WARUNKOWA

JESLI (PRAWDA)
 TO...
JESLI CO INNEGO (PRAWDA)
 TO...
A CALKOWICIE W INNYM WYPADKU
 TO...

 elif od ang else if

"""
wybor = input("* - mnożenie, / - dzielić, + - dodawać, - - odejmować: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if (wybor == '*'):
    print(a * b)
elif (wybor == '/'):
    if (b == 0):
        print("Cholero nie dziel przez zero")
    else:
        print(a / b)
elif (wybor == '+'):
    print(a + b)
elif (wybor == '-'):
    print(a - b)
else:
    print("nie wybrałeś dobrego wyboru")

import math

wybor = int(input("Wpisz cyfre "))
print(wybor)
print(abs(wybor))


"""
operatory logiczne
"""

wartosc = int(input("Sprawdzę, czy liczba jest z zakresu od 1 do 10: "))


# if (wartosc > 1 and wartosc < 10):
#     print("wartosc jest od 1 do 10")


a = 1
b = 2
if (not(a == 5 or b == 3)):
    print("tak")


'''
OPERATORY LOGICZNE

and - 'i'

True True - True
True False - False
False True - False
False False - False

KONIUNKCJA jest prawdzia, wtedy i tylko wtedy, gdy OBA wyrażenia w tym samym MOMENCIE są prawdziwe

or - 'lub'

True True - True
True False - True
False True - True
False False - False

Alternatywa jest fałszywa, wtedy i tylko wtedy, gdy OBA wyrazenia są w tym samym momencie fałszywe!

not - NIE

'''

#PĘTLA

#suma = 0
#x = int(input("Podaj kolejna liczbe:")


liczba = 0

while liczba <= 150:
    print(liczba)
    liczba += 1


