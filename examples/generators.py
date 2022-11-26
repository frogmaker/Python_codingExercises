import sys

evenNumbers = [element
               for element in range(440)
               if (element % 2 == 0)
               ]

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )
print(evenNumbers)
print(evenNumbers[3])
print(evenNumbersGenerator)
print()
i = 0
for item in evenNumbersGenerator:

    if (i == 3):
        print(item)
    i += 1
print()
print(sys.getsizeof(evenNumbersGenerator))

print(sum(evenNumbersGenerator)) #suma liczb powoływanych przez generator

zadanie = (item ** 2
           for item in range(100)
           if item % 1 == 0)
print(sum(zadanie))