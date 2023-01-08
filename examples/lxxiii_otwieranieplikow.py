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
    #print(0/0)
    file.write("\nSAMPLE ")
    file.write("B ")
finally:
    file.write("C ")
    file.write("\n")
    file.close()

# wczytanie pliku który zawsze zostanie zamknięty, nawet po błędzie
with open("test.txt", "a") as file2:
    file2.write("test ")
    #print(0/0)

with open("oceany.txt", "r") as file3:
    linia1 = file3.readline()
    linia2 = file3.readline()

print(linia1)
print(linia2)

with open("oceany.txt", "r") as file3:
    linia3 = file3.readline()

print(linia3) #ponowne otwarcie i czytanie od pierwszej linii

with open("oceany.txt", "r") as file3:
    ocenany = file3.readlines()

print(ocenany)

print(file3.encoding)  #niezgodność kodowania, wymagana zmiana

with open("oceany.txt", "r", encoding="UTF-8") as file3:
    ocenany = file3.readlines()

print(ocenany)
print(file3.encoding)

with open("oceany.txt", "r", encoding="UTF-8") as file3:
    oceany = file3.read()
    print(file3)
    print(oceany)
    print()
    oceany2 = file3.read().splitlines() #poza ramką odczytu, nie ma już co czytać dalej. rozwiązanie poniżej w sekcji LXXVII
    print(oceany2)

with open("oceany.txt", "r", encoding="UTF-8") as file3:
    oceany3 = file3.read().splitlines()
    print("oceany3: ", oceany3)

print(oceany3[0], oceany3[3])
print()
print(oceany3[0][11])
listaPierwszegoWierszaLiterowa = list(oceany3[0])
print(listaPierwszegoWierszaLiterowa)
listaPierwszegoWireszaWyrazowa = oceany3[0].split(" ")
print(listaPierwszegoWireszaWyrazowa[1])

with open("oceany.txt", "r", encoding="UTF-8") as file4:
    for line in file4:
        print(line)

# LXXVII _ zmiana wskaźnika

with open("oceany.txt", "r", encoding="UTF-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(10)
    print(file.readline())
    print(file.tell())

# LXXIX - tryby mnogie

"""
Mnogie tryby otwierania plików pozwalają na wykonanie dwóch czynności jednocześnie. 


Typy mnogie: 

r + (do czytania i pisania) pozwala na wykonanie file.read oraz file.write odrazu na tym pliku, sprawdza czy dany plik istnieje i nie usuwa go.
 
       with open("oceany.txt", "r+", encoding="UTF-8") as file:
            


w+ (do pisania i czytania) różni się od r+ tym, że usunie zawartość istniejącego pliku lub stworzy go, gdy ten nie istnieje

              with open("oceany.txt", "w+", encoding="UTF-8") as file:
             file.readline()

a+ (“wieczny tryb” dopisywanie i czytanie) wskaźnik dopisywania jest zawsze na samym końcu, jeśli plik nie istniał stworzy go 

       with open("oceany.txt", "a+", encoding="UTF-8") as file:
            file.write("Ocean Arka")


           Jeżeli chcemy w tym trybie czytać - musimy przejść do początku (0) 
              
            file.seek(0)
            print(file.readline())
            print(file.tell())


            file.write("Ocean Arkadiusza Wielkiego")

"""