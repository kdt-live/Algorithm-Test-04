for t in range(1, int(input()) + 1):
    card_n = int(input())
    card = list(map(str, input().split()))
        
    #카드의 절반을 구해줘
    if card_n % 2 == 0:
        half = card_n // 2
    else:
        half = card_n // 2 + 1

    # 절반을 잘라서 보관해줘
    a = card[:half]
    b = card[half:]
    # 하나씩 다시 넣어줘
    for i in range(half):
        card[i + i * 1] = a[i]
        try:
            card[i + 1 + i * 1] = b[i]
        except:
            pass       

    print(f'#{t}', *card)