import sys
sys.stdin = open('input.txt')
# 길이가 3인

T = int(input())

for t in range(1, T+1):
    word = input()
    list_word = list(word)

    lis = []
    cnt = 0
    for i in list_word:
        if i not in lis:
            lis.append(i)
            cnt += 1
        else:
            continue
    if cnt == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')