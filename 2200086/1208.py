# 1일차 - Flatten

for t in range(1, 11):
    cnt = int(input())
    box = sorted(map(int, input().split()))

    while cnt > 0:
        a = box.pop() -1
        b = box.pop(0) + 1

        box.append(a)
        box.append(b)
        box.sort()
        cnt -= 1

        if (max(box) - min(box)) == 0:
            break
        if (max(box) - min(box)) == 1:
            break

    print(f'#{t} {max(box) - min(box)}')