import sys
sys.stdin = open('input.txt')

a = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for t in range(1, T+1):
    word = input()
    list_word = list(word)

    ans = []
    for i in list_word:
        if i not in a:
            ans.append(i)
        elif i in a:
            continue
    res = ''.join(ans)
    print(f'#{t} {res}')