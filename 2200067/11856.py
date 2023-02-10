'''
11856 반반
'''

T = int(input())
for tc in range(1, T+1):
    S = list(input())
    result = 0
    for i in range(4):
        count = 0
        for j in range(4):
            if S[i] == S[j]:
                count += 1
        if count == 2:
            result += 1
    if result == 4:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))