# 창용 마을 무리의 개수

# 창용 마을에는 N명의 사람이 살고 있다.
# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.

# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는
# 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
# 이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
# 같은 관계는 반복해서 주어지지 않는다.

# [출력]
# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 무리의 개수를 출력한다.

# 예제입력
# 2
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3	

# 예제출력
# #1 2
# #2 1

# 코드
'''
T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split()) # 사람 수 N, 관계 수 M
    matrix = [[] for j in range(N+1)]

    for k in range(M):
        n1, n2 = map(int, input().split())
        matrix[n1].append(n2)
    
    for l in matrix:
'''

T = int(input()) # 테스트케이스 수 T 입력받기

for i in range(1, T+1): # 테스트케이스 수 만큼 실행
    N, M = map(int, input().split()) # 사람 수 N과 관계 수 M 입력받기
    people = [[j] for j in range(1, N+1)] # 사람들 번호로 이차원리스트 만들기

    for k in range(M): # 관계 수 M 만큼 실행 
        n1, n2 = map(int, input().split()) # 관계 입력받기

        for l in people: # 사람들 이차원리스트 순회
            if n1 in l: # 관계에 속하는 사람이 있는 모임이 나올 경우,
                a = l # a에 모임리스트를 할당
                people.remove(l) # 사람들 리스트에서 해당 모임리스트 삭제

        for m in people: # 사람들 이차원리스트 순회
            if n2 in m: # 관계에 속하는 사람이 있는 모임이 나올 경우,
                b = m # b에 모임리스트를 할당
                people.remove(m) # 사람들 리스트에서 해당 모임리스트 삭제

        if a != b: # a, b에 할당된 모임이 다른 경우,
            people.append(a + b) # 두 개의 모임을 합쳐서 사람들 이차원리스트에 넣기
            a = [] # a와 b 다시 빈 리스트로 초기화
            b = []

    print(f'#{i} {len(people)}') # 최종적으로 사람들 이차원리스트의 길이 출력