T = int(input())
for t in range(T):
    N = int(input())
    card = list(map(str,input().split()))
    x = len(card)//2
    card_3 = []
    if len(card)%2 == 0:
        card_1 = card[:x]
        card_2 =card[x:]
        for _ in range(x):
            card_3.append(card_1[_])
            card_3.append(card_2[_])
    elif len(card)%2 != 0:
        card_1 = card[:x+1]
        card_2 =card[x+1:]
        for _ in range(x):
            card_3.append(card_1[_])
            card_3.append(card_2[_])
        card_3.append(card_1[-1])
    a = ''
    for j in card_3:
        a += j 
        a += ' '
    print(f'#{t+1} {a}')