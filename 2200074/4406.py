T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']

for test_case in range(1, T+1):
    string = input()
    new_string = ''
    
    for char in string:
        if char in vowel:
            continue

        new_string += char
    
    print(f'#{test_case} {new_string}')