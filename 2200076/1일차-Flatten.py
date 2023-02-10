import sys
sys.stdin = open('input.txt', 'r')
import heapq

for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    heapq.heapify(boxes)

    for _ in range(dump):
        heapq.heappush(boxes, heapq.heappop(boxes)+1)
        x = max(boxes)
        for i in reversed(range(100)):
            if boxes[i] == x:
                boxes[i] -= 1
                break

        if x - boxes[0] <= 1:
            break
    
    print(f'#{t} {max(boxes)-boxes[0]}')