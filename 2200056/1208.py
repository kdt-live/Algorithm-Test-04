# 1일차 Flatten
for t in range(1, 11):
    n = int(input())
    num_list = list(map(int, input().split()))

    for _ in range(n):
        max_num = max(num_list) # 최댓값 변수
        min_num = min(num_list) # 최솟값 변수

        max_index = num_list.index(max_num) # 최댓값 인덱스 저장
        min_index = num_list.index(min_num) # 최솟값 인덱스 저장
        num_list[max_index] = max_num - 1 # 최댓값 인덱스에 -1
        num_list[min_index] = min_num + 1 # 최솟값 인덱스에 +1

    print(f"#{t} ", end="")
    print(max(num_list) - min(num_list))