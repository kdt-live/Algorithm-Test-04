for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    for _ in range(dump):
        max_index = boxes.index(max(boxes))
        min_index = boxes.index(min(boxes))

        boxes[max_index] -= 1
        boxes[min_index] += 1

    result = max(boxes) - min(boxes)
    
    print(f'#{test_case} {result}')