T=int(input())
for i in range (1,int(T)+1):
    testcase=list(input().strip())
    word_cnt=list(set(testcase))
    for j in word_cnt:
        if testcase.count(j)!=2:
            print(f'#{i}No')
            break
    else:
        print(f'#{i} Yes')