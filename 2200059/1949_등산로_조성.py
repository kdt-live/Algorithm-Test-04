# 미완성
# import sys
# sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T + 1):
    print('#', t)
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    # 최대 높이 구하기
    highest = 0
    highest_location = []
    for x in range(N):
        for y in range(N):
            if mountain[x][y] > highest:
                highest = mountain[x][y]
    # print(highest)
    # 최대 높이 좌표 구하기
    highest_location = []
    for x in range(N):
        for y in range(N):
            if mountain[x][y] == highest:
                highest_location.append((x, y))
    # print(highest_location)

    # 최장 경로 탐색
    # 경로 탐색하기 + 최장 경로

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    visited = []
    a, b = 2, 3
    stack.append((a, b))
    # max_stack = 0
    visited.append((a, b))
    while stack:
        # if max_stack < len(stack)+1:
        #     max_stack = len(stack)+1
        a, b = stack.pop()
        print(a, b)
        # 상하좌우 확인
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                if mountain[a][b] > mountain[nx][ny]:
                    a, b = nx, ny
                    stack.append((a, b))
                    print(a, b)
            else:
                print('stop')
                # visited.append((a, b))

    # print(max_stack)
