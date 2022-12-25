

def count(*arg):
    # print(arg)
    # print(arg[0])
    # print(len(arg))
    sum_of_arg = 0
    for i in arg:
        sum_of_arg += i
    return sum_of_arg


print(count(2, 4, 1, 2, 4, 5, 10))


def count_in_one_line(*arg):
    return sum([i for i in arg])


print(count_in_one_line(2, 4, 1, 2, 4, 5, 10))

print(sum([2, 4, 1, 2, 4, 5, 10]))
