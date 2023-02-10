#4 3499
from collections import deque
import math
t=int(input())

for i in range(t):
    n=int(input())

    deck=deque(input().split())
    half1=deque()
    half2=deque()
    new_deck=[]
    for J in range(math.ceil(n/2)):
        half1.append(deck.popleft())
    
    while len(deck)!=0:
        half2.append(deck.popleft())

    
    for K in range(math.ceil(n/2)):
        new_deck.append(half1.popleft())
        if len(half2)!=0:
            new_deck.append(half2.popleft())
    print(f'#{i+1}',end=' ')
    print(*new_deck)