from sys import stdin

stdin = open("input_1949.txt")
# stdin = open("sample_input.txt")
input = stdin.readline


def dfs(start, matrix, depth, K):
    global result
    (x, y) = start
    cur_height = matrix[y][x]

    for i in r(4):
        a = x + dx[i]
        b = y + dy[i]
        if not (N>a>=0 and N>b>=0):
            continue
        if matrix[b][a] == "X":
            continue
        # 서로에게 영향을 받지 않는 지도 케이스 생성(shallow copy 활용) 및 방문표시
        m = [row.copy() for row in matrix]
        m[y][x] = "X"
        if matrix[b][a] < cur_height:
            """
            공사를 하지 않는 경우
            """
            dfs((a, b), m, depth + 1, K=K)
        elif matrix[b][a] - cur_height < K:
            """
            다음 구간이 현재 구간보다 크거나 같지만 다음 구간을 줄이면 지나갈 수 있는 경우
            """
            m[b][a] = cur_height - 1  # 공사(최소 필요 공사 크기)
            dfs((a, b), m, depth + 1, K=0)
    else:
        """
        진행할 수 없는 경우
        """
        if result < depth:
            result = depth


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
