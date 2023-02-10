# 등산로 조성
import sys
sys.stdin = open('input.txt')

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    cnt = 1
    stack = [(x, y, cnt)]
    cnt_l = []

    while stack:
        curx, cury, curcnt = stack.pop()
        curcnt += 1
        for dx, dy in move:
            nx = curx + dx
            ny = cury + dy
            if nx < 0 or ny < 0 or nx >= n or ny >=n:
                continue
            if mount[nx][ny] >= mount[curx][cury]:
                continue
            cnt_l.append(curcnt)
            stack.append((nx, ny, curcnt))
    if len(cnt_l) == 0:
        return 1
    return max(cnt_l)

def high(matrix:list):
    high_set = set()
    high = max(map(max, matrix))
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == high:
                high_set.add((i, j))
    
    return high_set


for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    mount = [list(map(int, input().split())) for _ in range(n)]
    roots = set()
    highs = high(mount)
    for x, y in highs:
        roots.add(dfs(x, y))

    for i in range(n):
        for j in range(n):
            for k_ in range(1, k+1):
                mount[i][j] -= k_
                for x, y in high(mount):
                    roots.add(dfs(x, y))
                mount[i][j] += k_
    print(f'#{t} {max(roots)}')