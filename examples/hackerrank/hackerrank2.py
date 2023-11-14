# #if __name__ == '__main__':
# N = int(input())
# fun = []
# list = []
# for i in range(N):
#     fun.append(input())
#     #print(fun)
#     if fun[i][0] == 'i':
#         pos = int(fun[i].split(' ')[1])
#         # print('pos= ', pos)
#         num = int(fun[i].split(' ')[2])
#         # print('num= ', num)
#         # print('list=', list)
#         list.insert(pos, num)
#         # print('list=', list)
#     elif fun[i][0] == 'r' and fun[i][2] == 'm':
#         rem = int(fun[i].split(' ')[1])
#         list.remove(rem)
#     elif fun[i][0] == 'a':
#         app = int(fun[i].split(' ')[1])
#         list.append(app)
#     elif fun[i][0] == 's':
#         list.sort()
#     elif fun[i] == 'pop':
#         list.pop()
#     elif fun[i][0] == 'r' and fun[i][2] == 'v':
#         list.reverse()
#     else:
#         print(list)
#

###########################################

# n = int(input())
# integer_list = map(int, input().split())
# print(integer_list)
# t = tuple(integer_list)
# print(t)
# print(hash(t))

###################

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr.sort(), float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)