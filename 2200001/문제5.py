# 창용 마을 무리의 개수
T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    people = [[] for _ in range(n+1)]
    
    for i in range(m):
        a, b = map(int, input().split())
        people[a].append(b)
        people[b].append(a)
    print(people)