# 11856 반반

import sys
sys.stdin = open('input_11856.txt', 'r')

T = int(input())
for t in range(T):
    s = input()
    if s.count(s[0]) == 2 and len(set(s)) == 2:
        print(f'#{t+1} Yes')
    else:
        print(f'#{t+1} No')