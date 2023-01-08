"""
ĆWICZENIE:

Wczytaj imiona i nazwiska z pliku o nazwie:
imionanazwiska.txt

1) rozdziel je tak, by powstała lista krotek, gdzie wewnętrzne krotki to
pary imiona/nazwiska
2) zapisz imiona do pliku imiona.txt
3) zapisz nazwiska do pliu nazwiska.txt

Zastanów się jak rozwiązać problem,
gdy nie ma podanego nazwiska w pliku imionanazwiska.txt, gdy będziesz
zapsywał nazwiska do pliku nazwiska.txt


[
 ("Jakis", "Ziom")
]

"""

listOfTuples = []

with open("imionanazwiska.txt", "r") as file:
    lines = file.read().splitlines()
    for person in lines:
        listOfTuples.append(tuple(person.split(" ")))

with open("imiona", "w") as imionaFile:
    for person in listOfTuples:
        imionaFile.write(person[0] + "\n")

with open("nazwiska", "w") as nazwiskaFile:
    for person in listOfTuples:
        try:
            nazwiskaFile.write(person[1] + "\n")
        except IndexError:
            nazwiskaFile.write("\n")

        # if len(person) > 1:
        #     nazwiskaFile.write(person[1] + "\n")
        # else:
        #     nazwiskaFile.write("\n")


