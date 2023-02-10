# 창용 마을 무리의 개수

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    relation = [[] for j in range(n + 1)]
    chk = [True] + [False] * n
    result = 0
    
    # 마을 인맥 리스트를 완성한다.
    for j in range(m):
        u, v = map(int, input().split())
        relation[u].append(v)
        relation[v].append(u)
    
    # DFS를 활용해 무리의 개수를 센다.
    # 단, 이 때 센 무리는 두 명 이상일 때이다.
    for j in range(1, n + 1):
        stack = [j]
        flag = False
        
        while stack:
            person = stack.pop()

            for linked in relation[person]:
                if not chk[linked]:
                    chk[linked] = True
                    stack.append(linked)
                    flag = True
    
        if flag: result += 1
    
    # 타인과 관계가 없는 주민의 수를 더한다.
    for j in range(1, n + 1):
        if not chk[j]:
            result += 1
    
    print(f'#{i + 1} {result}')