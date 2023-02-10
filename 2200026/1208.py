# [S/W 문제해결 기본] 1일차 - Flatten D3
for i in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    while dump:
        max_height = max(height)  # 큰 값 저장
        min_height = min(height)
        max_index = height.index(max(height))  # 인덱스 찾아서 저장
        min_index = height.index(min(height))

        height[max_index] -= 1  # 인덱스위치로 값을 찾아서 -1
        height[min_index] += 1

        dump -= 1
    print(f'#{i} {max(height)-min(height)}')
