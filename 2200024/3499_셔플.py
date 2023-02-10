T = int(input())

for t in range(1, T+1) :
    new_li = []
    n = int(input())
    li = list(input().split())
    m = len(li)

    if n % 2 != 0 :
        n += 1
        
        li.append('0')
    # if n % 2 == 0 :
    a = 0
    b = n // 2
    for i in range(n // 2) :
        new_li.append(li[a])
        new_li.append(li[b])

        # print(new_li)
        a += 1
        b += 1
        
    if m % 2 != 0 :
        new_li.pop()
    print(f'#{t}', end=" ")
    print(*new_li)
    #else :
