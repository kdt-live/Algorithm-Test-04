T = int(input())

for t in range(1,T+1) :
    N = int(input())
    card = input().split()
    result = [''] * len(card)

    if N%2:
        for i in range(N//2+1):
            result[2*i] = card[i]
        for i in range(N//2):
            result[2*i+1] = card[i+N//2+1]

    else:
        for i in range(N//2):
            result[2*i] = card[i]
            result[2*i+1] = card[i+N//2]

    print(f'#{t}',*result)