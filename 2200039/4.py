T = int(input())
for _ in range(T):
    N = int(input()); first_deck = []; second_deck = []; result = ""
    cards = list(map(str,input().split()))
    if len(cards) % 2 == 0:
        for i in range(N):
            if i+1 <= N//2: first_deck.append(cards[i])
            else: second_deck.append(cards[i])
        for i in range(N//2):
            result += first_deck[i] + " "
            result += second_deck[i] + " "
    elif len(cards) % 2 == 1:
        for i in range(N):
            if i+1 <= (N+1) // 2: first_deck.append(cards[i])
            else: second_deck.append(cards[i])
        for i in range(len(second_deck)):
            result += first_deck[i] + " "
            result += second_deck[i] + " "
        result += first_deck[-1]
    print("#{} {}".format(_+1, result))