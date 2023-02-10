# 창용 마을 무리의 개수
import sys
sys.stdin = open('input.txt')

def dfs(start):
    visit = [False]*n
    visit[start] = True
    stack = [start]

    while stack:
        cur = stack.pop()
        for i in rela[cur]:
            if not visit[i]:
                visit[i] = True
                stack.append(i)
    
    group = set()
    for i in range(n):
        if visit[i]:
            group.add(i)

    return tuple(group)

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    rela = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        rela[a-1].append(b-1)
        rela[b-1].append(a-1)
    rela_set = set()
    for i in range(n):
        rela_set.add(dfs(i))
    print(f'#{t} {len(rela_set)}')