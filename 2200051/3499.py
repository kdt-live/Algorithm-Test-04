t=int(input())
result=[]
for i in range(t):
    n=int(input())
    # str=list(map(str,(input().split())))
    str=input().split()
    words=[0]*(n)
    if n%2 == 0:
        for j in range(n//2):
            words[2*j]=str[j]
        for k in range(n//2):
            words[2*k+1]=str[k+n//2]
        result.append(" ".join(words))
    else:
        n=n-1
        a=str.pop(n//2)
        for j in range(n//2):
            words[2*j]=str[j]
        for k in range(n//2):
            words[2*k+1]=str[k+n//2]
        words[-1]=a
        result.append(" ".join(words))
for i in range(t):
    print(f"#{i+1} {result[i]}")
            