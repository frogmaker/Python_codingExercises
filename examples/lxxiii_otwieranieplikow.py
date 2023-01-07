"""
PLIK - nazwana lokacja, która przechowuje na STAŁE dane na dysku.

RAM - pamięć podręczna komputera, gdzie przechowywane są dane TYMCZASOWO

Operacje na plikach
1) otwieranie
2) pisanie/czytanie
3) zamykanie

podstawowe sposoby otwierania plików
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeślli plik istniał to go usunie,
                        jeśli nie to stworzy
a - A ppend (dopisywanie)

rozszerzenie to tylko 'tekst' nadawany po to, aby inne programy
             rozpoznawały plik w odpowiedni dla tych programów sposób


"""

a = 5

file = open("test.txt", "w")#UCHWYT HANDLE
file.write("sample")
file.write("\n")
file.write("sample")
file.write("\n")
file.close()

# obsługa wyjątków_74
try:
    file = open("test.txt", "a")
    file.write("A")
    file.write("\n")
    print(0/0)
    file.write("SAMPLE")
    file.write("B")
finally:
    file.write("C")
    file.close()

