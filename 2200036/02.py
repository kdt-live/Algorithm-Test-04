# 창용 마을 무리의 개수

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int,input().split()))
    cnt = 0
    mem = [[] for _ in range(N)]
    for _ in range(M):
        m1, m2 = map(int,input().split())
        
    print(f"#{t} {cnt}")        
