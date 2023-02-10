# 테스트 케이스 51개중 8개 정답

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt):
    global res
    if res < cnt:
        res = cnt
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] == False:
            if lst[nx][ny] < lst[x][y]:                
                dfs(nx, ny, cnt+1)
            elif lst[nx][ny] - K < lst[x][y]:
                dfs(nx, ny, cnt+1)
                
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = [[int(x) for x in input().split()] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    mxm = 0
    res = 0
    
    # 최댓값 찾기
    for i in range(N):
        for j in range(N):
            if mxm < lst[i][j]:
                mxm = lst[i][j]
    
    # 최댓값 좌표 저장
    mxm_list = []
    for i in range(N):
        for j in range(N):
            if mxm == lst[i][j]:
                mxm_list.append((i, j))
    
    for i in range(len(mxm_list)):
        dfs(mxm_list[i][0], mxm_list[i][1], 1)
        
    print(f'#{test_case} {res}')