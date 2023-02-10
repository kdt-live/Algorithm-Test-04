T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    n_list = input().split()
    answer = []
    if n % 2 == 0:
        for x in range(n//2):
            answer.extend([n_list[x], n_list[n//2+x]])
    else:
        for x in range(n//2):
            answer.extend([n_list[x], n_list[n//2+1+x]])
        answer.append(n_list[n//2])
    print(f'#{test_case}', *answer)