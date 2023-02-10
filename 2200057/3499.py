T = int(input())

for t in range(1, T+1):
    N = int(input())
    li = list(input().split())
    li_left = list(reversed(li[:(N+1)//2]))
    li_right = list(reversed(li[(N+1)//2:]))
    print(f'#{t}', end=' ')
    for i in range(N):
        if i % 2:
            print(li_right.pop(), end=' ')
        else:
            print(li_left.pop(), end=' ')
    print()