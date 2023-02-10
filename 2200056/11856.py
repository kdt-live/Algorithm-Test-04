# 반반
T = int(input())
for t in range(1, T+1):
    string = input() # 문자 받기
    result_dict = {} # 딕셔너리에 저장
    for i in string:
        if i not in result_dict: # 글자가 딕셔너리에 없으며
            result_dict[i] = 1 # 추가해주고 값은 1로
        elif i in result_dict: # 딕셔너리에 있으면
            result_dict[i] += 1 # 값에 1 추가
    
    if list(result_dict.values()) == ([2, 2]): # 딕셔너리 값이 2, 2 이면
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")