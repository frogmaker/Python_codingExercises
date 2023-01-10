
import random
from enum import Enum

# Colours = Enum('Colours', {'Green': 'zielony',
#                            'Orange': 'pomarańczowy',
#                             }
#                )
Colours = Enum('Colours', 'Green Orange'
               )
print("List: ", list(Colours))
print(dir(Colours))
print(dir(Colours)[0])
print()
chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                             }

print(chestColoursDictionary)
chestColourList = tuple(chestColoursDictionary.keys())
print(chestColourList)
chestColourProbability = tuple(chestColoursDictionary.values())
print(chestColourProbability)


drawnColour = random.choices(chestColourList, chestColourProbability)
print("drawnColour: ", drawnColour[0])
print("drawnColour: ", drawnColour)
print("The chest color is", drawnColour[0].name)
