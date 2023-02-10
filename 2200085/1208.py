for t in range (10):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range (dump):
        max_box = max(box)
        max_idx = box.index(max_box)
        min_box = min(box)
        min_idx = box.index(min_box)

        box[min_idx] += 1
        box[max_idx] -= 1

    print(f'#{t+1} {max(box) - min(box)}')