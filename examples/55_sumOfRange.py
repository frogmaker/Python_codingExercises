
import time

rangeToSum: int = 5  # int(input("Podaj liczbę będącą końcem zakresu: "))

print('sposób 1')
def sum1(a):
    sum: int = 0
    # list = []
    for number in range(a + 1):
        sum += number
        # list.append(number)
    return sum

print("suma liczb z podanego zakresu to: ", sum1(rangeToSum))

# sposób 2
print('sposób 2')


def sum2(a):
    return sum([number for number in range( a +1)])

print(sum2(rangeToSum))
#

print(sum([number2 for number2 in range(rangeToSum +1)]))
print([number for number in range(rangeToSum +1)])
# sposób 3
print('sposób 3')

def sum3(a):
    return (((a) ) *( a +1) ) /2

print(int(sum3(rangeToSum)))

# sposób 4
print('sposób 4')


def sum4(a):
    return sum({number for number in range( a +1)})

print(sum4(rangeToSum))
print({number for number in range(rangeToSum +1)})

# sposób 5
print('sposób 5')


def sum5(a):
    return sum((number for number in range(a + 1)))

print(sum5(rangeToSum))
print((number for number in range(rangeToSum + 1)))

print()
print("ocena czasu działania kodu: ")

def finish_timer(start):
    end = time.perf_counter()
    return end - start


start = time.perf_counter()
print(sum1(234567))
print(finish_timer(start))

start = time.perf_counter()
print(sum2(234567))
print(finish_timer(start))

start = time.perf_counter()
print(sum3(234567))
print(finish_timer(start))

start = time.perf_counter()
print(sum4(234567))
print(finish_timer(start))

start = time.perf_counter()
print(sum5(234567))
print(finish_timer(start))


# funkcja jako zmienna _57
def function(func):
    func()


def show_message():
    print("jakaś wiadomość")


function(show_message)


def function2(func, arg):
    func(arg)


def show_message2(message):
    print(message)


function2(show_message2, "inna wiadomość")

#58_domyślne wartośc argumentu::np:: arg = 1


def function_performance(func, how_many_times=1, **arg):
    sumOfTime: int = 0
    print(arg)
    print(arg.get("element"))
    print(arg.get("a"))
    for i in range(how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sumOfTime += (end - start)
    return sumOfTime


print("a ", function_performance(sum1, how_many_times=25, a=500000))
print("b ", function_performance(sum2, 1, a=500000))
print("c ", function_performance(sum3, 1, a=500000))
print("d ", function_performance(sum4, 1, a=500000))
print("e ", function_performance(sum5, 1, a=500000))


#LX_ćwiczenie is_element_in?

# def function_with_two_arg_performance(func, arg2, arg = 30, how_many_times = 1):
#     sumOfTime: int = 0
#     for i in range(how_many_times):
#         start = time.perf_counter()
#         func(arg, arg2)
#         end = time.perf_counter()
#         sumOfTime += (end - start)
#     return sumOfTime
# ###################### rozwiązaniem jest argument wielowartościowy:: *arg

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]
# print(setContainer)
# print(listContainer)


def is_element_in(element, container):
    for i in container:
        if element == i:
            return True
    return False


print(is_element_in(30, setContainer))
print(is_element_in(30, listContainer))

print(is_element_in(3000, setContainer))
print(is_element_in(3000, listContainer))

# print("setContainer: ", function_with_two_arg_performance(is_element_in, setContainer, 3000, 5))
# print("listContainer: ", function_with_two_arg_performance(is_element_in, listContainer, 3000, 5))
print("setContainer: ", function_performance(is_element_in, how_many_times=500000, element=500, container=setContainer))
print("listContainer: ", function_performance(is_element_in, how_many_times=500000, element=500, container=listContainer))

