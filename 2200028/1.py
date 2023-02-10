import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    S = input()
    N = sorted(S)
    if N[0]==N[1] and N[2] == N[3] and N[0] != N[-1]:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')