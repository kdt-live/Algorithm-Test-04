T = 10
for t in range(T) :
    cnt = int(input())
    heights = list(map(int,input().split()))
    for i in range(cnt) :
        for i in range(100) :
            if heights[i] == max(heights) :
                heights[i] -= 1
                break
        for i in range(100) :
            if heights[i] == min(heights) :
                heights[i] += 1
                break
        if (max(heights) == min(heights)) :
            break

    print(f'#{t+1} {max(heights) - min(heights)}')
