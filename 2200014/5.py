#5 1949
# 모르겠다
def dfs(j,k):
    global cnt
    
    visited[j][k]=True
    if k+1<n:
        if arr[j][k]>arr[j][k+1]:
            if visited[j][k+1]==False:
                cnt+=1
                visited[j][k+1]=True
                dfs(j,k+1)
    if j+1<n:
        if arr[j][k]>arr[j+1][k]:
            if visited[j+1][k]==False:
                cnt+=1
                visited[j+1][k]=True
                dfs(j+1,k)
    if j-1>=0 :
        if arr[j][k]>arr[j-1][k]:
            if visited[j-1][k]==False:
                cnt+=1
                visited[j-1][k]=True
                dfs(j-1,k)
    if k-1>=0:
        if arr[j][k]>arr[j][k-1]:
            if visited[j][k-1]==False:
                cnt+=1
                visited[j][k-1]=True
                dfs(j,k-1)

    
    return visited


t=int(input())

for i in range(t):
    
    n,k=map(int,input().split())
    arr= [ list(map(int,input().split()))for i in range((n))]
    
    
    
    for j in range(n):
        for k in range(n):
            cnt=0
            visited=[[False]*n for i in range(n)]
            if arr[j][k]==max(map(max,arr)):
                
                print(dfs(j,k),cnt)
                