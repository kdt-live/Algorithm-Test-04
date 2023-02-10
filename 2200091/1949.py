# 어디가 문제일까..........................

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def dfs(x, y, distance, is_construct):
    global cnt

    if cnt < distance:
        cnt = distance

    visited[x][y] = True

    # 동서남북 확인
    for dx, dy in delta:
        nx = x + dx
        ny = y + dy

        # 범위를 벗어나거나 방문한 길이면 무시
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
            continue

        # 다음 길이 현재 길보다 낮으면 방문처리하고 그 자리에서 dfs
        if graph[nx][ny] < graph[x][y]:
            visited[nx][ny] = True
            dfs(nx, ny, distance+1, is_construct)

        # 다음 길이 현재 길보다 높거나 같고, 공사가 가능한 상태면 공사 진행
        elif graph[nx][ny] >= graph[x][y] and not is_construct:
            # 최대 K만큼 깎을 수 있으니 1부터 K까지 반복
            for k in range(1, K+1):
                # 공사 상태를 바꾸고 k만큼 깎으면서 현재 길과 높이 비교
                is_construct = True
                graph[nx][ny] -= k

                # 깎은 길이 현재 길보다 낮으면 방문처리하고 dfs 
                if graph[nx][ny] < graph[x][y]:
                    visited[nx][ny] = True
                    dfs(nx, ny, distance+1, is_construct)

                # 다른 높이로도 깎아봐야하므로 공사 안 한 것처럼 돌려놓기
                is_construct = False
                graph[nx][ny] += k


test = int(input())

for t in range(test):
    N, K = map(int, input().split())
    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    graph = [[] for _ in range(N)]

    for i in range(N):
        graph[i] = list(map(int, input().split()))

    max_ = max(map(max, graph))
    cnt = 0

    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_:
                visited = [[False] * N for _ in range(N)] 
                dfs(i, j, 1, False)

    print(f"#{t+1} {cnt}")