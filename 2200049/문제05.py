from collections import deque
def bfs(arr,i,visited):
  q = deque()
  visited[i]=True
  q.append(i)
  while q:
    ci = q.popleft()
    for j in range(1,N+1):
      if arr[ci][j]==1 and not visited[j]:
        visited[j]=True
        q.append(j)
for idx in range(int(input())):
  N,M = map(int,input().split())
  arr = [[0]*(N+1) for _ in range(N+1)]
  for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1
  visited = [False]*(N+1)
  cnt=0
  for i in range(1,N+1):
    if not visited[i]:
      cnt+=1
      bfs(arr,i,visited)
  print(f"#{idx+1}",cnt)