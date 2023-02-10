N = int(input())

for t in range(1, N+1):
    string = input()
    set_string = set(string)

    if len(set_string) == 2:
        for s in set_string:
            if string.count(s) != 2:
                print(f'#{t} No')
                break
        else:
            print(f'#{t} Yes')
    else:
        print(f'#{t} No')