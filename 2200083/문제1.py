# 반반
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s = input() # ABAB
    r_s = sorted(s)  # 문자열을 정렬시킴 : AABB

    # (조건문) 나열된 문자열의 인덱스 0, 1 / 2, 3 이 같으면서 1, 2이 같지 않을 경우
    if r_s[0] == r_s[1] and r_s[2] == r_s[3] and r_s[1] != r_s[2]: 
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
