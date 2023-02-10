
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cards = list(input().split())
    result = []
    l = 0
    r = (n+1) // 2
    for i in range(n//2):
        result.append(cards[l])
        result.append(cards[r])
        l, r = l+1, r+1

    if n % 2:
        result.append(cards[n//2])

    print(f'#{tc}',' '.join(result))

