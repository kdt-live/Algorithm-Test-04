for idx in range(int(input())):
  N,K = map(int,input().split())
  arr = []
  for _ in range(N):
    arr.append(list(map(int,input().split())))
    #최대 공사가능 깊이만큼 다 깍아보기 (단, 최대지점 제외)
    #bfs로 어디까지 방문가능한지 구해보기
  maxn = max(map(max,arr))
  def bfs(tmp):
    print(tmp)
  for i in range(N):
    for j in range(N):
      if arr[i][j]!=maxn:
        for k in range(1,K+1):
          tmp = arr
          tmp[i][j]-=k
          bfs(tmp)