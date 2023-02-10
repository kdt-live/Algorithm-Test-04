def dfs(graph, start):
    visit = []
    stack = [start]

    while stack:
        node = stack.pop()
        
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    
    return visit

for t in range (int(input())):
    n, m = map(int, input().split())
    graph = {}
    visit = []
    ans = 0

    for i in range (m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    for key in graph.keys():
        if key in visit:
            continue
        
        else:
            visit.extend(dfs(graph, key))
            ans += 1
    
    ans += n - len(graph)

    print(f'#{t+1} {ans}')