


for tc in range(10):
    N = int(input())
    box = sorted(list(map(int, input().split())))
    while N > 0:
        box[-1] -= 1
        box[0] += 1
        box.sort()
        if box[-1]-box[0] <= 1:
            break
        N -= 1
    print("#{} {}".format(tc+1, box[-1]-box[0]))