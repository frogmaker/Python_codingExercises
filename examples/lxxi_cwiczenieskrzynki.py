"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""


import random
from enum import Enum


def find_aproximate_value(value, percentRange):
    return random.randint((value*(percentRange/100)), (value*(1+(percentRange/100))))

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())


Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomarańczowy',
                           'Purple': 'fiolet',
                           'Gold': 'złoty'
                          }
               )

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())
print(chestColourList)
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                       chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                       for reward in range(len(chestColourList))
                   }

gameLength = 1
goldAcquired = 0

print("Welcome in my game called KOMNATA")
print("""You have only 5 steps to make,
see yourself how much gold you gonna acquire till the end!""")

while gameLength > 0:
    gamerAnswer = "yes" # \input("Do you want to move forward?")
    if (gamerAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList,eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(chestColourList, chestColourProbability)[0]
            print(random.choices(chestColourList, chestColourProbability))
            print(random.choices(chestColourList, chestColourProbability)[0])

            print("drawnColour: ", drawnColour)
            print("The chest color is", drawnColour.value)
            gamerReward = find_aproximate_value(rewardsForChests[drawnColour], 50)
            goldAcquired = goldAcquired + gamerReward
        elif(drawnEvent == Event.Empty):
            print("You've drawn nothing, you are so unlucky!")
            
    else:
        print("You can go just straight man, nothing else, this game is dumb")
        continue
    
    gameLength = gameLength - 1

print("Congratulation, you have acquired: ", goldAcquired)

print(10*"*", type(gameLength), "gameLength", gameLength)

print("""

""")
