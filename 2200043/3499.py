# SWEA 3499 퍼펙트 셔플
from collections import deque

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    cards_num = int(input())
    cards = input().split()
    new_deck = []
    # 카드 수와 카드 이름을 입력받는다.
    # 순서가 새롭게 섞인 카드 덱을 저장할 빈 리스트를 만든다.

    if cards_num % 2 == 0:
        A_deck = deque(cards[:cards_num // 2])
        B_deck = deque(cards[cards_num // 2:])
    # 카드 수가 짝수이면 카드 덱을 두 개로 나누어 같은 양씩 저장한다.

    else:
        A_deck = deque(cards[:cards_num // 2 + 1])
        B_deck = deque(cards[cards_num // 2 + 1:])
    # 카드 수가 홀수이면 카드 덱 A에 한 장 더 많이 저장한다.

    while A_deck:
        new_deck.append(A_deck.popleft())
        if len(B_deck) == 0:
            break
        else:
            new_deck.append(B_deck.popleft())
    # 따로 저장한 카드 A 덱과 B 덱에서 카드를 한 장씩 가져와 새로운 카드 덱에 저장한다.

    print(f'#{t}', *new_deck)
    # 새로운 카드 덱을 출력한다.
