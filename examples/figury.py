import math


def pole_kwadratu(a):
    return a * a


def pole_prostokata(a, b):
    return a * b


def pole_kola(r):
    return math.pi * r ** 2


def pole_trojkata(a, h):
    return 0.5 * a * h


def pole_trapezu(a, b, h):
    return (a + b) / 2 * h


option = 0







while option == 0:

    print("Pole jakiej figury chciałbyś obliczyć:")
    print("1. kwadrat")
    print("2. prostokąt")
    print("3. koło")
    print("4. trójkąt")
    print("5. trapez")
    print("6. Zakończ")
    option: int = int(input("Wprowadź numer opcji:"))


    if option == 1:
        a: int = int(input("Podaj bok a:"))
        print("Pole zadanego kwadratu:", pole_kwadratu(a))
        print()
        s = input("Czy chcesz obliczyć coś jeszcze? T/n: ")
        if s == 'n':
            break
        else:
            option = 0
    elif option == 2:
        a = int(input("Podaj bok a:"))
        b = int(input("Podaj bok b:"))
        print("Pole zadanego prostokąta:", pole_prostokata(a, b))
        print()
        s = input("Czy chcesz obliczyć coś jeszcze? T/n: ")
        if s == 'n':
            break
        else:
            option = 0
    elif option == 3:
        r = int(input("Podaj promień r:"))
        print("Pole zadanego koła:", pole_kola(r))
        print()
        s = input("Czy chcesz obliczyć coś jeszcze? T/n: ")
        if s == 'n':
            break
        else:
            option = 0
    elif option == 4:
        a = int(input("Podaj bok a:"))
        h = int(input("Podaj hysokość h:"))
        print("Pole zadanego trójkąta:", pole_kwadratu(a))
        print()
        s = input("Czy chcesz obliczyć coś jeszcze? T/n: ")
        if s == 'n':
            break
        else:
            option = 0
    elif option == 5:
        a = int(input("Podaj długość podstawy a:"))
        b = int(input("Podaj długość podstawy b:"))
        h = int(input("Podaj hysokość h:"))
        print("Pole zadanego trójkąta:", pole_trapezu(a, b, h))
        print()
        s = input("Czy chcesz obliczyć coś jeszcze? T/n: ")
        if s == 'n':
            break
        else:
            option = 0
    elif option == 6:
        break
    else:
        print("Padł wybór spoza zakresu")
        end = input("zakończyć?: T/n")
        if end == 'n':
            option = 0
        else:
            break
