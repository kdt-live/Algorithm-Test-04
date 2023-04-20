T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    cards = input().split()
    results = []

    standard = N//2 if N%2 == 0 else N//2 + 1
    split_cards1 = cards[:standard]
    split_cards2 = cards[standard:]

    for index in range(standard):
        try:
            results.append(split_cards1[index])
            results.append(split_cards2[index])
        except:
            break
    
    print(f'#{test_case}', *results)