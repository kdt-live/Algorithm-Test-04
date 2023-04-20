for t in range(1, 11) :
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N) :
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1
        box[min_index] += 1

    print(f"#{t} {max(box) - min(box)}")