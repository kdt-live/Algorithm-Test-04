i_n = int(input())
for i_1 in range(i_n):
    s_input = input()
    dc_input = {}
    for s_1 in s_input:
        dc_input[s_1] = dc_input.get(s_1, 0) + 1
    
    bool_checker = True
    for val_1 in dc_input.values():
        if val_1 != 2:
            bool_checker = False
            break

    if bool_checker == True:
        print(f'#{i_1 + 1} Yes')
    else:
        print(f'#{i_1 + 1} No')