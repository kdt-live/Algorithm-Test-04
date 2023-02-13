for i in range(1,11) :
    n = int(input())
    s = list(map(int,input().split()))
    for j in range(n) :
        s.sort(reverse = True)
        s[0] -=1
        s[-1] +=1
    s.sort(reverse = True)
    result = s[0]-s[-1]
    print(f"#{i} {result}")