def podwoj(x):
    x = x * 2
    return x


print(podwoj(4))

test = lambda x: x * 2
print(test(4))

print((lambda x: x*2)(4))


myList = [11, 24, 35, 17, 20, 3, 2, 18]

myList_filtered = list(filter(lambda x: x % 2 != 0, myList))
print(myList_filtered)
myList_filtered2 = [i for i in myList if i % 2 != 0]
print(myList_filtered2)
