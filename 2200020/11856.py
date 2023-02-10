T = int(input())
for test_case in range(1, T + 1):
    s = input()
    li = []
    for x in s:
        if x not in li:
            li.append(x)
        else:
            li.remove(x)
    print(f'#{test_case} Yes') if not li and len(set(s))==2 else print(f'#{test_case} No')