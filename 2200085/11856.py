for t in range (int(input())):
    string = input()
    res = 0

    for i in range(4):
        count = 0
        
        for j in range(4):
            if string[i] == string[j]:
                count += 1
        
        if count == 2:
            res += 1
    
    if res == 4:
        print(f'#{t+1} Yes')
    
    else:
        print(f'#{t+1} No')