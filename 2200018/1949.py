# 등산로 조심
from sys import stdin
stdin = open("input_1949.txt")
input = stdin.readline

def dfs(start) -> int:
    explored, stack, ans = set(), [start], []
    while stack:
        v = stack.pop()
        if v not in explored:
            explored.add(v)
            ans.append(v)
            for x in graph[v]:
                if x not in explored:
                    stack.append(x)
    return ans


for i in range(int(input())):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    max_height = max(map(max, matrix))
    apexes = [(x, y) for x in range(n) for y in range(n) if matrix[y][x] == max_height]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    graph = [[] for _ in range(n*n + 1)]

    for x in range(n):
        for y in range(n):
            for delta in range(4):
                a, b = x + dx[delta], y + dy[delta]
                if a < 0 or b < 0 or a >= n or b >= n:
                    continue
                if matrix[y][x] > matrix[b][a]:
                    graph[matrix[y][x]].append(matrix[b][a])

    for a in apexes:
        (x, y) = a
        route = dfs(matrix[y][x])

        