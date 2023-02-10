t = int(input())

def dfs(start):
    visited[start] = 1
    #is_dfs = 0
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    #         is_dfs = 1
    # if is_dfs:
    #     return 1
    # else:
    #     return 0

for tc in range(1, t+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        # if dfs(i):
        #     cnt +=1
        # 둘 이상만 무리로 따지는 게 아니고 한 명만 있어도 하나의 무리였다,,,,
        if visited[i] == 0:
            dfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')