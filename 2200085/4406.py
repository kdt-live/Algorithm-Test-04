for t in range (int(input())):
    word = input()
    ans = ''

    for w in word:
        if w not in ['a', 'e', 'i', 'o', 'u']:
            ans += w
    
    print(f'#{t+1} {ans}')