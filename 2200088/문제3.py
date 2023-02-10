# Flatten
for t in range(1, 11):
    N = int(input()) 
    lst = list(map(int, input().split()))
    cnt = 0
    while True:
        if cnt == N:
            break
        cnt += 1
        big_index = lst.index(max(lst))
        small_index = lst.index(min(lst))
        lst[big_index] -= 1
        lst[small_index] += 1
    print(f'#{t} {max(lst)-min(lst)}')