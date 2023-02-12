# 등산로 조심
from sys import stdin
# stdin = open("input_1949.txt")
stdin = open("sample_input.txt")
input = stdin.readline

def dfs(start: tuple, matrix: list[list[int]], depth: int, construction: int) -> int:
    # print("함수가 호출되었습니다.")
    global result
    c = construction
    d = depth
    (x, y) = start
    height = matrix[y][x]
    # print("height:", height)
    
    if height == "X":
        # print("returning")
        return d

    for i in r(4):
        a = x + dx[i]
        b = y + dy[i]
        if a < 0 or b < 0 or a >= N or b >= N:
            continue
        else:
            if matrix[b][a] == "X":
                continue
            
            if matrix[b][a] < height:
                """
                공사를 하지 않는 경우
                """
                # print(matrix[b][a], height, "공사하지 않음")   # 잘 나옴
                m = [row.copy() for row in matrix]
                m[y][x] = "X"
                # pprint(m)
                # print("d:", d)
                # result.add(dfs((a, b), m, d + 1, c))
                route = dfs((a, b), m, d + 1, c)
                if route > result:
                    result = route
                # print("result:", result)
            
            elif matrix[b][a] - height < c:
                """
                다음 구간이 이전 구간보다 크지만 다음 구간을 c 만큼 줄이면 지나갈 수 있는 경우
                """
                # print(matrix[b][a], height, "공사들어감")
                m = [row.copy() for row in matrix]
                m[y][x] = "X"
                # pprint(m)
                for constructed in range(1, c+1):
                    m[b][a] -= constructed
                    # print("d:", d)
                    route = dfs((a, b), m, d + 1, 0)
                    if route > result:
                        result = route
                    # result.add(dfs((a, b), m, d + 1, 0))


    else:
        return d
           
r, h = range, lambda x, y, m: m[y][x]
for i in r(int(input())):
    result = 0
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in r(N)]

    max_height = max(map(max, matrix))
    apexes = [(x, y) for x in r(N) for y in r(N) if h(x, y, matrix) == max_height]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    graph = {(x, y): set() for x in r(N) for y in r(N)}
    for l, s in graph.items():
        (x, y) = l
        for delta in r(4):
            a, b = x + dx[delta], y + dy[delta]
            if a < 0 or b < 0 or a >= N or b >= N:
                continue
            s.add((a, b))

    for l in apexes:
        dfs(l, matrix, 1, K)
    
    print(f"#{i + 1}", result)