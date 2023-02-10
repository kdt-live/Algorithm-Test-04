T = int(input())

for t in range(T):
    N = int(input())
    deck = list(input().split())
    suffle = []
    if N % 2 == 0:
        deck_A = deck[0:int(len(deck)/2)]
        deck_B = deck[int(len(deck)/2):]

    else:
        deck_A = deck[0:int(len(deck)/2)+1]
        deck_B = deck[int(len(deck)/2)+1:]
    

    while len(deck_A) != 0:   # A덱의 길이가 0이되면 종료
        if len(deck_A) != 0:
            suffle.append(deck_A.pop(0))
        if len(deck_B) != 0:
            suffle.append(deck_B.pop(0))
                
    print(f'#{t+1}', *suffle)
