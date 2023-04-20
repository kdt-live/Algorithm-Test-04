# 반반
T = int(input())

for t in range(1,1+T):
    string = list(input())
    set_string = set(string)
    if len(set_string) == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')