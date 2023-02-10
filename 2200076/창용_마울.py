import sys
sys.stdin = open('input.txt', 'r')

def dfs(x):
    check[x] = True

    for j in village[x]:
        if not check[j]:
            dfs(j)
    return

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    village = [[] for _ in range(n+1)]
    check = [False] * (n+1)
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        village[a].append(b)
        village[b].append(a)

    for i in range(1, n+1):
        if not check[i]:
            dfs(i)
            cnt += 1

    print(f'#{t+1} {cnt}')