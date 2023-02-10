import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())
for t in range(T):
    n = int(input())
    deck = input().split()
    new_deck = []

    if n & 1:
        a_deck = deque(deck[:n//2+1])
        b_deck = deque(deck[n//2+1:])
    else:
        a_deck = deque(deck[:n//2])
        b_deck = deque(deck[n//2:])

    for i in range(n):
        if i & 1:
            new_deck.append(b_deck.popleft())
        else:
            new_deck.append(a_deck.popleft())
    
    print(f'#{t+1}', *new_deck)