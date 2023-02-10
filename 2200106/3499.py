t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cards = list(input().split())
    if n % 2 == 0:
        left_cards = [cards[i] for i in range(len(cards)//2)]
        right_cards = [cards[i] for i in range(len(cards)//2, n)]
    else:
        left_cards = [cards[i] for i in range(round(len(cards)/2)+1)]
        right_cards = [cards[i] for i in range(len(cards)//2+1, n)]
    ps_cards = []
    for i in range(n//2+1):
        try:
            ps_cards.append(left_cards[i])
            ps_cards.append(right_cards[i])
        except:
            pass
    print(f'#{tc} {"".join(ps_cards)}')