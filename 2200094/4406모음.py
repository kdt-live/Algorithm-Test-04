

T = int(input())

for t in range(1, T + 1):
    word = input()
    result = ''

    for w in word:
        if w not in ['a', 'e', 'i', 'o', 'u']:
            result += w

    print(f"#{t} {result}")