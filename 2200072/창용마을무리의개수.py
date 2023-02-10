
def dfs(adj_list,v,visted):
  visted[v] = True
  
  for adj in adj_list[v]: # 2 5
      adj_list[v] = []
      if not visted[adj]:
          dfs(adj_list, adj,visted)

T = int(input())
for test_case in range(1,T+1):
    n,m = map(int, input().split())

    # 인접 리스트
    town = [[]*n for _ in range(n+1)]
    for _ in range(m):
        v1,v2 = map(int,input().split())
        town[v1].append(v2)
        town[v2].append(v1)

    visted = [False] * (n+1)
    
    count = town.count([]) -1 # 혼자도 무리다.
    for i in range(1,len(town)):
        if len(town[i]) > 0:
            dfs(town,i,visted)
            count += 1
    print(f'#{test_case} {count}')

    