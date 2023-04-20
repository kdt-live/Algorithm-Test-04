def dfs(x):
    if x == graph[x]:
        return x
    else:
        return dfs(graph[x])
t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    graph=[i for i in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        pa = dfs(a)
        pb = dfs(b)
        if pa > pb:
            pa, pb = pb, pa
        graph[pb] = pa
    visited=[False]*(n+1)
    res=0
    for i in range(1,n+1):
        p= dfs(i)
        if not visited[p]:
            visited[p] = True
            res += 1
    
    print(f"#{tc} {res}")
