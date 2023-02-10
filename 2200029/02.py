import sys

sys.stdin = open('s_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N + 1)
    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(start):
        stack = [start]
        visited[start] = True
        while stack:
            cur = stack.pop()
            for i in graph[cur]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
    # start에 하나 넣으면 그와 인접한 모든 사람들이 true가 됨.
    # false중에 인접한 false들이 있을거임. 그럼 그것 또한 하나의 무리가 됨. 고로 false를 start에 넣어봐야됨.
    cnt = 0
    while True:
        dfs(visited[1:].index(False) + 1)
        cnt += 1
        if False not in visited[1:]:
            break
    print(f'#{t} {cnt}')




     

