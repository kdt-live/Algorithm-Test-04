# 1949 등산로 조성

# 여러 방법으로 풀어봤는데 계속 틀렸다
# 어떤 케이스는 맞고 어떤 케이스는 틀리고..
# 51개 케이스 중 41개 정답..
######## 푸는중 ###########

import sys
sys.stdin = open('input_1949.txt', 'r')

def dfs(x,y):
    global ans
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        ans = max(ans, visited[x][y])
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx, ny))
        visited[x][y] = 0

T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(T):
    ans = 0
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for a in range(1, k+1):
        for i in range(n):
            for j in range(n):
                graph[i][j] -= a
                max_ = max(map(max,graph))
                for x in range(n):
                    for y in range(n):
                        if graph[x][y] == max_:
                            visited = [[0] * n for _ in range(n)]
                            dfs(x, y)
                graph[i][j] += a

    print(f'#{t+1} {ans}')

# def dfs(x,y):
#     stack = [(x, y)]
#     visited[x][y] = 1
#     while stack:
#         x, y = stack.pop()
#         for idx in range(4):
#             nx = x + dx[idx]
#             ny = y + dy[idx]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
#                     stack.append((nx, ny))
#                     visited[nx][ny] = visited[x][y] + 1
""" 
def dfs(x,y):
    global ans
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        ans = max(ans, visited[x][y])
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx, ny))
        visited[x][y] = 0


T = int(input())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(T):
    # result = []
    ans = 0
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    for a in range(1, k+1):
        for i in range(n):
            for j in range(n):
                graph[i][j] -= a
                max_ = max(map(max,graph))
                for x in range(n):
                    for y in range(n):
                        if graph[x][y] == max_:
                            visited = [[0] * n for _ in range(n)]
                            dfs(x, y)
                            # result.append(max(map(max,visited)))
                # print(*graph, sep='\n')
                # print()
                graph[i][j] += a
    # print(result)
    print(f'#{t+1} {ans}') """


'''
from collections import deque

# def dfs(x,y):
#     q = deque([(x, y)])
#     visited[x][y] = 1
#     while q:
#         x, y = q.popleft()
#         for idx in range(4):
#             nx = x + dx[idx]
#             ny = y + dy[idx]
#             if 0 <= nx < 5 and 0 <= ny < 5:
#                 if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
#                     q.append((nx, ny))
#                     visited[nx][ny] = max(visited[nx][ny], visited[x][y] + 1)

# def dfs(x,y):
#     global ans
#     ans = max(visited[x][y], ans)
#     for idx in range(4):
#         nx = x + dx[idx]
#         ny = y + dy[idx]
#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if not visited[nx][ny]:
#                 if graph[nx][ny] < graph[x][y]:
#                     visited[nx][ny] = visited[x][y] + 1
#                     dfs(nx, ny)
#                     visited[x][y] = 0

def dfs(x,y):
    global ans
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        ans = max(ans, visited[x][y])
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
                    visited[nx][ny] = visited[x][y] + 1
                    stack.append((nx, ny))
        visited[x][y] = 0


graph = [
    [9, 3, 2, 3, 2],
    [6, 3, 1, 7, 5],
    [3, 4, 8, 8, 9],
    [2, 3, 7, 7, 7],
    [7, 6, 5, 5, 8]
]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
ans = 0
for x in range(5):
    for y in range(5):
        if graph[x][y] == 9:
            visited = [[0]*5 for _ in range(5)]
            # visited[x][y] = 1
            dfs(x, y)
            # visited[x][y] = 0
            print(*visited, sep='\n')
            print()
print(ans)
'''