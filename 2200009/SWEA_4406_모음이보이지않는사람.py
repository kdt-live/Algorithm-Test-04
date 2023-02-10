st_mother = set('aeiou')
i_t = int(input())
for i_1 in range(i_t):
    s_input = input()
    s_output = ''
    for s_1 in s_input:
        if s_1  not in st_mother:
            s_output += s_1
    print(f'#{i_1 + 1} {s_output}')