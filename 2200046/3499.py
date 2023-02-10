# 퍼펙트 셔플

from collections import deque
from math import ceil

t = int(input())

for i in range(t):
    n = int(input())
    card_original = input().split()
    result = list()

    # 카드를 두 묶음으로 나눈다.
    front = deque(card_original[:ceil(n / 2)])
    back = deque(card_original[ceil(n / 2):])

    # 인덱스가 짝수일 때에는 front에서,
    # 홀수일 때에는 back에서
    # 카드를 한 장씩 result에 append한다.
    for j in range(n):
        if not j % 2:
            result.append(front.popleft())
        else:
            result.append(back.popleft())
    
    print(f'#{i + 1}', end = ' ')
    print(*result)