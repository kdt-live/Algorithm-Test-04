# 1949 [모의 SW 역량테스트] 등산로 조성

import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x,y):
    global cnt,is_big

    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] < g[x][y]:
            cnt += 1
            dfs(nx,ny)
        elif is_big == 0 and 0 <= nx < n and 0 <= ny < n and g[nx][ny] - k < g[x][y]:
            cnt += 1
            is_big += 1
            big_dfs(nx,ny,g[x][y]-1)
    is_big = 0
    if cnt > 0: cnt_li.append(cnt)
    cnt = 0

def big_dfs(x,y,z):
    global cnt
    g2 = g.copy()
    g2[x][y] = z
    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and g2[nx][ny] < g2[x][y]:
            cnt += 1
            dfs(nx,ny)

d = [(1,0),(-1,0),(0,1),(0,-1)]
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    g = [list(map(int,input().split())) for _ in range(n)]
    max_g = max(map(max,g))
    cnt = 0
    is_big = 0
    cnt_li = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == max_g:
                dfs(i,j)
    print(max(cnt_li) + 1)