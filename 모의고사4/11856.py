tc = int(input())
for j in range(tc):
    s = input()
    d = {}
    for i in s:
        d[i] = d.get(i,0)+1
    
    if len(d) == 2:
        for i in s:
            if d[i] != 2:
                print(f'#{j+1} No')
                break
        else:
            print(f'#{j+1} Yes')
    else:
        print(f'#{j+1} No')