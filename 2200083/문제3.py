# 모음이 보이지 않는 사람
# 입력되는 단어에 모음이 들어가면 제거
# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    s = input()
    gather = ['a', 'e', 'i', 'o', 'u']
    for i in gather:
        if i in s:
            s = s.replace(i, '')

    print(f'#{tc} {s}')
