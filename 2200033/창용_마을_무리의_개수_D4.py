T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    relation = [list(map(int, input().split())) for _ in range(k)]


    matrix = [[] for _ in range(n+1)]
    visited = [[False] for _ in range(n+1)]

    for x in range(k):
        matrix[relation[x][0]].append(relation[x][1])
        matrix[relation[x][1]].append(relation[x][0])

    cnt = 0
    stack = []
    for y in range(1, n+1):
        if visited[y][0] == False:
            cnt += 1
            stack.append(y)

            while stack:
                p = stack.pop()
                for h in matrix[p]:  
                    if visited[h][0] == False:
                        visited[h][0] = True
                        stack.append(h)
            
    print(f'#{i} {cnt}')

