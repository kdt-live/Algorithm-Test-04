T = int(input())
for _ in range(1,T+1):
    
    N = int(input())
    card = input().split()
    
    card1 = 0
    card2 = (N+1)//2
    print(f'#{_}',end=' ')
    
    for i in range(card2):
        print(card[card1+i],end=' ')
        
        if card2+i < N:
            print(card[card2+i],end=' ')
    print()