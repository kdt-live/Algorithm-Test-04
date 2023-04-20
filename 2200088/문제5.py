# 창용 마을 무리의 개수
T = int(input())
for t in range(1,1+T):
    N, M = map(int, input().split())

    matrix = [[] for _ in range(N+1)]
    visited = [False] *(N+1)

    for i in range(M):
        p1, p2 = map(int, input().split())
        matrix[p1].append(p2)
        matrix[p2].append(p1)
    # print(matrix)
    # print(visited)
    cnt = 0
    for i in range(len(visited)):

        if visited[i] == False and i != 0:
            cnt += 1
            stack = [i]
            visited[i] = True
            # print(stack)

            while stack:
                s = stack.pop()
                for j in matrix[s]:
                    if not visited[j]:
                        visited[j] = True
                        stack.append(j)
    print(f'#{t} {cnt}')
# # print(visited)
# print(cnt)
# print(visited)