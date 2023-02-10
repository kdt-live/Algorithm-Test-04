for t in range (int(input())):
    N = int(input())
    cards = input().split()
    ans = []
    l = 0
    r = (N+1) // 2

    for _ in range (N//2):
        ans.append(cards[l])
        ans.append(cards[r])

        l, r = l+1, r+1
    
    if N % 2:
        ans.append(cards[N//2])

    print(f'#{t+1}', *ans)