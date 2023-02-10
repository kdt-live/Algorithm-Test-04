import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

for i in range(test):
    n = int(input())
    card1 = deque()
    card2 = deque()

    tmp = list(input().split())

    for j in range(n):
        if n % 2 == 0:
            if j < n//2:
                card1.append(tmp[j])
            else:
                card2.append(tmp[j])
        else:
            if j <= n//2:
                card1.append(tmp[j])
            else:
                card2.append(tmp[j])

    print(f"#{i+1}", end=" ")
    for j in range(n):
        if j % 2 == 0:
            print(card1.popleft(), end=" ")
        else:
            print(card2.popleft(), end=" ")

    print()

