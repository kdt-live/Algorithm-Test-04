for t in range(1, 11):
    dump = int(input())
    ground = list(map(int, input().split()))

    for _ in range(dump):
        max_h = max(ground)
        min_h = min(ground)
        
        if max_h - min_h < 2:
            break
        else:
            ground[ground.index(max_h)] -= 1
            ground[ground.index(min_h)] += 1
    print(f'#{t} {max(ground)-min(ground)}')