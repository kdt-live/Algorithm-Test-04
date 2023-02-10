# Flatten

for i in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()           # 높이를 정렬한다.

    for j in range(dump):
        boxes[-1] -= 1     # 가장 높은 곳에서 1을 뺀다.
        boxes[0] += 1      # 가장 낮은 곳에 1을 더한다.
        boxes.sort()       # 다시 정렬한다.
    
    print(f'#{i + 1} {boxes[-1] - boxes[0]}')