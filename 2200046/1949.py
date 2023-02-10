# 등산로 조성

import sys
sys.stdin = open('sample_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cut, route_length):
    # 최대값 갱신
    global longest
    if longest < route_length:
        longest = route_length
    
    # 인접 위치 확인
    for m in range(4):
        del_x = x + dx[m]
        del_y = y + dy[m]

        # 인접 좌표가 범위 안에 들고, 방문하지 않은 곳일 때
        if (0 <= del_x < n) and (0 <= del_y < n) and not visited[del_x][del_y]:
            # 인접 위치의 높이가 현 위치보다 낮을 때
            if mount[del_x][del_y] < mount[x][y]:
                visited[del_x][del_y] = True
                dfs(del_x, del_y, cut, route_length + 1)
                visited[del_x][del_y] = False
            
            # 인접 위치의 높이가 현 위치의 높이 이상이고 공사를 하지 않은 상태일 때
            elif not cut and (mount[del_x][del_y] >= mount[x][y]):
                # 1에서 k까지의 높이를 깎는 경우
                for o in range(1, k + 1):
                    mount[del_x][del_y] -= o
                    cut = True
                    
                    # 깎은 높이가 현 위치의 높이보다 낮을 때
                    if mount[del_x][del_y] < mount[x][y]:
                        visited[del_x][del_y] = True
                        dfs(del_x, del_y, cut, route_length + 1)
                        visited[del_x][del_y] = False
                
                    # 공사 전으로 복구
                    mount[del_x][del_y] += o
                    cut = False

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    mount = [[0 for j in range(n)] for l in range(n)]
    coord = list()
    highest = 0
    longest = 0

    # 지도를 완성하고 가장 높은 곳의 높이와 좌표를 저장한다.
    for j in range(n):
        mount[j] = list(map(int, input().split()))

        for l in range(n):
            if highest < mount[j][l]:
                highest = mount[j][l]
                coord = [[j, l]]
            elif highest == mount[j][l]:
                coord.append([j, l])
    
    # 가장 높은 곳부터 탐색을 시작한다.
    for point in coord:
        visited = [[False for j in range(n)] for l in range(n)]
        visited[point[0]][point[1]] = True
        dfs(point[0], point[1], False, 1)
    
    print(f'#{i + 1} {longest}')