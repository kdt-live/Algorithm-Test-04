# 창용 마을 무리의 개수
from sys import stdin
stdin = open("input_7465.txt")
input = stdin.readline

def build_graph(a, b):
    graph[a].append(b)
    graph[b].append(a)

def dfs(start_vertex):
    explored, stack = {start_vertex, }, [start_vertex]
    while stack:
        v = stack.pop()
        if v not in explored:
            explored.add(v)

        for i in graph[v]:
            if i not in explored:
                stack.append(i)

    return explored


for i in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    result = set()
    
    for _ in range(m):
        a, b = map(int, input().split())
        build_graph(a, b)

    cnt = 0
    for u in range(1, n + 1):
        if u not in result:
            result = result.union(dfs(u))
            cnt += 1

    print(f"#{i + 1}", cnt)