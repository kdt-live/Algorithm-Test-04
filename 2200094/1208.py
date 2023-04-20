


T = 10

for t in range(1, T + 1):



    M = int(input())

    array = list(map(int, input().split()))
    for j in range(M):
        max_ = max(array)
        min_ = min(array)
        mini = array.index(min_)
        maxi = array.index(max_)
        array[mini] += 1
        array[maxi] -= 1

    result = max(array) - min(array)
    print("#", t, " ", result, sep='')