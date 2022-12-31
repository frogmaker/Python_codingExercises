"""
Napisz funkcję, która zasymuluje jak działa lotto,
tzn. wybiersz 6 UNIKALNYCH liczb z 49

sample - próbka/przykład

"""



import random
# lotto_numbers = [num for num in range(1, 50)]
#
# print(lotto_numbers)

def choose_random_numbers(amount, total_amount):
    lotto = []
    i = 0
    while i < amount:

        if i == 0:
            luck = random.choice([num for num in range(1, total_amount + 1)])
            # print("i: ", i, ", luck: ", luck)
            lotto.append(luck)
        else:
            luck = random.choice([num for num in range(1, total_amount + 1)])
            # print("i: ", i, ", luck: ", luck)
            lotto.append(luck)
            # print(lotto)
            for ii in range(i):
                if lotto[ii] == luck:
                    # print("przed pop: ", lotto)
                    lotto.pop()
                    # print("po pop: ", lotto)
                    i -= 1
        i += 1

    lotto.sort()
    print("Lotto results: ", lotto)


choose_random_numbers(6, 49)


print()
print()
print("sposób nr 2")
print()
def choose_random_numbers2(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))

choose_random_numbers2(6, 49)





