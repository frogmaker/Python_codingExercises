"""




"""

import methods




"""
suma = 0
licznik = 0
while True:
    a = int(input("podaj liczbe"))
    if a == 0: break
    suma = suma+a
    licznik = licznik+1
print(suma/licznik)


suma = 0
licznik = 0
while suma<=100:
    a = int(input("podaj liczbe"))
    if a == 0: break
    suma += a
    licznik += 1
else:
    print("uwaga suma>100")
print("...")

"""
print("hello world")


# r = 3.0
# p = 0.01
# for i in range
#
#
#
# rm =
#

case = input("case: ")

match case:
    case "1":
        print("case 1: ")
        print()

        g = (methods.fibo())
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))
        print(next(g))

        methods.findHowNumberCanBeDivided(int(input("n=")))

        methods.collatzProblem(int(input("n=")))

    case "2":
        print("case 2: ")
        print()

        r = 3.0
        p = 0.01
        for i in range(1, 101):
            q = p + r * p * (1 - p)
            print(q)
            p = q
        # end for

    case "3":
        print("case 3: ")
        print()
        kod = methods.gen()
        koniec = False
        tr =0
        print("wprowadź 4-cyfrowy kod (np '>>1234') ")
        while not koniec:

            proba = input(">>")
            p = methods.spr(kod, proba)
            print(10*" ",p)
            tr += 1
            koniec = (p==(4, 0))
        print("gratulacje, ", "wykonane proby: ", tr)

    case "4":
        print("case 4: ")
        print()

    case "5":
        print("case 5: ")
        print()