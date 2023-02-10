d = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(i,j,h,t,con):
    global r
    if r < t:
        r = t
    
    for dt in d:
        dx,dy = dt
        mi = i + dx
        mj = j + dy

        if 0<=mi<n and 0<=mj<n and visited[mi][mj] == False:
            if l[mi][mj] < h:
                visited[mi][mj] = True
                dfs(mi,mj,l[mi][mj],t+1,con)
                visited[mi][mj] = False

            else:
                if con == True:
                    for c in range(1,k+1):
                        if(l[mi][mj]-c+1)<=h:
                            visited[mi][mj] = True
                            con = False
                            dfs(mi,mj,l[mi][mj]-c,t+1,con)
                            visited[mi][mj] = False
                            con = True
    

tc = int(input())
for t in range(tc):
    n,k = map(int,input().split())
    l = []
    m = 0
    for _ in range(n):
        v = list(map(int,input().split()))
        if max(v)>m:
            m = max(v)
        l.append(v)

    r = 0
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if l[i][j] == m:
                visited[i][j] = True
                dfs(i,j,m,0,True)
                visited[i][j] = False

    print(f'#{t+1} {r+1}')
