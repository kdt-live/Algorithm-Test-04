t=int(input())
for i in range(1,t+1) : 
    n=int(input())
    card = list(map(str,input().split()))
    first = []
    second = []
    result = []
    if n%2 == 0 :
        for j in range(0,((n//2))) :
            first.append(card[j])
        for k in range((n//2),n) :
            second.append(card[k])
        for s in range(len(first)) :
            result.append(first[s])
            result.append(second[s])
    else :
        for j in range(0,((n//2)+1)) :
            first.append(card[j])
        for k in range((n//2)+1,n) :
            second.append(card[k])
        for s in range(len(second)) :
            result.append(first[s])
            result.append(second[s])
        result.append(first[-1]) 
    real_result = ""
    for z in result :
        real_result +=z + " "       
    print(f"#{i} {real_result}")