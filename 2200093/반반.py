TC = int(input())

for tc in range(1, TC + 1):
    S = list(map(str, input()))
    
    A = []
    B = []

    for i in range(4):
        if A != []:
            if S[i] == A[0] :
                A.append(S[i])
            else:
                B.append(S[i])
        else:
            A.append(S[i])
        # print(A)
        # print(B)
    
    if len(A) and len(B) == 2:
        if A[0] == A[1] and B[0] == B[1]:
            print(f'#{tc} Yes')
        else:
            print(f'#{tc} No')
    else:
        print(f'#{tc} No')