dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cut, cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if visited[nx][ny] == 1:
                continue
            if matrix[x][y] > matrix[nx][ny]:  #다음 길로 갈 수 있다면
                visited[nx][ny] = 1  #이동
                dfs(nx, ny, cut, cnt+1)
                visited[nx][ny] = 0  #복귀
            else:
                if cut and matrix[x][y] > matrix[nx][ny] - k:  #아직 공사를 하지 않았고 공사를 했을 때 이동이 가능하다면
                    pre = matrix[nx][ny]
                    matrix[nx][ny] = matrix[x][y] - 1  #다음 길은 최소한으로 깎기
                    visited[nx][ny] = 1
                    dfs(nx, ny, 0, cnt+1)
                    visited[nx][ny] = 0
                    matrix[nx][ny] = pre  #공사한 상태 원상복구

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]  #방문처리용
    distance_map = [[0]*n for _ in range(n)]  #거리계산용
    #print(visited)
    max_ = max(map(max, matrix))  #가장 높은 봉우리

    res = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == max_:
                cut = 1  #공사 기회
                visited = [[0]*n for _ in range(n)]  #방문처리용
                visited[i][j] = 1
                dfs(i, j, cut, 1)

    print(f'#{tc} {res}')