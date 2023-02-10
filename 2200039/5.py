# 이것도 시간 내에 다 못 풀었네요ㅠㅠ 원래는 dfs 안 쓰고 탐색으로 풀고있었는데
# 그러다가 자꾸 답이 꼬여서 전부 지우고 dfs로 도전해보고 있었어요,,,😭
# ㅠㅠ 그런데 결국에는 그것도 좀 어려워서 끝까지 해결을 못했습니다... 속상해요ㅠㅠ

def dfs(x,y):
    global highest, visited
    dX = [-1,1,0,0]; dY = [0,0,-1,1]; X_position = 0; Y_position = 0
    for i in range(4):
        X_position = x + dX[i]
        Y_position = y + dY[i]
        if not (0 <= X_position < N and 0 <= Y_position < N) or visited[X_position][Y_position]: continue
        else:

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for i in range(N)]
    highest = 0
    for i in range(N):
        for j in range(N):
            if highest < matrix[i][j]: highest = matrix[i][j]
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == highest:
                visited[i][j] = 1
                dfs(i,j)