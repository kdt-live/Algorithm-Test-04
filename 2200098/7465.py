# 창용 마을 무리의 개수
T = int(input())
for t in range(1, T+1):
    t_case = '#' + str(t)
    N, M = map(int, input().split())
    linked = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        linked[n1] += [n2]
        linked[n2] += [n1]
    groups = [linked[1]]
    for i in range(1, N):
        groups.append([i] + linked[i])