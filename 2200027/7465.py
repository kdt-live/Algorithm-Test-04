T = int(input())

for _ in range(1,T + 1):
    man, line = map(int, input().split())
    graph = [[] for _ in range(man+1)]

    for _ in range(line):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * len(graph)
    visited[1] = True #1부터 시작이니깐
    stack = [1]

    nums = [i for i in range(1,man+1)]
    answer = [1]

    while stack:
        cur = stack.pop()

        for num in graph[cur]:
            if not visited[num]:
                visited[num] = True
                stack.append(num)
                answer.append(num)

    print('visited:',visited)
    print(graph)
    print(answer)
    print(visited)