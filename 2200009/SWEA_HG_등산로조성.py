import copy

i_t = int(input())
dx = (1, -1 , 0, 0)
dy = (0, 0, -1, 1)
# 그래프, 시작점, depth 적힌 방문지점, 깊이
def pathfinder(graph, start, visit, depth):
    x = start[0]
    y = start[1]
    visit[y][x] = depth
    for i_10 in range(4):
        if (0 <= y+dy[i_10] <= i_n - 1) * (0 <= x+dx[i_10] <= i_n - 1):
            if ((graph[y][x] > graph[y + dy[i_10]][x + dx[i_10]])
            * (visit[y+dy[i_10]][x+dx[i_10]] <= depth)):
                pathfinder(graph,(x+dx[i_10], y+dy[i_10]), visit, depth + 1)
for i_1 in range(i_t):
    i_n, i_k = map(int, input().split())
    ls_graph = [list(map(int, input().split())) for i_2 in range(i_n)]
    i_longest = 0
    # K 만큼 땅을 깍은 지형 새로 생성 모든 지점에 반복
    for i_3 in range(i_k + 1):
        for i_4 in range(i_n):
            for i_5 in range(i_n):
                ls_graph_k = copy.deepcopy(ls_graph)
                ls_graph_k[i_4][i_5] -= i_3
                # 새로 생성된 지형에서 최고높이 찾기
                i_highest = 0
                for i_6 in range(i_n):
                    for i_7 in range(i_n):
                        if ls_graph_k[i_6][i_7] > i_highest:
                            i_highest = ls_graph_k[i_6][i_7]
                # 새로 생성된 지형에서 최고 지점 찾기
                lst_highest = []
                for i_8 in range(i_n):
                    for i_9 in range(i_n):
                        if ls_graph_k[i_8][i_9] == i_highest:
                            lst_highest.append((i_9, i_8))
                # 최고지점부터 길찾기
                for tp_1 in lst_highest:
                    ls_visit = [[0] * i_n for i_11 in range(i_n)]
                    # 깊이 설정
                    i_depth = 1
                    pathfinder(ls_graph_k, tp_1, ls_visit, i_depth)
                    # 깊이 가장 깊은 지점 찾기
                    i_depth_max = 0
                    for i_12 in range(i_n):
                        for i_11 in range(i_n):
                            if ls_visit[i_12][i_11] > i_depth_max:
                                i_depth_max = ls_visit[i_12][i_11]

                    if i_depth_max > i_longest:
                        i_longest = i_depth_max
    print(f'#{i_1 + 1} {i_longest}')