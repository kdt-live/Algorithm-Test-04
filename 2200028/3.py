import sys
sys.stdin = open("input3.txt", "r")

vowel = ['a', 'e','i','o','u']

T = int(input())
for t in range(1, T+1):
    result = ''
    word = input()
    for i in word:
        if i not in vowel:
            result += i
    print(f'#{t} {result}')