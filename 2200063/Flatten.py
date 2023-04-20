import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for t in range(10):
    N = int(input())
    list_ = list(map(int, input().split()))

    cnt = 0

    while cnt != N:
        list_ = sorted(list_)
        min_num = list_.pop(0) + 1
        max_num = list_.pop() - 1
        list_.append(min_num)
        list_.append(max_num)
        cnt += 1

    print(f'#{t+1} {max(list_)-min(list_)}')
