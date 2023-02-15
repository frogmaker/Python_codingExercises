# arr = [1,2,3,4,6,6,6,6,6,5]
#
# Arr = sorted(arr)
#
# print(Arr)
#
# pop = Arr.
# print(pop)
# print(Arr)
#
# while pop == Arr[len(Arr)-1]:
#     Arr.pop()
#     print(Arr)
# print("Arr=", Arr)
# snd = Arr.pop()
#
# print(snd)

sortedScores = [1,1,2,2,3]
min = sortedScores[0]
for i in range(1, len(sortedScores)):
    if min != sortedScores[i]:
        snd = sortedScores[i]
        break

print(snd)

aaa = 10.00000
print('%.2f'%aaa)

################
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avelist = student_marks[query_name]
    ave = (avelist[0] + avelist[1] + avelist[2]) / 3

    print('%.2f' % ave)

    #################
    if __name__ == '__main__':
        records = []
        names = []
        for _ in range(int(input())):
            name = input()
            score = float(input())

            records.append([name, score])
        # print(records)
        scores = []
        for i in range(0, len(records)):
            scores.append(records[i][1])
        sortedScores = sorted(scores)
        min = sortedScores[0]
        for i in range(1, len(sortedScores)):
            if min != sortedScores[i]:
                snd = sortedScores[i]
                break
        snds = []
        for i in range(0, len(records)):
            if snd == records[i][1]:
                snds.append(records[i][0])
        sortedSnds = sorted(snds)
        for i in range(0, len(sortedSnds)):
            print(sortedSnds[i])

