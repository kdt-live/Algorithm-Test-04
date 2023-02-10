T=int(input())
for i in range(1,T+1):
    N=int(input())
    testcase=input().split()
    length=len(testcase)
    ans=[None]*length
    while True:
        length=len(testcase)
        if length%2==0:
            for j in range (length):
                if j<=(length//2-1 ):
                    ans[2*j]=testcase[j]
                else:
                    ans[1+(j-length//2)*2]=testcase[j]  
            print(f'#{i}',end=' ')
            print(*ans)
            break            
        else:
            ans[-1]=testcase.pop(length//2)