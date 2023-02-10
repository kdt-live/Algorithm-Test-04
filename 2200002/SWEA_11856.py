


T = int(input())

for tc in range(1, T + 1):
    S = list(input())

    list1 = list(set(S))

    check = True

    for i in list1:
        if S.count(i) != 2:
            check = False

    if check:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")