# 반반 

T = int(input())

for t in range(T):
    cnt = 0
    S = input()

    for i in S:
       ans = S.count(i)
       if ans == 2:
           cnt += 1
           
    if cnt == 4:
        print(f'#{t+1} YES')
    else:
        print(f'#{t+1} No')


    




