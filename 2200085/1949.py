dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs (r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])

    for d in range (4):
        nr = r + dr[d]
        nc = c + dc[d]

        if not (0<=nr<n and 0<=nc<n) or visited[nr][nc]:
            continue

        if arr[r][c] > arr[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        
        elif chance and arr[nr][nc] - k < arr[r][c]:
            tmp = arr[nr][nc]
            arr[nr][nc] = arr[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance - 1)
            visited[nr][nc] = 0
            arr[nr][nc] = tmp

for t in range (int(input())):
    n, k = map(int, input().split())
    arr = []
    top = 0

    for i in range (n):
        arr.append(list(map(int, input().split())))

        for j in range (n):
            if arr[i][j] > top:
                top = arr[i][j]
    
    MAX = 0
    visited = [[0] * n for _ in range (n)]

    for i in range (n):
        for j in range (n):
            if arr[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print(f'#{t+1} {MAX}')