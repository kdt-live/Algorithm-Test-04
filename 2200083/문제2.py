# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

    for adj in graph[cur]:
      if not visited[adj]:
        visited[adj] = True
        stack.append(adj)

dfs(1)
print(sum(visited)-1)