for i in range(10):
    n=int(input())
    graph=list(map(int,input().split()))
    for _ in range(n):
        graph[graph.index(max(graph))]-=1
        graph[graph.index(min(graph))]+=1
    print(f"#{i+1} {graph[graph.index(max(graph))]-graph[graph.index(min(graph))]}")