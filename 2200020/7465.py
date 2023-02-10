from collections import deque

def bfs(start):
    queue = deque([start])
    visited = [0] * (n+1)
    visited[start] = 1
    while queue:
        cur = queue.popleft()
        for adj in graph[cur]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = 1
    return visited

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    answer = []
    for x in range(1, n+1):
        if bfs(x) not in answer:
            answer.append(bfs(x))
    print(f'#{test_case} {len(answer)}')