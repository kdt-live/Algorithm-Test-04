# 반반 

T = int(input())

for t in range(1, T+1):
    string = sorted(list(input()))

    if string[0] == string[1] and string[2] == string[3] and string[1] != string[2]:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')
