from collections import deque
for j in range(10):
    num = int(input())
    l = list(map(int,input().split()))
    for i in range(num):
        l = list(l)
        l = deque(sorted(l))
        l.appendleft(l.popleft()+1)
        l.append(l.pop()-1)
    print(f'#{j+1} {max(l)-min(l)}')