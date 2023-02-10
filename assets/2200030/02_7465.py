'''7465. 창용 마을 무리의 개수
창용 마을에 p명의 //1번부터 P번 사람
두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 묶어서 하나의 무리라고 한다.//몇 개의 무리가 존재하는지 계산

[입력]  첫 번째 줄에 테스트 케이스의 수 T가 주어진다.//
각 첫 번째 줄에 사람의 수(P)와 알고 있는 사람의 관계 수를 나타내는 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.//
이후 M개의 줄//서로를 알고 있는 두 사람의 번호//같은 관계는 반복해서 주어지지 않는다.

[출력]  각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,//무리의 개수를 출력'''
'''2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3'''
#1 2
#2 1

import sys 
sys.stdin = open("input.txt")
from pprint import pprint

# 창용 마을에 p명의 //1번부터 P번 사람
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,하나의 무리라고 한다.//
# 몇 개의 무리가 존재하는지 계산
# 각 첫 번째 줄에 사람의 수(P)와 알고 있는 사람의 관계 수(R)를 나타내는 두 정수 P, R
# 이후 R개의 줄//서로를 알고 있는 두 사람의 번호//같은 관계는 반복해서 주어지지 않는다.

for T in range(1,int(input())+1):
    P, R = map(int,input().split())
    print(T, P, R)

    matrix = [ [ ] for _ in range(P+1) ]

    for r in range(R):
        P1, P2 = map(int,input().split())
        matrix[P1].append(P2)
        matrix[P2].append(P1)
        # print(P1,P2)
    pprint(matrix)

    # 방문 체크리스트
    visited = [False] * (P+1)
    # print(visited)

    # 인접노드 
    stack = []

    graph = [ [ ] for _ in range(P+1)]

    for n in range(R):  # n = 1
        cnt = 1
        for n1 in matrix[n]:    # matrix[n] = [2,5]
            start = n1  # start = n1 = 2

            # 방문기록 체크
            if visited[start] == False: # visited[2] = False
                visited[start] = True   # visited[2] = True
                # 인접노드 스택에 넣기
                if start not in stack:  # start = n1 = 2    # stack = []
                    stack.append(start) # stack = [2]
            
            elif visited[start] == True:    # start = 5
                if start in stack:  # stack = [2, 5, 1]
                    # print(visited)  
                    stack.remove(start) # stack = [2, 1]
                    pass
                    print(stack)

                # 스택이 빌 때까지
                elif len(stack) == 0:
                    cnt += 1
                    print(cnt)