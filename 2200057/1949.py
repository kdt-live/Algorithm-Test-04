T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for t in range(1, T+1):
    N, K = map(int, input().split())
    ground = []
    max_h = 0
    max_route = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        li = list(map(int, input().split()))
        max_h = max(max(li), max_h)
        ground.append(li)    

    def dfs(x, y, construct):
        global max_route, visited
        max_route = max(max_route, visited[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if ground[x][y] > ground[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    dfs(nx, ny, construct)
                    visited[nx][ny] = 0
                elif ground[x][y] > ground[nx][ny] - K and not construct:
                    temp = ground[nx][ny]
                    ground[nx][ny] = ground[x][y] - 1
                    construct = True
                    visited[nx][ny] = visited[x][y] + 1
                    dfs(nx, ny, construct)
                    ground[nx][ny] = temp
                    construct = False
                    visited[nx][ny] = 0         

    for i in range(N):
        for j in range(N):
            if ground[i][j] == max_h:
                visited[i][j] = 1
                dfs(i, j, construct= False)
                visited[i][j] = 0
    print(f'#{t} {max_route}')