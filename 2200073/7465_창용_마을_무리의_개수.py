# 7465 창용 마을 무리의 개수

import sys
sys.stdin = open('input_7465.txt', 'r')

def dfs(x):
    stack = [x]
    visited[x] = True
    while stack:
        now = stack.pop()
        for j in graph[now]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'#{t+1} {cnt}')