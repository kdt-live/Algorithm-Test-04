def dfs(index):
    stack = [index]
    visited[index] = True

    while stack:
        cur = stack.pop()

        for adj in people[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    people = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    group = 0

    for _ in range(M):
        v1, v2 = map(int, input().split())

        people[v1].append(v2)
        people[v2].append(v1)
    
    for index in range(1, N+1):
        if not visited[index]:
            dfs(index)
            group += 1

    print(f'#{test_case} {group}')
