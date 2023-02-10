T = int(input())

def max_(matrix, z):   # 행렬의 최댓값 찾기
    list_ = []
    for x in range(z):
        for y in range(z):
            list_.append(matrix[x][y])
    else:
        result = max(list_)
        return result

def C(number, z):    # 최댓값의 좌표 튜플로 묶인 리스트로 반환
    list_ = []
    for x in range(z):
        for y in range(z):
            if matrix[x][y] == number:
                list_.append([x, y])
    else:
        return list_

# def dfs(x, y, cnt):
#     cnt += 1
#     if x <= -1 or x >= N or y <= -1 or y >= N:  # 범위 밖으로 나가게 되면 종료
#         return False
#     if visited[x][y] == False:      # 노드가 방문하지 않은경우 
#         visited[x][y] = True       # 해당 노드 방문 처리
#         dfs(x - 1, y)         # 재귀함수를 통해 인접 노드 탐색
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return cnt
#     return cnt

for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N):      
        for j in range(N):
            if matrix[i][j] - K >= 0: # 공사 조건 공사하려는 땅의 크기가 공사하려는 크기보다 크거나 같아야함
                matrix[i][j] = matrix[i][j] - K   
                A = max_(matrix, N)  # 최댓값
                B = C(A, N) # 최댓값의 좌표
                bool_ = True
                for b in B:
                    visited = [[False] * N for _ in range(N)]
                    while True:
                        x = b[0]
                        y = b[1]
                        if visited[x+1][y] == True and visited[x-1][y] == True and visited[x][y+1] == True and visited[x][y-1] == True:
                            break
                        else:
                            bool_ = True
                        cnt = 1
                        while bool_:
                            if matrix[x][y] > matrix[x][y+1]:
                                if y + 1 <= N:
                                    if visited[x][y+1] == False:
                                        visited[x][y+1] = True
                                        y += 1
                                        cnt +=1
                                    
                            elif matrix[x][y] > matrix[x][y-1]:
                                if y - 1 >= 0:
                                    if visited[x][y-1] == False:
                                        visited[x][y-1] = True
                                        y -= 1
                                        cnt +=1
                                    
                            elif matrix[x][y] > matrix[x+1][y]:
                                if x + 1 <= N:
                                    if visited[x+1][y] == False:
                                        visited[x+1][y] = True
                                        x += 1
                                        cnt +=1
                                    
                            elif matrix[x][y] > matrix[x-1][y+1]:
                                if x - 1 >= 0:
                                    if visited[x-1][y] == False:
                                        visited[x-1][y] = True
                                        x -= 1
                                        cnt +=1
                                    
                            else:
                                if result < cnt:
                                    result = cnt
                                bool_ = False
                    
                        
    print(result)