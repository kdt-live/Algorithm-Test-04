# 퍼펙트셔플
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    card = input().split()
    part_a = []
    part_b = []
    ncard = []
    if n % 2:
        for i in range(n//2 + 1):
            part_a.append(card[i])

        for i in range(n//2 + 1, n):
            part_b.append(card[i])
    else:
        for i in range(n//2):
            part_a.append(card[i])

        for i in range(n//2, n):
            part_b.append(card[i])

    for i in range(len(part_b)):
        ncard.append(part_a.pop(0))
        ncard.append(part_b[i])
    if len(part_a):
        ncard.append(part_a.pop())
    
    print(f'#{t}', end=' ')
    print(*ncard)