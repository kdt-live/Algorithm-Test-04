T = int(input())

erase = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T+1):
    word = input()
    ans = ''
    for j in word:
        if j not in erase:
            ans += j
    
    print(f'#{i} ans')