import sys
sys.stdin = open('2200053/input.txt')

T = int(input())

for t in range(1, T+1):
    string = list(input())

    vowel = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(string)):
        for j in vowel:
            if j in string:
                string.remove(j)
    # print(*string)
    print(f'#{t} {"".join(string)}')