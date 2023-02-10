for i in range(1,11):
    dump = int(input())#덤프횟수
    box = list(map(int, input().split()))
    
    for _ in range(dump):
        high = max(box)
        low = min(box)
        if high == low:
            print(f'#{i} {0}')
            break
        else:
            hi_i = box.index(high)
            low_i = box.index(low)
            box[hi_i] -= 1
            box[low_i] += 1
    else:
        print(f'#{i} {max(box)-min(box)}')




