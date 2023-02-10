# Flatten
import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump):
        maxindx = boxes.index(max(boxes))
        minindx = boxes.index(min(boxes))
        boxes[maxindx] -= 1
        boxes[minindx] += 1
    print(f'#{t} {max(boxes) - min(boxes)}')