from collections import Counter
tc = int(input())
for t in range(1, tc+1):
    word = input()
    cnt = dict(Counter(word))
    is_t = 0

    for k, v in cnt.items():
        if v == 2 and len(cnt) == 2:
            is_t = 1
    if is_t:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')
