T=int(input())
deny=['a', 'e', 'i', 'o', 'u']
for i in range (1,T+1):
    testcase=input()
    ans=''
    for j in testcase:
        if j not in deny:
            ans+=j
    print(f'#{i} {ans}')