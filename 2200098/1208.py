#[S/W 문제해결 기본] 1일차 Flatten
T = int(10)
for t in range(1, T+1):
    t_case = '#' + str(t)
    dump_cnt = int(input())
    h = [*map(int, input().split())]
    cnt = 0
    while cnt < dump_cnt:
        h[h.index(max(h))] -= 1
        h[h.index(min(h))] += 1
        cnt += 1
    answer = max(h) - min(h)
    print(t_case, answer)