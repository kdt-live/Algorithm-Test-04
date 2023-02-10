t = int(input())
for i in range(1,t+1):
    alp = str(input())
    result = 0
    if alp[0] == alp[2] and alp[1] == alp[3]:
        result = 'Yes'
    elif alp[0] == alp[1] and alp[2] == alp[3]:
        result = 'Yes'
    elif alp[0] == alp[3] and alp[1] == alp[2]:
        result ='Yes'
    elif alp[0] == alp[1] == alp[2] == alp[3]:
        result ='No'
    elif alp[0] != alp[1] != alp[2] != alp[3]:
        result ='No'

    print(f'#{i} {result}')