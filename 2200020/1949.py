dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(x, y, dig):
    global maximum
    maximum = max(maximum, visited[x][y])
    for d in range(4):
        if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n and visited[x + dx[d]][y + dy[d]] == 0:
            nx = x + dx[d]
            ny = y + dy[d]
            if graph[x][y] > graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, dig)
                visited[nx][ny] = 0
            elif dig and graph[nx][ny] - k < graph[x][y]:
                temp = graph[nx][ny]
                graph[nx][ny] = graph[x][y] - 1
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny, dig-1)
                visited[nx][ny] = 0
                graph[nx][ny] = temp

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = []
    top, maximum = 0, 0
    for i in range(n):
        graph.append(list(map(int, input().split())))
        if max(graph[i]) > top:
            top = max(graph[i])
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] == top:
                visited[x][y] = 1
                dfs(x, y, 1)
                visited[x][y] = 0
    print(f'#{test_case} {maximum}')