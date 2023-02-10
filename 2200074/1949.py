import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    visited[y][x] = True

    for _ in range(4):
        nx, ny = x + dx[_], y + dy[_]

        if 0 <= nx < N and 0 <= ny < N:
            if maxtrix[y][x] > maxtrix[ny][nx] and not visited[ny][nx]:
                dfs(nx, ny)
         
N, K = map(int, input().split())
maxtrix = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, maxtrix))

for y in range(N):
    for x in range(N):
        if maxtrix[y][x] == max_height:
            visited = [[False]*N for _ in range(N)]
            dfs(x, y)
