from pprint import pprint
# SWEA 7465번 창용 마을 무리의 개수
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split()) # 마을 사람의 수 n, 관계 수 m
    li=[[0]*(n+1) for nums in range(n+1)] # 각 정점의 번호를 매번 바꾸지 않게 위해 n+1.
                                      # li[0]은 쓰지 않음
    # print(li)

    # 인접 matrix 생성
    for _ in range(m):
        p1, p2=map(int,input().split())
        li[p1][p2]=1
        li[p2][p1]=1
    pprint(li)

    # 다녀온 정점 체크하기 위한 check list
    ck=[[True]*(n+1) for nums in range(n+1)]
    for a in range(1,n+1):
        for b in range(1,n+1):
            if li[a][b]==1:
                ck[a][b]=False
    pprint(ck)

    cnt=0 # while문 종료 조건 변수
    crowd=0 # 무리의 수

    False_index=[]
    cond=True
    while cond:
        for a in range(1,n+1):
            try:
                i=a
                j=ck[a].index(False)
                False_index.append([a,ck[a].index(False)])
            except:
                pass
        for ele in False_index[::-1]:
            i,j=ele
        # print(i,j)
        # try:
            if ck[i][j]==True:
                j+=1
                if ck[i][j]==False:
                    ck[i][j]=True
                    ck[j][i]=True
                    i=j
                    j=i
        # except:
            j=1
            cnt+=1
            print(f'i={i} cnt={cnt}')
        # if cnt==n:
        #     crowd+=1
        #     break


# try/except에서 i, j를 1씩 더하는 방식으로는 무리가 몇 개인지 체크가 안 됨.
#    cond=True
#     i=1
#     j=1
#     while cond:
#         try:
#             if ck[i][j]==True:
#                 j+=1
#                 if ck[i][j]==False:
#                     ck[i][j]=True
#                     ck[j][i]=True
#         except:
#             i+=1
# cnt+=1
        # print(f'i={i} cnt={cnt}')
    