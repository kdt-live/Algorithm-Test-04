import sys
sys.stdin = open('input.txt', 'r')

# 못풀었습니다ㅠㅠ

def l_explore(x, y, cnt, k, hills, check):
    check[y][x] = True
    cnt += 1

    is_be = False
    for dx, dy in delta:
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if hills[y+dy][x+dx] < hills[y][x] and not check[y+dy][x+dx]:
                l_explore(x+dx, y+dy, cnt, k, hills, check)
                is_be = True
            
            elif hills[y+dy][x+dx] < hills[y][x] + k and not check[y+dy][x+dx]:
                hills[y+dy][x+dx] = hills[y][x] - 1
                l_explore(x+dx, y+dy, cnt, 0, hills, check)
                is_be = True
    
    if not is_be:
        length.append(cnt)
        return


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    hills = [list(map(int, input().split())) for _ in range(n)]

    start = max(hills[0])
    for i in range(1, n):
        if max(hills[i]) > start:
            start = max(hills[i])
    
    length = []
    delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for i in range(n):
        for j in range(n):
            if hills[i][j] == start:
                check = [[False]*n for _ in range(n)]
                cnt = 0
                l_explore(j, i, cnt, k, hills, check)

    print(f'#{t+1}', max(length))