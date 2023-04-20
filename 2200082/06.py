# 11856. 반반
"""
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
"""
import collections

TC = int(input())
for t in range(1, TC+1):
    S = input()
    s_cnt = collections.Counter(S).most_common()
    if len(s_cnt) == 2:
        if s_cnt[0][1] == s_cnt[1][1] == 2:
            case_result = 'Yes'
        else:
            case_result = 'No'
    else:
        case_result = 'No'
    
    print(f"#{t} {case_result}")