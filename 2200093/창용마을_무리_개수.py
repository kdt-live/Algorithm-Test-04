# dfs

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    def dfs(x, count):
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                count = dfs(i, count+1)
        return count

    visited = [False for _ in range(N+1)]

