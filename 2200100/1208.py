import sys
input = sys.stdin.readline

for t in range(10):
    dump = int(input())
    box = list(map(int,input().split()))
    a = 0
    for _ in range(dump):
        if min(box) != max(box):
            b = box.index(max(box))
            c = box.index(min(box))
            box[b] -= 1
            box[c] += 1
        elif max(box) - 1 == min(box):
            a = 1
        elif max(box) == min(box) :
            a = 0
    a = max(box) - min(box)
    print(f'#{t+1} {a}')