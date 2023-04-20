T=int(input())
for i in range (1,T+1):
    N,K=map(int,input().split())
    mount=[list(map(int,input().split())) for _ in range (N)]
    #가장 높은 봉우리에서 시작해서 나올 수 있는 모든 경로를 찾는 코딩을 구현하지 못하였습니다. 
    high_mount=0
    start_list=[]
    for j in range (N):
        if high_mount>max(mount[j]):
            high_mount=max(mount[j])
    for m in range(N):
        for n in range(N):
            if mount[m][n]==high_mount:
                start_list.append((m,n))
    # 가장 높은 봉우리들의 인덱스를 튜플화하여 리스트 생성
    # 재귀적 DFS 알고리즘을 통하여 이동할 때마다 다시 알고리즘을 적용이 필요
    # 이 부분 구현을 하지 못하였습니다 

        