t = int(input())
moeum = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, t+1):
    word = input()
    for ele in moeum:
        word = word.replace(ele, '')
    print(f'#{tc} {word}')