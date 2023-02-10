# 등산로 조정
N, K = map(int, input().split())
nums_list = []
max_list = []
for _ in range(N):
    numlist = list(map(int, input().split()))
    max_list.append(max(numlist))
    nums_list.append(numlist)
max_num = max(max_list)
dx = [-1, 0, 1, 0]
dy = [0, -1, -1, 1]
max_xy = []
for i in range(N):
    for j in range(N):
        if nums_list[i][j] == max_num:
            max_xy.append((i, j))
# print(max_xy) # [(0, 0), (2, 3), (2, 4)]
result = [max_num]

for move in max_xy:
    x = move[0]
    y = move[1]
    while True:
        for n in range(4):
            new_x = x + dx[n]
            new_y = y + dy[n]

# 최댓값 기준으로 사방으로 돌면서... 낮을 때 찾고 아닌 경우엔 pass 해준다
# 또 움직였을 때 사방으로 돌면서 값을 저장하고 개수가 전과 비교했을 때 크면 큰 값으로 초기화...
# 이런식으로 하는 것 같은데 푸신 분들은 다들 함수를 사용하신거 보면 깔끔하게 하기 위한 용도이겠지만...
# 아직까지 함수가 낯설어서 코드 읽기가 힘들다ㅠ 그냥 읽기 싫은 거일 수도...
# 나름 문제를 보면서 못 풀겠다 라는 생각은 든 적이 없고 그냥 시간이 오래걸리거나 오류 나겠다 정도였는데
# 이 문제는 처음으로 못 풀겠다... 라는 생각이 난 것 같다ㅠ 접근 방식부터 어떻게 해야되는지 잘 감이 안왔다.