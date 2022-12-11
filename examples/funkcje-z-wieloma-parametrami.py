def pole_prostokata(a, b):
    print(a * b)

pole_prostokata(2, 5)

def innePoleProstokata(a, b):
    return a * b

print(10 * innePoleProstokata(2, 5))

def dzielenie(a, b):
    if b == 0:
        return
    return a / b

x = dzielenie(10, 0)
if (x):
    print("dzialanie wykonano poprawnie")
else:
    print("coś poszło nie tak")
