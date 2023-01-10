"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""

definicje = {}

while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")

    wybor = input("Co chcesz zrobić? ")

    if (wybor == "1"):
        klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie")
    elif (wybor == "2"):
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif (wybor == "3"):
        klucz = input("Jaką definicję chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunięto definicję o nazwie:", klucz)
        else:
            print("Nie znaleziono definicji o nazwie", klucz)
    elif (wybor == "4"):
        print("No to pa!")
        break
    else:
        print("Podałeś coś z poza zakresu")
