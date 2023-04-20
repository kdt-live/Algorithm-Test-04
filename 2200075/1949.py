from collections import deque
T = int(input())
for t in range(1, T+1) :
    N, k = map(int,input().split())
    matrix = [list(map(int,input().split())) for y in range(N)]
    # print(matrix)
    max_mat = 0
    for y in range(N):
        max_mat = max(max_mat, max(matrix[y]))
    # print(max_mat)

    dxy = [(-1,0),(1,0),(0,1),(0,-1)]
    max_load = 0

    for y_2 in range(N) :
        for x_2 in range(N) :

            for i in range(1,k + 1) :

                matrix[y_2][x_2] -= i

                for y in range(N) :
                    for x in range(N) :
                        if matrix[y][x] == max_mat :

                            queue = deque()
                            queue.append((y,x,1))
                            len_road = []
                            while queue :
                                loc = queue.pop()
                                for dy, dx in dxy :
                                    if 0 <= loc[0] + dy < N and 0 <= loc[1] + dx < N and matrix[loc[0]][loc[1]] > matrix[loc[0] + dy][loc[1] + dx] :
                                        queue.appendleft((loc[0] + dy, loc[1] + dx, loc[2] + 1))
                                        # print(queue)
                                    else : 
                                        len_road.append(loc[2])
                            # print(len_road)
                            max_load = max(max_load, max(len_road))

                matrix[y_2][x_2] += i



    print(f'#{t} {max_load}')
    # print(max_mat)