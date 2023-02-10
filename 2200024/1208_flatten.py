from collections import deque
for t in range(1, 11) :
    n = int(input())
    li = list(map(int, input().split()))
    li = sorted(li)
    dq = deque(li)

    for _ in range(n) :
        dq = sorted(dq)
        dq = deque(dq)

        a = dq.popleft()+1
        b = dq.pop()-1
        
        dq.append(a)
        dq.append(b)

    print (f'#{t} {max(dq) - min(dq)}')    