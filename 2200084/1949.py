import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    map_N = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map_N[i][j] == max(max(map_N)):
                cnt = 1
                