t = int(input())
for i in range(1, t+1) :
    a = list(input())
    dict = {}
    for j in a :
        if j not in dict :
            dict[j] = 1
        else :
            dict[j] +=1
    cnt = 0
    for key, value in dict.items():
        if value == (len(a)//2) :
            cnt+=1
    if cnt == len(a) //2 :
        print(f"#{i} Yes")
    else :
        print(f"#{i} No")