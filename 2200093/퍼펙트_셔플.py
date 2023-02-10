T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split(' '))
    shuffle = []
    if N % 2 == 0:
        for i in range(N//2):
            shuffle.append(card[i])
            shuffle.append(card[i + (N//2)])
    else:
        for i in range((N-1)//2):
            shuffle.append(card[i])
            shuffle.append(card[i + ((N+1)//2)])
        shuffle.append(card[(N-1)//2])
        
    print(f'#{tc}', *shuffle)