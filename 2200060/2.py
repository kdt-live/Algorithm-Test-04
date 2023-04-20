T = int(input())
for t in range(1,T+1):
    a,b = map(int,input().split())
    LS = []
    for i in range(b):
        nums = map(int,input().split())
        if nums not in LS:
            