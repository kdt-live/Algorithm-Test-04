T=int(input())
# 방문 체크리스트
def dfs(start): #DFS 알고리즘
    stack=[start]
    visited[start]=True  
    while stack:        
        cur=stack.pop()
        for adj in graph[cur]:
            if not visited [adj]: 
                visited[adj]=True
                stack.append(adj)
for i in range (1,T+1):
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for j in range(1,M+1):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited=[False]*(N+1)   # 0번 노드 때문에 M+1
    visited[0]=[True]# 0번 노드는 방문처리 
    cnt=0
    for k in range (1,N+1):   # for 문을 통해서 방문하지 못한, 즉 새로운 무리가 생길때마다 DFS 알고리즘 사용,cnt +
        if not visited[k]:
            dfs(k)
            cnt+=1
    print(f'#{i} {cnt}')