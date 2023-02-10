import sys
sys.stdin = open('2200053/input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) # N : 정점, M : 간선

    #인접리스트 만들기
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    # print(graph)