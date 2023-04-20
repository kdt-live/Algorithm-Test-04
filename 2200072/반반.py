import collections
TC = int(input())
for test_case in range(1,TC+1):
    word = list(input())
    word_count = collections.Counter(word)
    if len(word_count) == 2 and all(num == 2 for num in word_count.values()):
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
