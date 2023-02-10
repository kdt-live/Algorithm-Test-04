T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', input().translate(str.maketrans('aeiou', 'aaaaa')).replace('a',''))