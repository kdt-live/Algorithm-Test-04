# 창용 마을 무리의 개수
for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    relation = [False] * (n+1)

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    cnt = 0
    while True:
        if relation[1:] == [True]*(len(relation)-1): # 첫번째를 뺀 모든 값이 true이면 (다 돌았으면)
            break
        else:
            start = relation.index(False,1) # 시작 노드
            stack = [start] # 돌아갈 곳을 기록
            relation[start] = True # 시작 정점 방문 처리
            while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
                cur = stack.pop() # 현재 방문 정점(후입선출)
                for i in graph[cur]:
                    if not relation[i]: # relation가 False이면(방문하지 않았으면)
                        relation[i] = True
                        stack.append(i)
            cnt += 1 # 한 번 순회를 마치면 카운팅 해주기(무리의 개수)
    #         print(relation)

    # print("*",relation)
    print(f"#{t} {cnt}")
