a= ['a','e','i','o','u']

b = int(input())

for i in range(1,b+1):
    c= list(map(str,input()))

    while True:
        if a[0] in c:
            c.remove(a[0])
        elif a[1] in c:
            c.remove(a[1])
        elif a[2] in c:
            c.remove(a[2])
        elif a[3] in c:
            c.remove(a[3])
        elif a[4] in c:
            c.remove(a[4])
        else:
            break
    print(f'#{i}',end=' ')
    print(''.join(map(str,c)))