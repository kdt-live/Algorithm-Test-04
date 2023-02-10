# 3499 퍼펙트 셔플

import sys
sys.stdin = open('input_3499.txt', 'r')

from collections import deque
T = int(input())
for t in range(T):
    n = int(input())
    q = list(input().split())
    result = []
    q1 = deque(q[:(n+1)//2])
    q2 = deque(q[(n+1)//2:])
    while q1:
        result.append(q1.popleft())
        if q2:
            result.append(q2.popleft())
    print(f'#{t+1}', *result)

'''
T = int(input())
for t in range(T):
    n = int(input())
    q = list(input().split())
    result = []
    for i in range(n//2):
        result.append(q[i])
        result.append(q[n//2+i])
    if n & 1:
        result.append(q[n//2])
    print(f'#{t+1}', *result)
'''