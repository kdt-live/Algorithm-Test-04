def dfs(graph, v, visit):
    visit[v] = True
    for i_3 in graph[v]:
        if visit[i_3] != True:
            dfs(graph, i_3, visit)

i_t = int(input())
for i_1 in range(i_t):
    i_n, i_m = map(int, input().split())
    ls_connect = [[] for i_5 in range(i_n + 1)]
    for i_2 in range(i_m):
        i_c1, i_c2 = map(int, input().split())
        ls_connect[i_c1].append(i_c2)
        ls_connect[i_c2].append(i_c1)
    lst_visit = [False] * (i_n + 1)
    i_cnt = 0
    for i_4 in range(1, i_n + 1):
        if lst_visit[i_4] == False:
            i_cnt += 1
            dfs(ls_connect, i_4, lst_visit)
    print(f'#{i_1 + 1} {i_cnt}')