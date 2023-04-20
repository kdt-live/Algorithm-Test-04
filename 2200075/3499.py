T = int(input())
for t in range(1, T+1) :
    card_num = int(input())
    cards = list(input().split())
    # print(card_num)
    # print(cards)
    result = []

    i = 0
    i_2 = card_num//2
    if card_num % 2 == 1 :
        i_2 += 1
    print(f'#{t} ', end='')
    while len(result) != len(cards):
        # print(i, i_2)
        result.append(cards[i])
        i += 1
        i, i_2 = i_2, i
    print(*result)