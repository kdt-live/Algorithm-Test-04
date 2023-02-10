# 퍼펙트 셔플
T = int(input())
for t in range(1, 1+T):
    N = int(input())
    cards = list(input().split())
    cut = (N // 2) + (N % 2)

    front = cards[0:cut]
    back = cards[cut:]
    lst = []
    for i in range(cut):
        try:
            lst.append(front[i])
            lst.append(back[i])
        except:
            pass
    print(f'#{t}', *lst)