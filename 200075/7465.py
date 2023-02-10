T = int(input())
for t in range(1,T+1) :
    N, M = map(int, input().split())
    list1 = [[] for i in range(N + 1)]

    for i in range(M) :
        n1, n2 = map(int, input().split())
        list1[n1].append(n2)
        list1[n2].append(n1)

    # print(list1)
    visited = [False for i in range(N + 1)]
    # print(visited)

    cnt = 0
    while False in visited :
        for i in range(len(visited)) :
            # print(i)
            if visited[i] == False :
                visited[i] = True
                start = i
                break
        stack = [start]
        while stack :
            # print(f'visited = {visited}')
            for i in list1[stack.pop()] :
                # print(f'i = {i}')  
                if visited[i] == False :
                    visited[i] = True
                    stack.append(i)
                # print(visited)
                # print(list1)  
        cnt +=1
    print(f'#{t} {cnt-1}')
