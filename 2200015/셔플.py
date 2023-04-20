a= int(input())

for i in range(1, a+1):
    q=[]
    p=[]
    b=int(input())
    c =list(input().split())
    for j in range(b//2):
        q.append(c[j])
        if b%2 ==1:
            p.append(c[j+(b//2)+1])
        else:
            p.append(c[j+(b//2)])
        q.append(p[j])
    if b%2 ==1:
            q.append(c[(b//2)])

    s= (' '.join(map(str,q)))
    print(f'#{i}',end=' ')
    print(' '.join(map(str,q)))
 

    