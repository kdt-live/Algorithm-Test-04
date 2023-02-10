# Flatten

for t in range(1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N):
        max_len = lst.index(max(lst)) 
        lst[max_len] -= 1
        min_len = lst.index(min(lst))
        lst[min_len] += 1

    print(f'#{t+1} {max(lst) - min(lst)}')










