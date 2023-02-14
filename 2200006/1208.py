# 1208번 - [S/W 문제해결 기본] 1일차 - Flatten
T = 10
for tc in range(1, T +1):
    N = int(input())
    num = list(map(int, input().split()))
    for i in range(N):
        max_num = max(num)
        min_num = min(num)
        index_max = num.index(max_num)
        index_min = num.index(min_num)
        num[index_max] -= 1
        num[index_min] += 1

    print(f'#{tc} {max(num)-min(num)}')