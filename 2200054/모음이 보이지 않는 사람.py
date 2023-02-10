import sys
input = sys.stdin.readline
t = int(input())
for tc in range(1, t + 1) :
    string = input()
    result = ''
    for i in range(len(string)) :
        if string[i] in ['a', 'e', 'i', 'o', 'u'] :
            continue
        result += string[i]

    print(f'#{tc} {result}')