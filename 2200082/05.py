# 7465. 창용 마을 무리의 개수
"""
창용 마을에는 N명의 사람이 살고 있다.

사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.

두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.

두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,

이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.

창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는

두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.

이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.

같은 관계는 반복해서 주어지지 않는다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

무리의 개수를 출력한다.
"""
'''
def newGroup(group_no, mem1, mem2):
    group_name = 'group_' + str(group_no)
    a = set()
    a.add(mem1)
    a.add(mem2)
    groups.append(group_name)
    return a


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    connaissances = []
    for c in range(M):
        connaissances.append(list(map(int, input().split())))
    
    groups = []
    group01 = set()
    group01.add(connaissances[0][0])
    group01.add(connaissances[0][1])
    groups.append(group01)
    
    group_no = 1
    for c in connaissances:
        for g in groups:
            if c[0] in group01 or c[1] in group01:
                group01.add(c[0])
                group01.add(c[1])
            else:
                group_no += 1
                groups[-1] = newGroup(group_no, c[0], c[1])
                
            print(groups)