import sys

sys.stdin = open("input1.txt","r")
##1
T = int(input())
result = []
for _ in range(T):
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        result.append("Yes")
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        result.append("Yes")
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        result.append("Yes")
    else:
        result.append("No")
for i in range(0,T):
    print("#%s %s"%((i+1),result[i]))
    
    
