# 퍼펙트 셔플 

from collections import deque

T = int(input())

for t in range(T):
    ans = []

    N = int(input()) # 카드 개수
    cards = list(input().split()) # 카드 이름

    if N % 2 == 0: # 카드의 개수가 짝수일 때 
        queue1 = deque(cards[:N//2])
        queue2 = deque(cards[N//2:])

    else: # 카드의 개수가 홀수일 때
         queue1 = deque(cards[:(N//2)+1])
         queue2 = deque(cards[(N//2)+1:])
         queue2.append(" ")

    while len(queue1) != 0:
        ans.append(queue1.popleft())
        ans.append(queue2.popleft())

    print(f'#{t+1}', end=" ")
    if N % 2 != 0:
        print(*ans[:-1])
    else:
        print(*ans)






