for i in range(1,11):
    c=int(input())
    
    b = list(map(int,input().split()))
    for j in range(c):
        b.append(max(b)-1)
        b.remove(max(b))
        b.append(min(b)+1)
        b.remove(min(b))

    print(f' #{i} {max(b)-min(b)}')

