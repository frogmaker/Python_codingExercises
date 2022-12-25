import copy
""" copy - płytka
    deepcopy - głębokiego
"""

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    #toBeDestroyedList.clear()
    toBeDestroyedList[0] = 99
    print(toBeDestroyedList)
   

myList = [1, 4, 2, 1, 52, 3]  # lista zawiera wratości immutable - wystarczy płytka kopia

print("przed_evil: ", id(myList), " ", myList)
evil_function(myList.copy())
evil_function(list(myList))
evil_function(myList[:])   # kopia - wartości nie zmienione
print("po evil: ", myList)
evil_function(myList)   # wartości zmienione
print("bez kopii: ", myList)

print()


def evil_function2(toBeDestroyedList):
    print(id(toBeDestroyedList))
    #toBeDestroyedList.clear()
    toBeDestroyedList[0][0] = 99
    print(toBeDestroyedList)


myList2 = [[1, 4], [2, 1], [52, 3]]

print("przed_evil: ", id(myList2), " ", myList2)

# evil_function2(myList2.copy())   # kopia, ale płytka - !!!wartości zmienione

evil_function2(copy.deepcopy(myList2)) # kopia głęboka - dane bezpieczne

print("po evil: ", myList2)
evil_function2(myList2)   # wartości zmienione
print("bez kopii: ", myList2)



a = 4
b = 4 # INT immutable
