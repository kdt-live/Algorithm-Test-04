# 창용 마을 무리의 개수

def dfs(people, c, check):
    print('c',c)
    check[c] = True
    for i in people[c]:
        if not check[i]:
            print('i', i, check[i])
            dfs(people, i, check)

T = int(input())
for t in range(1, T + 1):
    N, M = list(map(int, input().split()))    #N:사람수, M:간선
   
    check = [False] * (N + 1)

    people = [[] for _ in range(N+1)]
    for a in range(M):
        num1, num2 = map(int, input().split())
        people[num1].append(num2)
        people[num2].append(num1)
    
    cnt = 0
    for b in range(1, N + 1):
        print('b:',b)
        if dfs(people, b, check) == True:
            ('b', b, 'check',check, cnt)
            cnt += 1
        






# 2
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3