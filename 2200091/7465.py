import sys
input = sys.stdin.readline

test = int(input())

for k in range(test):
    n, m = map(int, input().split())
    # n = 정점 / m = 간선

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    stack = []
    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            stack = [i]

            while stack:
                v = stack.pop()
                visited[v] = True

                for j in graph[v]:
                    if not visited[j]:
                        stack.append(j)

    print(f"#{k+1} {cnt}")
