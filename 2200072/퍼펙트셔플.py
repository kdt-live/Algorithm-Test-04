from collections import deque

def suffle(d_card1, d_card2):
    new_card = []
    while len(d_card2) > 0:
        new_card.append(d_card1.popleft())
        new_card.append(d_card2.popleft())
    if d_card1:
        new_card.append(d_card1[-1])
        return new_card
    else:
        return new_card

T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    cards = input().split()
    if n%2: # 홀수
        cards_a = cards[:(n//2)+1]
        cards_b = cards[(n//2)+1:]
        print(f'#{test_case}',*suffle(deque(cards_a),deque(cards_b)))
    else:
        cards_a = cards[:n//2]
        cards_b = cards[n//2:]
        print(f'#{test_case}',*suffle(deque(cards_a),deque(cards_b)))