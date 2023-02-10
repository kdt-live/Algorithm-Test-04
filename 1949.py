# 미완성 완성해서 실라버스에 낼 예정
# 막힌 부분 : 카운트를 어디서 어떻게 하는게 좋을지
# 막막한 부분 : 길은 어떻게 깍을지... 나와 똑같은 모든걸 밀고 봐야할지...

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
cnt = 0

def road(graph, I, J, n, C):
    C += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 네 방향으로 움직여줘
    for i in range(4):
        # 범위 밖에 안에있어야해
        if 0<= I + dx[i] < n and 0<= J + dy[i] < n:
            # 전 수보다 작아야해
            if graph[I][J] > graph[I + dx[i]][J + dy[i]]:
                I = I + dx[i]
                J = J + dy[i]
                road(graph, I, J, n, C)
        
    if C not in m_cnt:
        m_cnt.append(C)
    print(m_cnt)                        


for t in range(1, T + 1):
    N, chance = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 시작점을 구해줘
    start = 0
    for mx in mountain:
        if start < max(mx):
            start = max(mx)

    for i in range(N):
        for j in range(N):
            # 시작점과 값이 같다면 함수를 실행해줘
            if mountain[i][j] == start:
                road(mountain, i, j, N, cnt)