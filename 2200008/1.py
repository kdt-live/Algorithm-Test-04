# 반반
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    s = input()
    set_s = set(s)
    if len(set_s) != 2:
        print(f'#{t} No')
        continue
    for chr in set_s:
        if s.count(chr) !=2:
            print(f'#{t} No')
            break
    print(f'#{t} Yes')