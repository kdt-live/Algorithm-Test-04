# 4406 모음이 보이지 않는 사람

import sys
sys.stdin = open('input_4406.txt', 'r')

T = int(input())
d = ['a', 'e', 'i', 'o', 'u']
for t in range(T):
    s = input()
    for i in d:
        s = s.replace(i,'')
    print(f'#{t+1} {s}')