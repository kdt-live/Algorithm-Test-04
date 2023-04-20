# 퍼펙트 셔플
T = int(input())
for t in range(1, T+1):
    t_case = '#' + str(t)
    N = int(input())
    words = input().split()
    answer = []
    if len(words) % 2 == 0:
        wd1 = words[0:(N//2)]
        wd2 = words[(N//2):]
        for i in range(len(wd2)):
            answer += [wd1[i], wd2[i]]
    else:
        wd1 = words[0:(N//2)+1]
        wd2 = words[(N//2) + 1:]
        for j in range(len(wd2)):
            answer += [wd1[j], wd2[j]]
        answer += [wd1[-1]]
    print(t_case, *answer)