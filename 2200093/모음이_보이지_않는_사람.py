T = int(input())

for tc in range(1, T + 1):
    word = input()
    new_word = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] not in vowel:
            new_word.append(word[i])
        else:
            pass
    print(f'#{tc}',  ''.join(new_word))