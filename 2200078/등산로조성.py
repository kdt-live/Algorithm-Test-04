def test(N, K):
    global data
    data = dict()
    # 입력 받기 
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            data[row[j]] = data.get(row[j], [])
            data[row[j]].append((i, j))

    # 가장 높은 봉우리의 높이
    peak = max(data.keys())
    # 각 봉우리 별로 최대 등산로를 찾는다
    ans = []
    for x in data[peak]:
        ans.append(answer(x, peak, N, K))
    
    return max(ans)

def answer(x, peak, N, K):
    # dfs를 활용한다
    i, j = x
    h = peak
    path = [(i, j)]
    dx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (di, dj) in dx:
        if (i+di, j+dj) not in path and 
            