# 창용 마을 무리의 개수

def dfs(people, c, check):
    check[c] = True
    for i in people[c]:
        if not check[i]:
            dfs(people, i, check)
   
T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))    #N:사람수, M:간선
   
    people = [[] for _ in range(N+1)]
    for _ in range(M):
        num1, num2 = map(int, input().split())
        people[num1].append(num2)
        people[num2].append(num1)
    
    check = [False] * (N + 1)
    cnt = 0
    for b in range(1, N + 1):
        if check[b] == False:
            dfs(people, b, check)
            cnt += 1
    
    print(f'#{t} {cnt}')