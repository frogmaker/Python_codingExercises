def add():
    c = 4
    print(c)


c = 1
add()
print(c)

print()
def add2(c, amount = 1):
    c = c + amount
    print(c)


add2(c)
print(c)


print()
def change_global_c():
    global c
    c = c + 4
    print(c)


change_global_c()
print(c)

