i_t = int(input())
for i_1 in range(i_t):
    i_n = int(input())
    ls_card = list(input().split())
    ls_front = ls_card[0:(len(ls_card) + 1) // 2]
    ls_back = ls_card[(len(ls_card) + 1) // 2:]
    ls_output = []
    for i_2 in range(i_n):
        if i_2 % 2 == 0:
            ls_output.append(ls_front[i_2//2])
        else:
            ls_output.append(ls_back[i_2//2])
    print(f'#{i_1 + 1}', end= ' ')
    print(*ls_output)