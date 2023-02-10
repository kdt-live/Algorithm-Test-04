TC = int(input())
for test_case in range(1,TC+1):
    vowel = ['a', 'e', 'i', 'o', 'u']
    word = list(input())

    for i in range(len(word)):
        if word[i] in vowel:
            word[i] = ''
    print(f'#{test_case}',''.join(word))
