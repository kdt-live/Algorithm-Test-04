import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(input().split())
    half = N // 2 + N % 2
    result = []

    for i in range(N // 2):
        result.append(card[i])
        result.append(card[i + half])

    if N % 2 == 1:
        result.append(card[N // 2])

    print(f'#{t}', *result)