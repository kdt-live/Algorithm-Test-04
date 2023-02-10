#2 7465 
def dfs(start):
    global cnt
    visited[start]=True

    for i in arr[start]:
            
        if visited[i]==False:
            visited[i]=True
            dfs(i)
            
        
        
    return visited

t=int(input())

for i in range(t):

    n,m=map(int,input().split())
    visited=[False]*(n+1)
    arr=[[]for i in range(n+1)]
    cnt=0
    
    for j in range(m):
        a,b=map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    
    
    for k in range(1,n+1):
        if visited[k]==False:
            dfs(k)
            cnt+=1
    print(f'#{i+1} {cnt}')
