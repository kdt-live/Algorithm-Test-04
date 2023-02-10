for i in range(int(input())):
    n=int(input())
    graph=list(input().split())
    result=''
    if n%2==0:
        for x,y in zip(graph[:n//2],graph[n//2:]):
            result+=x+" "+y+" "
    else:
        for x,y in zip(graph[:n//2+1],graph[n//2+1:]):
            result+=x+" "+y+" "
        result+=graph[:n//2+1][-1]
    print(f"#{i+1} {result}")