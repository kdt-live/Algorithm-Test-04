T = int(input())
for t in range(T):
    N , M = map(int,input().split())
    graph = [[] for _ in range(N + 1)]  
    for _ in range(M):
        x , y = map(int,input().split())
        graph[y].append(x)
        graph[x].append(y)
    print(graph)

    print(f'#{t+1} ')                            