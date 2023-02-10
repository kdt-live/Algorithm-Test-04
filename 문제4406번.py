T = int(input())

vowel = ['a', 'e', 'i', 'o', 'u']

for test_case in range(1, T+1):
    data = input()

    for i in data:
        if i in vowel:
            data = data.replace(i,'')

    print("#{} {}". format(test_case, data))