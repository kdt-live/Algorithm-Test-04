# SWEA 7465번 창용 마을 무리의 개수
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    li=[[] for nums in range(n+1)]
    # print(li)
    for _ in range(m):
        p1, p2=map(int,input().split())
        li[p1].append(p2)
    print(li)