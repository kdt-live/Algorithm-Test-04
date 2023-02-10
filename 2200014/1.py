#1 11856

t=int(input())
for i in range(t):
    arr=input()
    dic={}
    for j in arr:
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
    for k in dic:
        if dic[k]!=2:
            print(f"#{i+1} No")
            break
    else:
        print(f"#{i+1} Yes")