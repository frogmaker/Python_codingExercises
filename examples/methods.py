"""


"""
import math
import random

def fibo():
#”Funkcja generująca kolejne wyrazy ciągu Fibonacciego”
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b
# end def


def findHowNumberCanBeDivided(n):
    #0 n = int(input("n="))
    b = 2
    #1 while n>1:
    while b <= math.sqrt(n):
        if n % b == 0:
            print(b)
            n = n//b
        else:
            b = b+1
    """
        # end if
    # end while
    """
    if n > 1:
        print(n)
    print("koniec")


def collatzProblem(n):
    while n!=1:
        if n%2==0:
            n=n//2
            print(n)
        else:
            n = 3*n+1
            print(n)
    print("koniec")


def nwd(a, b):


    assert a > 0 and b > 0, "a,b musza byc wieksze od zera"

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a

    return a


def gen():
    '''generuje 4 znakowy napis złożony z cyfr 1-6'''
    res = ""
    for i in range(4):
        res = res + str(random.randint(1,6))
    return res


def spr(kod, proba):
    "zwraca liczbę cyfr na poprawnych miejscach oraz na nie swoich miejscach w postaci krotki (1c,1b)"
    k = list(kod)
    p = list(proba)
    lc = 0
    for i in range(4):
        if p[i] == k[i]:
            lc = lc + 1
            p[i] = -1
            k[i] = -2
    lb = 0
    for i in range(4):
        for j in range(4):
            if p[i] == k[j]:
                lb = lb + 1
                p[i] = -1
                k[j] = -2
    return (lc, lb)


