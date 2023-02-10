# 11856 반반
# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, 
# S에 정확히 두 개의 서로 다른 문자가 등장하고, 
# 각 문자가 정확히 두 번 등장하는 지 판별하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 
# 각 테스트 케이스는 다음과 같이 구성되었다.
#     ∙ 첫 번째 줄에 문자열 S가 주어진다.

# [출력]
# 각 테스트 케이스마다
#     ∙ 조건이 만족되면 “Yes”, 아니면 “No” 를 출력하라.
 
import sys
sys.stdin = open("0210_swea/01_text.txt", "r")

TC = int(input())

cnt =0
for i in range(1,TC+1):
    S = input()
    ls = [] # 문자열 삽입 리스트
    ls1 = [] # 중복 문자열 삽입 리스트
    for j in range(4):
        if S[j] not in ls:
            ls.append(S[j])
        else:
            ls1.append(S[j])
            ls.remove(S[j])
    if len(ls) == 0:
        if len(ls1) > 1:
            if ls1[0] == ls1[1]:
                print(f'#{i} No')
            else:
                print(f'#{i} Yes')
    elif len(ls) !=0:
        print(f'#{i} No')
    # elif 
    # print(ls)
    # print(ls1)
    
'''
ABAB
CCDD
EFFE
EEEE
NONE
'''