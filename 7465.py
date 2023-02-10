import sys
sys.stdin = open("input.txt", "r")

# 함수로 dfs 정의
def dfs(graph, n, visited):
    # n은 방문도장
    visited[n] = True

    # 방문한 n의 그래프엔 뭐가 들어있어?
    for i in graph[n]:
        if not visited[i]:
            # 없다면 이걸로 함수를 반복해줘
            dfs(graph, i, visited)

T = int(input())

for t in range(1, T + 1):
    hum, nei = map(int, input().split())
    town = [[] for _ in range(hum+1)]

    # 방문 도장을 찍을 리스트를 만들어줘
    town_2 = [False] * (hum+1)
    # 타운 0을 트루로 만들어줘
    town_2[0] = True

    for N in range(nei):
        hum_1, hum_2 = map(int, input().split())
        town[hum_1].append(hum_2)
        town[hum_2].append(hum_1)
    
    cnt = 0
    # false가 없어질때까지 함수를 돌려줘
    while False in town_2:
        cnt += 1
        dfs(town, town_2.index(False), town_2)
    
    print(f"#{t} {cnt}")
