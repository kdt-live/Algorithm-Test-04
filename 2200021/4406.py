# 4406 모음이 보이지 않는 사람

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

li = ['a','e','i','o','u']
for t in range(1,int(input())+1):
    s = input().rstrip()
    print(f'#{t}',end=' ')
    for i in s:
        if i not in li:
            print(i,end='')
    print()