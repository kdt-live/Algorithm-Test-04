# SWEA에 제출하면 오답으로 나오는데 이유가 궁금합니다.. 제가 어떤 부분을 놓친건지 모르겠습니다.

T = int(input())

for t in range (1, T+1) :
    S = list(input())
    ans = ''
    for i in S :
        for j in S :
            if S.count(i) and S.count(j) == 2:
                ans = 'Yes'
            else : 
                ans = 'No'
    print(f"#{t} {ans}")