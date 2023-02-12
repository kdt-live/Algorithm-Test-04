from sys import stdin
stdin = open("input_1949.txt")
# stdin = open("sample_input.txt")
input = stdin.readline

def dfs(start, matrix, depth, K):
    global result
    (x, y) = start
    height = matrix[y][x]

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
            route = dfs((a, b), m, depth+1, K=K)
            if route > result:
                result = route
        elif matrix[b][a] - height < K:
            """
            다음 구간이 현재 구간보다 크거나 같지만 다음 구간을 1~c 만큼 줄이면 지나갈 수 있는 경우
            """
            m = [row.copy() for row in matrix]
            m[b][a] = m[y][x] - 1   # 최소 필요 공사 크기
            m[y][x] = "X"   # 공사 후 방문표시
            route = dfs((a, b), m, depth+1, K=0)
            if route > result:
                result = route
    else:
        """
        진행할 수 없는 경우
        """
        return depth

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
        dfs(apex, matrix, depth=1, K=K)

    print(f"#{i + 1}", result)