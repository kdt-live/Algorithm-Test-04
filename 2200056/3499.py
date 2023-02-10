# 퍼펙트 셔플
T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = input().split()
    # 홀수 개 일 경우 앞에 1개 더 가져가야 하니 나눠야하는 기준을 조건식으로 작성
    if len(num_list) % 2 == 0:
        n = len(num_list) // 2 - 1
    else:
        n = len(num_list) // 2
    # n을 기준으로 앞뒤로 나누기
    num_list_front = num_list[0:n+1]
    num_list_back = num_list[n+1:]
    
    # 번갈아 가면서 프린트 해줘야하기에 새로운 리스트에 번갈아가면서 자장해준다.
    result = []
    for i in range(n+1):
        try:
            result.append(num_list_front[i])
            result.append(num_list_back[i])
        except:
            pass
    print(f"#{t}", end= " ")
    print(*result)