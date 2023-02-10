# 반반

TC = int(input())
for i in range(1, TC + 1):
    s = input()
    set_s = set(s)

    if len(set_s) != 2:
        print(f'#{i} No')

    else:
        a = s.count(list(set_s)[0])
        b = s.count(list(set_s)[1])
    
        if a == b == 2:
            print(f'#{i} Yes')
    
        else:
            print(f'#{i} No')