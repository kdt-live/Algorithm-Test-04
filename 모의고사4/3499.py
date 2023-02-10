tc = int(input())
for j in range(tc):
    num = int(input())
    l = list(input().split())
    if num%2 == 0:
        l1 = l[0:num//2]
        l2 = l[num//2:num]
    else:
        l1 = l[0:num//2+1]
        l2 = l[num//2+1:num]
    print(f'#{j+1}',end=' ')

    if num%2==0:
        for i in range(num//2):
            print(l1[i],end = ' ')
            print(l2[i],end = ' ')
    else:
        for i in range(num//2):
            print(l1[i],end = ' ')
            print(l2[i],end = ' ')
        print(l1[-1],end = ' ')

    print()