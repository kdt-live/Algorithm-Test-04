T = int(input())

for t in range(1, T+1):
    string = input()
    ans = ''
    for s in string:
        if s not in 'aeiou':
            ans += s
    print(f'#{t} {ans}')