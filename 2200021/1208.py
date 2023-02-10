# 1208 [S/W 문제해결 기본] 1일차 - Flatten

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

# heap 풀이
import heapq as hq

for t in range(1,11):
    n = int(input())
    min_h = list(map(int,input().split()))
    max_h = []
    for i in range(100):
        hq.heappush(max_h,(-min_h[i],min_h[i]))
    hq.heapify(min_h)
    for i in range(n):
        hq.heappush(min_h,hq.heappop(min_h)+1)
        a, b = hq.heappop(max_h)
        hq.heappush(max_h,(a+1,b-1))
    print(f'#{t} {max_h[0][1]-min_h[0]}')

# list 풀이

for t in range(1,11):
    n = int(input())
    g = sorted(list(map(int,input().split())))
    while n > 0:
        g[0] += 1
        g[-1] -= 1
        g.sort()
        n -= 1
    print(f'#{t} {g[-1] - g[0]}')