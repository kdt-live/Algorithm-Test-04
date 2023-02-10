dir = ((1,0),(0,1),(-1,0),(0,-1))
def dfs(y,x,cheight,cnt,change):
  visited[y][x]=True
  global ans
  ans=max(cnt,ans)
  for i in range(4):
    ny=y+dir[i][0]
    nx=x+dir[i][1]
    print("y",y,"x",x,"ny",ny,"nx",nx,"cnt",cnt,"change",change)
    if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
      nheight=arr[ny][nx]
      if cheight>nheight:
        visited[ny][nx]=True
        dfs(ny,nx,nheight,cnt+1,change)
        visited[ny][nx]=False
      elif nheight-K<cheight and change==False:
        tmp=arr[ny][nx]
        nheight=cheight-1
        arr[ny][nx]=nheight
        visited[ny][nx]=True
        dfs(ny,nx,nheight,cnt+1,True)
        visited[ny][nx]=False
        arr[ny][nx]=tmp
for idx in range(int(input())):
  N,K= map(int,input().split())
  arr=[]
  for _ in range(N):
    arr.append(list(map(int,input().split())))
  top = max(map(max,arr))
  visited = [[False]*(N+1) for _ in range(N+1)]
  ans=0
  for i in range(N):
    for j in range(N):
      if arr[i][j]==top:
        visited[i][j]=True
        dfs(i,j,arr[i][j],1,False)
        visited[i][j]=False
  print(ans)








'''
dir = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(y,x,height,arr,fix,cnt):
  global ans
  if ans<cnt:
    ans=cnt
  for id in range(4):
    ny=y+dir[id][0]
    nx=x+dir[id][1]
    if 0<=ny<N and 0<=nx<N:
      nheight = arr[ny][nx]         
      if not visited[ny][nx]:
        if height>nheight:
          visited[ny][nx]=True
          cnt+=1
          dfs(ny,nx,arr[ny][nx],arr,False,cnt)
          visited[ny][nx]=False
          cnt-=1
        else:
          if not fix and nheight-K<height:
            visited[ny][nx]=True
            cnt+=1
            fix=True
            tmp=arr[ny][nx]
            nheight=height-1
            dfs(ny,nx,nheight,arr,fix,cnt)
            visited[ny][nx]=False
            cnt-=1
            arr[ny][nx]=tmp
for idx in range(int(input())):
  N,K = map(int,input().split())
  arr = []
  for _ in range(N):
    arr.append(list(map(int,input().split())))
  visited = [[False]*(N+1) for _ in range(N+1)]
  maxn = max(map(max,arr))
  ans = 0
  for i in range(N):
    for j in range(N):
      if arr[i][j]==maxn:
        visited[i][j]=True
        dfs(i,j,arr[i][j],arr,False,1)
        visited[i][j]=False
  print(f"#{idx+1}",ans)
  '''