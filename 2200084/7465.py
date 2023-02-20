import sys
sys.stdin = open('input.txt', 'r')
def dfs(start, stack):
    cur = stack.pop()
    visited[cur] = start
    for i in graph[cur]:
        if visited[i] == False:
            stack.append(i)
            dfs(start, stack)
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    cnt = 0
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    start = 1             
    stack = [start]         
    visited[start] = True
    for j in range(1, N+1):
        if visited[j] == False:
            dfs(j, [j])
            cnt += 1  
    print(f'#{t} {cnt}')