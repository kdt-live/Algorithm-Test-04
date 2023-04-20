T = int(input())

for t in range(1, T+1) :
    s = input()
    s_li = list(s)
    
    if s_li[0] == s_li[1] == s_li[2] == s_li[3] :
        print(f'#{t} No') 

    else :     
        for _ in range(2) :
            s_li = list(s)
            s = s.replace(s_li[0],"",2)

        if len(s) == 0 :
            print(f'#{t} Yes')   
        else :
            print(f'#{t} No')       

        