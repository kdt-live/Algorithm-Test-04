from collections import deque

T = int(input())

for i in range(1, T+1):
    n = int(input())
    word_list = list(input().split())
    ans = []
    up = deque()
    down = deque()

    if n % 2 == 1:
        p = (n // 2) + 1
    else:
        p = n // 2
    
    for j in range(p):
        up.append(word_list[j])

    for k in range(p, len(word_list)):
        down.append(word_list[k])
    
    if n % 2 == 1:
        while down:
            ans.append(up.popleft())
            ans.append(down.popleft())
        ans.append(up.popleft())
    else:
        while up:
            ans.append(up.popleft())
            ans.append(down.popleft())
    
    print(f'#{i}', end = ' ')
    print(*ans)