


T = int(input())

for t in range(1, T + 1):

    N = list(input())

    a = list(set(N))

    check=True

    for i in a:
        if N.count(i)!=2:
            check=False

    if check:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")