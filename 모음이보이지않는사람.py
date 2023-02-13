t = int(input())
for i in range(1,t+1) :
    a = list(input())
    result = []
    for j in a :
        if j == "a" :
            continue
        elif j == "e" :
            continue
        elif j == "i" :
            continue        
        elif j == "o" :
            continue
        elif j == "u" :
            continue
        else :
            result.append(j)
    r = ""
    for k in result :
        r+=k
    print(f"#{i} {r}")    