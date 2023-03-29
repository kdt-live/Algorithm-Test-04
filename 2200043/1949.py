# SWEA 1949 등산로 조성

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N)]

    for n in range(N):
        graph[n].append(list(map(int, input().split())))
