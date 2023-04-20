T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    visited = [False] * (N+1)

    for m in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    result = []
    cnt = 0

    for n in range(1, N+1):
        if n not in result:
            result.append(n)
            stack = [n]
            visited[n] = True
        
            while stack:
                cur = stack.pop()

                for adj in graph[cur]:
                    if not visited[adj]:
                        visited[adj] = True
                        stack.append(adj)
                        result.append(adj)

            cnt += 1

    print(f'#{t+1} {cnt}')