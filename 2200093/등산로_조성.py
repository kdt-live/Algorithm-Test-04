# dfs

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = []
    top = 0
    for i in range(N):
        A.append(list(map(int, input().split())))

        for j in range(N):
            if A[i][j] > top:
                A[i][j] = top
    
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1
                
                ...?