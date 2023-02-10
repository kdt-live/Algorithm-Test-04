T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    mt_road = [list(map(int, input().split())) for _ in range(n)]
    max_total = 0
    select = []

    for rr in range(n):
        for cc in range(n):
            select.append(mt_road[rr][cc])
    peak = max(select)

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]


    for r in range(n):
        for c in range(n):
            if mt_road[r][c] == peak:
                stack = []
                stack.append(c)
                stack.append(r)
                total = 1
                cnt = 1

                while stack:
                    x = stack.pop()
                    y = stack.pop()

                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]

                        cnt -= 1                        
                        
                        if cnt == 0:
                            total += 1
                            
                            if 0 <= nx < n and 0 <= ny < n:
                                if mt_road[x][y] > mt_road[nx][ny]:
                                            cnt += 1
                                            stack.append(ny)
                                            stack.append(nx)


            if max_total < total:
                max_total = total

    print(f'#{i} {max_total}')