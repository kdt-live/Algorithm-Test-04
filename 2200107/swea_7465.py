# SWEA 7465번 창용 마을 무리의 개수
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split()) # 마을 사람의 수 n, 관계 수 m
    li=[[] for nums in range(n+1)]
    # print(li)
    
    # # 인접 list 방식으로 풀려다가, True, False로 체크하려니 인접 matrix가 낫겠음.
    # for _ in range(m):
    #     p1, p2=map(int,input().split())
    #     li[p1].append(p2)
    #     li[p2].append(p1)
    # print(li)
    # ck=[[] for nums in range(n+1)]
    # for a in range(1,n+1):
    #     for _ in range(len(li[a])):
    #         ck[a].append(False)
    # print(ck)
    cond=True
    while cond:
        for i in range(1,n+1):
            for j in range(n-1):
                if ck[i][j]==False:
                    ck[i][j]=True
                    ck[j][i]=True