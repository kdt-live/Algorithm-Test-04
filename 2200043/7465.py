# SWEA 7465 창용 마을 무리의 개수

T = int(input())
# 테스트 케이스 수를 입력받는다.

for t in range(1, T + 1):
    N, M = map(int, input().split())
    # 마을에 사는 사람의 수와 관계 수를 입력받는다.

    village = [[] for _ in range(N + 1)]

    for _ in range(M):
        p1, p2 = map(int, input().split())
        village[p1].append(p2)
        village[p2].append(p1)
    # 서로 알고 있는 두 사람의 번호를 입력받아 인접 리스트를 만든다.

    visited = [False] * (N + 1)
    # 인덱스 번호는 0부터이지만 사람의 번호는 1부터이기 때문에 편의상 N + 1개의 정점을 만든다.

    stack = []
    # 빈 스택을 만든다.

    cnt = 0
    # 관계가 있는 무리의 수를 구하기 위해 cnt 변수를 만들고 0을 설정한다.

    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            stack.append(i)
            cnt += 1

        while stack:
            num = stack.pop()

            for j in village[num]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
    # 마을의 1번 사람부터 시작해서 관계가 있는 사람이 누구인지 확인한다.
    # 1번 사람을 먼저 True로 만들고 1번 사람과 관계가 있는 사람들의 visited 여부를 true로 바꾸며 스택에 넣는다.
    # 그 후 1번 사람과 관계가 있는 2번 사람을 불러오고, 다시 2번 사람과 관계가 있는 또 다른 사람들의 visited 여부를 true로 바꾸며 스택에 넣는다.
    # 이 과정을 반복하여 1번 사람과 관계가 있는 모든 사람들의 visited 여부를 true로 바꿀 수 있다. 즉 이 사람들이 하나의 무리라고 볼 수 있다.
    # 그 후에는 visited 여부가 False인 또 다른 사람을 불러와 그 사람의 무리를 확인한다.
    # 위 과정을 반복해 무리의 개수를 카운트한다.

    print(f'#{t} {cnt}')
    # 무리의 개수를 출력한다.
