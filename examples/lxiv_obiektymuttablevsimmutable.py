"""
    obiekt to zmienna, która ma więcej możliwości,
    można wywołać na nim "funkcje"
    może mieć więcej niż 1 wartość
    
    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmmienne
    mutable - zmienny

    = ZMIANA miejsca wskazywania na nowy adres, na inny obiekt
"""

a = 4
print(a.bit_length())

listSample = [1, 4, 512, 24]
print(id(listSample))
listSample2 = listSample
print(id(listSample))
listSample2.append(5)
print(id(listSample))
print(listSample)
print(id(listSample2))

print()
print("a: ", id(a))
b = a
print("a: ", id(a))
print("b: ", id(b))
b = 7
print("a: ", id(a))
print("b: ", id(b))

print()
k = 5
h = 5
print("k: ", id(k))
print("h: ", id(h))
print()

c = 5
print("c: ", id(c))


def add(c, amount = 1):
    print("c: ", id(c))
    c = c + amount
    print("c: ", id(c))


add(c)
print("c: ", id(c))
print()

def append_element_to_list(listka, element):
    print("listka: ", id(listka))
    listka.append(999)
    print("listka: ", id(listka))
    x = [2, 4, 20]
    listka = x
    print("listka: ", id(listka))


print(listSample)
print("listSample: ", id(listSample))
append_element_to_list(listSample, 5)
print("listSample: ", id(listSample))
print(listSample)
print(listSample2)


