T = int(input())

for test_case in range(1, T+1):
    char_dict = {}
    result = 'No'
    S = input()

    for char in S:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    if len(char_dict.keys()) == 2 and len(set(char_dict.values())) == 1:
        result = 'Yes'

    print(f'#{test_case} {result}')