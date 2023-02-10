T = int(input())
for t in range(1, T + 1):
    word = input()
    cnt = 0
    for i in word:
        if word.count(i) == 2:
            cnt += 1
    if cnt == 4:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')