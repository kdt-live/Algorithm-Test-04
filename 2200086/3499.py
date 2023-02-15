# 퍼펙트 셔플

from collections import deque

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    card = input().split()
    result = []

    if N % 2 == 0:   #짝수
        half = int(N/2)
        front = deque(card[:half])
        back = deque(card[half:])
        while front:
            a = front.popleft()
            result.append(a)
            b = back.popleft()
            result.append(b)


    else:    #홀수
        half  = int(N/2) +1
        front = deque(card[:half])
        back = deque(card[half:])
        while back:
            a = front.popleft()
            result.append(a)
            b = back.popleft()
            result.append(b)
        a = front.popleft()
        result.append(a)

    print(f'#{t}', *result)