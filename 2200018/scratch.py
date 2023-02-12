# 등산로 조성
# 51개 중 32개
from sys import stdin
stdin = open("input_1949.txt")
# stdin = open("sample_input.txt")
input = stdin.readline

# def dfs(start: tuple, matrix: list[list[int]], depth: int, construction: int) -> int:
def dfs(start, matrix, depth, construction):
    global result
    c = construction
    d = depth
    (x, y) = start
    height = matrix[y][x]
    # m = [row.copy() for row in matrix]
    # m[y][x] = "X"

    # 이부분 주석처리해도 32
    # if height == "X":
    #     return d - 1

    for i in r(4):
        a = x + dx[i]
        b = y + dy[i]
        if a < 0 or b < 0 or a >= N or b >= N:
            continue
        if matrix[b][a] == "X":
            continue
        if matrix[b][a] < height:
            """
            공사를 하지 않는 경우
            """
            # 서로 영향을 받지 않는 지도 케이스 생성(shallow copy 활용)
            m = [row.copy() for row in matrix]
            m[y][x] = "X"
            route = dfs((a, b), m, d + 1, c)
            if route > result:
                result = route
        elif matrix[b][a] - height < c:
            """
            다음 구간이 이전 구간보다 크거나 같지만 다음 구간을 1~c 만큼 줄이면 지나갈 수 있는 경우
            """
            m = [row.copy() for row in matrix]
            m[y][x] = "X"
            for constructed in range(1, c + 1):
                """
                1부터 c까지 모든 경우 탐색
                """
                # print(m[b][a])
                m = [row.copy() for row in m]   # 이 줄 추가해도 32
                m[b][a] -= constructed
                route = dfs((a, b), m, d + 1, 0)
                if route > result:
                    result = route
    else:
        """
        진행할 수 없는 경우
        """
        return d

r = range
for i in r(int(input())):
    result = 1
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in r(N)]

    max_height = max(map(max, matrix))

    # 가장 높은 지점(출발점) 리스트 만들기
    apexes = [(x, y) for x in r(N) for y in r(N) if matrix[y][x] == max_height]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 각 꼭대기에서 dfs 실행
    for apex in apexes:
        dfs(apex, matrix, 1, K)

    print(f"#{i + 1}", result)