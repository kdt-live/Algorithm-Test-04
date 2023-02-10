import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

test = 10
for i in range(10):
    n = int(input())
    box = list(map(int, input().split()))

    for _ in range(n):
        box = sorted(box)
        min_ = box[0]
        max_ = box[len(box)-1]

        if max_ - min_ < 2:
            print(f"#{i+1} {max_ - min_}")
            break
        else:
            box[len(box)-1] -= 1
            box[0] += 1
    else:
        box = sorted(box)
        print(f"#{i+1} {box[len(box)-1] - box[0]}")