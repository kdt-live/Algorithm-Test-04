# 반반

T = int(input())

for t in range(1, T + 1):
    S = input()
    SS = set(S)
    if len(SS) != 2:
        print(f"#{t} No")
    else:
        cnt1 = S.count(list(SS)[0])
        cnt2 = S.count(list(SS)[1])
        if cnt1 == 2 and cnt2 == 2:
            print(f"#{t} Yes")
        else:
            print(f"#{t} No")
    