import sys
sys.stdin = open("flattern.txt", "r")


T = 10
for i in range(1, T + 1):
    dump = int(input())
    box_list = list(map(int,input().split()))
    for j in range(dump):
        maxhigh = max(box_list)
        minhigh = min(box_list)
        maxindex = box_list.index(maxhigh)
        minindex = box_list.index(minhigh)
        box_list[maxindex] -= 1
        box_list[minindex] += 1
    print(f'#{i} {max(box_list) - min(box_list)}')

