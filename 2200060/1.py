# end = False
# T = int(input())
# for i in range(1,T+1):
#     S = input()
#     for j in S:
#         if S.count(j) == 2: # 2만 있으면 패스
#             pass
#         else:
#             end = True # 2개가 아닌게 있으면 True 로 바꿈
#             break
#     if end == True:
#         print(f'#{i} NO')
#     else:
#         print(f'#{i} YES')



T = int(input())
for t in range(1,T+1):
    S = sorted(list(input()))
    if S[0] == S[1] and S[2] == S[3] and S[1] != S[2]:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')



T = int(input())
for t in range(1, T+1):
    S = input()
    for i in S:
        if S.count(i) != 2:
            print(f'#{t} NO')
            break
    else:
        print(f'#{t} YES')



