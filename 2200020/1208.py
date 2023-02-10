T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    box_list = sorted(list(map(int, input().split())), reverse=True)
    while dump != 0:
        box_list = sorted([box_list[0]-1] + box_list[1:-1] + [box_list[-1]+1], reverse=True)
        dump -= 1
    print(f'#{test_case} {box_list[0]-box_list[-1]}')