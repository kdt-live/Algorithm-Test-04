import sys
sys.stdin = open('input_sample.txt', 'r')

T = int(input())

vowel = ['a', 'e', 'i','o', 'u']
for t in range(1, T+1):
    word = input()
    result = ""
    for alpha in word:
        if alpha not in vowel:
            result += alpha
    print(f'#{t} {result}')