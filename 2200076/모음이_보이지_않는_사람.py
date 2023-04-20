import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
vowel = {'a', 'e', 'i', 'o', 'u'}
for t in range(T):
    string = input()
    new_s = ''
    for s in string:
        if s not in vowel:
            new_s += s
    print(f'#{t+1} {new_s}')