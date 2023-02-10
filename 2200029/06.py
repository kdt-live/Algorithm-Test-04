import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    thumb = int(input())
    ls = list(map(int, input().split()))
    while True:
        ls[ls.index(max(ls))] = max(ls) - 1
        ls[ls.index(min(ls))] = min(ls) + 1
        thumb -= 1
        result = max(ls) - min(ls) 
        if thumb == 0 or result == 0 or result == 1:
            print(f'#{t} {result}')
            break


    