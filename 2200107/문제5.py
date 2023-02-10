# SWEA 1949번 [모의 SW 역량테스트] 등산로 조성
T=int(input())

for tc in range(1,T+1):
    n,k=map(int,input().split())
    
    li=[list(map(int,input().split())) for _ in range(n)]
    # 가장 높은 봉우리값 찾기
    max_find_li=[]
    for _ in range(n):
        max_find_li.append(max(li[_]))
    # print(max_find_li)
    # print(max(max_find_li))
    
    # 가장 높은 봉우리의 위치 찾기
    max_index_li=[]
    iv=0
    for a in range(n):
        for b in range(n):
            if li[a][b]==max(max_find_li):
                print(f'a={a}, b={b}')
                max_index_li.append([a,b])
                iv+=1
    # print(max_index_li)


# print(li)
# from pprint import pprint
# pprint(li)
