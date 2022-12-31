"""
shuffle - randomizes entire list

"""

import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList) #działa na oryginale

print(cardList)
print(random.sample(cardList, 5))

kartyA = []
kartyB = []
def rozdaj_dwa_sety(ile_kart_rozdac):
    for i in range(ile_kart_rozdac):
        karta = cardList.pop()
        kartyA.append(karta)
        karta = cardList.pop()
        kartyB.append(karta)

rozdaj_dwa_sety(5)

print(cardList)
print(kartyA)
print(kartyB)




