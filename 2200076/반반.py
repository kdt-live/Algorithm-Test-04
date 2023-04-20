import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    string = input()
    for s in string:
        if string.count(s) != 2:
            print(f'#{t+1} No')
            break
    else:
        print(f'#{t+1} Yes')