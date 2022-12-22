

import time

rangeToSum: int = 5 #int(input("Podaj liczbę będącą końcem zakresu: "))

print('sposób 1')
def sum1(a):
    sum: int = 0

    for number in range(a + 1):
        sum += number

    return sum

print("suma liczb z podanego zakresu to: ", sum1(rangeToSum))

#sposób 2
print('sposób 2')


def sum2(a):
    return sum([number for number in range(a+1)])

print(sum2(rangeToSum))
#

print(sum([number2 for number2 in range(rangeToSum+1)]))
print([number for number in range(rangeToSum+1)])
#sposób 3
print('sposób 3')

def sum3(a):
    return (((a))*(a+1))/2

print(int(sum3(rangeToSum)))

#sposób 4
print('sposób 4')


def sum4(a):
    return sum({number for number in range(a+1)})

print(sum4(rangeToSum))
print({number for number in range(rangeToSum+1)})


#sposób 5
print('sposób 5')


def sum5(a):
    return sum((number for number in range(a+1)))

print(sum5(rangeToSum))
print((number for number in range(rangeToSum+1)))

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