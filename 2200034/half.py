TC = int(input())
cnt = 0
for i in range(1, TC + 1):
    S = list(input())

    for a in range(4):

        if S.count(S[a]) == 2:
            cnt += 1
            if cnt == 4:
                print(f'#{i} Yes')
                cnt = 0

        elif S.count(S[a]) != 2:
            print(f'#{i} No')
            cnt = 0
            break
        
            

    
    