from collections import deque

for tc in range(1, 1+ int(input())):
    #6 5 일때
    N, M = map(int, input().split()) # N은 사람의 수 M개의 줄에 걸쳐서(사람의 관계 수를 나타냄)

    #인접 리스트 생성 Key, Value 형태의 딕셔너리
    adj = {x + 1: [] for x in range(N)}

    for _ in range(M):    #5번의 주민 네트워크 
        a, b = map(int,input().split())  #a, b에 주민 번호를 넣음
        adj[a].append(b) #a주민의(숫자가 들어갈 거임) 정보에는 b주민하고 연결되있다는 것을 의미
        adj[b].append(a) #반대로 b주민은 a와 연결되어있으니 서로 상대방 네트워크 번호를 삽입
    visited = [0] * (N + 1) #0의 방문은 비워둔다.
    q = deque()
    cnt = 0  # 무리의 수

    #전체 무리를 찾기 위해 for문으로 큐에 넣음
    for i in range(1, N + 1):
        #방문하지 않았을 경우는
        if visited[i] == 0:
            cnt += 1
            q.append(i)     #큐에 값(주민의 번호)을 넣고
            visited[i] == 1  #방문 표시를 1로 남긴다.

        #bfs    
        while q:   #큐에 값이 없을때까지
            c = q.popleft() #하나씩 뺀다 처음에는 1을 빼는데 1로 탐색을 시작
            for neighbor in adj[c]:    #neighbor은 adj[1]에 들어가있는 2,5(1과 연결된 네트워크) 하나씩 받는다.
                if visited[neighbor] == 0:   #2는 방문하지 않았고    
                    q.append(neighbor)       #큐에 2을 삽입 for문이 끝나고 fifo로 하나씩 뺀다
                    visited[neighbor] = 1       #2를 방문하였으므로 2에 1값을 넣는다.
    print('#{} {}'.format(tc, cnt))


