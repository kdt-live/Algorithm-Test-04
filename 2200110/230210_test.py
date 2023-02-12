from collections import deque


# 반반
TC = int(input())
for t in range(1, TC+1):
    S = input()
    same = []
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if S[i] == S[j]:
                if i not in same:
                    same.append(i)
    if len(same) == 2:
        print(f'#{t} Yes')

    else:
        print(f'#{t} No')


# 창용 마을 무리의 개수 (테스트케이스는 다 되는데 fail. 반례 못찾음)
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0 for _ in range(N+1)]

    friend = 0

    def dfs(start):
        stack = [start]
        visited[start] = 1

        while stack:
            cur = stack.pop()

            for i in graph[cur]:
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)

            if len(graph[cur]) == 0:
                global friend
                friend -= 1
                break

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            friend += 1

    print(f'#{t} {friend}')

# bfs로 ...
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0 for _ in range(N+1)]

    friend = 0

    def bfs(start):
        q = deque(start)
        visited[start] = 1

        while q:
            cur = q.popleft()

            for i in graph[cur]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)

    for i in range(1, N+1):
        if visited[i] == 0:
            bfs[i]
            friend += 1

    print(f'#{t} {friend}')


# [] [5] [3, 5] [2, 5] [] [1, 2, 3]

# 만약 무리 별 사람 수를 구하라고 하면 ...?


# 모음이 보이지 않는 사람
T = int(input())
for t in range(1, T+1):
    my_str = input()

    vowel = ['a', 'e', 'i', 'o', 'u']

    for i in vowel:
        if i in my_str:
            my_str = my_str.replace(i, '')
    print(f'#{t} {my_str}')


# 퍼펙트 셔플

T = int(input())
for t in range(1, T+1):
    N = int(input())
    given = input().split()

    if N % 2 == 1:
        given_1 = deque(given[: N//2 + 1])
        given_2 = deque(given[N//2 + 1:])

    else:
        given_1 = deque(given[: N//2])
        given_2 = deque(given[N//2:])

    new = deque()

    while True:
        if len(given_1) != 0:
            new.append(given_1.popleft())

        if len(given_2) != 0:
            new.append(given_2.popleft())

        if len(given_1) == 0 and len(given_2) == 0:
            break

    print(f'#{t}', *new)


# [모의 SW 역량테스트] 등산로 조성 (못품)
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    world = []

    for _ in range(N):
        world.append(list(map(int, input().split())))

    # 제일 큰 값 찾기
    real_max = 0
    for i in range(N):
        if real_max <= max(world[i]):
            real_max = max(world[i])

    max_ = []
    for i in range(N):
        for j in range(N):
            if world[i][j] == real_max:
                max_.append((i, j))

    # 순회하면서 최대 공사 등산로 찾기
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(len(max_)):
        max_[i][0] + dx[0]
        max_[i][1] + dy[0]
        i = i + dx[0]
        j = j + dx[0]
        world[i][j]


# [S/W 문제해결 기본] 1일차 - Flatten D3
for t in range(1, 11):
    dump = int(input())
    case = deque(map(int, input().split()))

    for i in range(dump):
        tmp_1 = max(case)
        tmp_2 = min(case)
        case.remove(max(case))
        case.append(tmp_1 - 1)
        case.remove(min(case))
        case.append(tmp_2 + 1)

    print(f'#{t} {max(case)-min(case)}')
