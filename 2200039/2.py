# 오마이갓,,, 어려워서 시간 내에 다 못 풀었어용...ㅠㅠㅠ이런 적이 없었는데🤪🤪🤪
# 아직 개인적으로 그래프랑 dfs 개념 정립이 덜 된것 같숩니답,,,
# 문제가 살짝이라도 꼬이면 어떻게 접근해야할지 좀 막막한데
# 그냥 많이 풀어보면서 경험을 늘려나가다보면 이 유형도 푸는 눈이 좀 트일까요...?
# 저만 이 유형을 유난히 어려워하는건지 아니면 다른 학생 분들도 대체로 많이들 어렵게 느끼시는건지 감이 잘 안 옵니다..ㅠ

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    visited = [False] * (N+1)
    people = [[] for i in range(N+1)]
    count = 0
    for i in range(M):
        a, b = map(int,input().split())
        people[a].append(b)
        people[b].append(a)
    start = 1; stack = [start]
    while stack:
        cur = stack.pop()
        for adj in people[cur]:
            if visited[adj] == False:
                visited[adj] = True
                stack.append(adj)
                count += 1
    print("#{} {}".format(_+1,count))