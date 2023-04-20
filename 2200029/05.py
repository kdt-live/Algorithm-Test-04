# 최대값 찾고 그 수의 위치 튜플을 stack에 추가.
# dfs. pop한 다음 pop한 수 보다 작은 수 stack에 추가
# 길이 찾는 로직 완성시키면. 어차피 깎는 건 나중에 하나씩 다 깍은거에 로직 넣으면 됨
import sys
sys.stdin = open('sample_input.txt', 'r')

# matrix만들고 최대값 위치 튜플로 stack에 저장
T = int(input())
for t in range(1, T+1):
    N, k = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    bong = 0
    stack = []
    for row in matrix:
        if max(row) > bong:
            bong = max(row)
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == bong:
                stack.append((i, j))

    
    
    while stack:
        cnt = 0
        length = []
        answer = 'no'
        while True:
            cur1, cur2 = stack.pop()
            if (cur1-1) in range(N) and matrix[cur1][cur2] > matrix[cur1-1][cur2]:
                stack.append((cur1-1,cur2))
                answer = 'ok'
            if (cur1+1) in range(N) and matrix[cur1][cur2] > matrix[cur1+1][cur2]:
                stack.append((cur1+1,cur2))
                answer = 'ok'
            if (cur2-1) in range(N) and matrix[cur1][cur2] > matrix[cur1][cur2-1]:
                stack.append((cur1,cur2-1))
                answer = 'ok'
            if (cur2+1) in range(N) and matrix[cur1][cur2] > matrix[cur1][cur2+1]:
                stack.append((cur1,cur2+1))
            cnt += 1
            if answer == 'no':
                length.append(cnt)
                break
    print(length)


# k아직 안함