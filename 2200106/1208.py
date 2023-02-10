for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump+1):
        max_ = boxes.index(max(boxes))
        min_ = boxes.index(min(boxes))

        diff = boxes[max_] - boxes[min_]
        if diff <= 1:
            print(f'#{tc} {diff}')
            break
        else:
            boxes[max_] -= 1
            boxes[min_] += 1
    else:
        print(f'#{tc} {diff}')
