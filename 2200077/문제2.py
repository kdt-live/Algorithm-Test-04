# 창용 마을 무리의 개수 

T = int(input())

for t in range(T):
    N, M = map(int, input().split()) # 6 5 
    persons = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        v1, v2 = map(int, input().split()) # 1 2
        persons[v1].append(v2)
        persons[v2].append(v1)

    main_visited = [False] * (N + 1)
    
    re = []

    for j in range(1, N+1):
        visited = [False] * (N + 1)
        stack = [j]
        ans = []

        while stack:
            cur = stack.pop()
            for i in persons[cur]:
                if not visited[i]:
                    visited[i] = True
                    main_visited[i] = True
                    stack.append(i)
            for k in range(N+1):
                if visited[k] == True:
                    ans.append(k)
        re.append(set(ans))

    new_result = []

    for x in re:
        if x == set():
            new_result.append(x)
        elif x not in new_result:
            new_result.append(x)
    print(f'#{t+1} {len(new_result)}')






    




