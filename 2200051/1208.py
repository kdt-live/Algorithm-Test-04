result=[]
for _ in range(10):
    dump=int(input())
    height=list(map(int,input().split()))
    for j in range(dump):
        a=max(height)
        b=min(height)
        max_index=height.index(a)
        min_index=height.index(b)
        height[max_index]=a-1
        height[min_index]=b+1
    result.append(max(height)-min(height))
for i in range(10):
    print(f"#{i+1} {result[i]}")