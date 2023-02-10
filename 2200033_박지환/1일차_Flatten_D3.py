from collections import deque

for number in range(1, 11):    
    dump = int(input())
    box = list(map(int, input().split()))
    box = deque(sorted(box))
    cnt = 0

    for i in range(dump):
        box.appendleft(box.popleft() + 1)
        box.append(box.pop() - 1)
        box = deque(sorted(box))
    
    print(f'#{number} {max(box) - min(box)}')
            