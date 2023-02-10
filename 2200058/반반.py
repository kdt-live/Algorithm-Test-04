for j in range(int(input())):
    ind={}
    s=list(input())
    for i in s:
        ind[i]=s.count(i)
    result=''
    x=list(ind.values())
    if len(set(s))==2:
        if x[0]==2 and x[1]==2 :
            result="Yes"
        else:
            result="No"
    else:
        result="No" 
    print(f"#{j+1} {result}")