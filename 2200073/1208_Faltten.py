# 1208 Faltten

import sys
sys.stdin = open('input_1208.txt', 'r')

# T = int(input())
for t in range(10):
    n = int(input())
    # graph = [0]*(101)
    data = list(map(int, input().split()))
    max_ = max(data)
    min_ = min(data)
    # graph = dict((i, 0) for i in range(min_, max_+1))
    graph = {}
    for d in data:
        graph[d] = graph.get(d,0) + 1

    
    while n > 0:
        # keys = graph.keys()
        # max_ = max(keys)
        # min_ = min(keys)

        
        graph[max_] -= 1
        graph[max_-1] = graph.get(max_-1, 0) + 1
        
        graph[min_] -= 1
        graph[min_+1] = graph.get(min_+1, 0) + 1

        n -= 1

        if not graph[max_]:
            # graph.pop(max_)
            max_ -= 1
        if not graph[min_]:
            # graph.pop(min_)
            min_ += 1
        if min_ >= max_:
            break
        # if n >= graph[max_]:
        #     graph[max_-1] = graph.get(max_-1, 0) + graph[max_]
        #     n -= graph[max_]
        #     max_ -= 1

        #     graph[min_+1] = graph.get(min_+1, 0) + graph[max_]
        #     min_ += 1
        # else:
        #     break
        # if min_ >= max_:
        #     break
    # print(n, graph)
    print(f'#{t+1} {max_-min_}')

        # graph()
    # print(graph)