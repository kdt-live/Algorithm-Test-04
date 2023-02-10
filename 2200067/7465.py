'''
1208 Flatten
'''

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        max_n = max(arr)
        min_n = min(arr)
        max_lc = arr.index(max_n)
        min_lc = arr.index(min_n)
        arr[max_lc] -= 1
        arr[min_lc] += 1
    
    answer =max(arr) - min(arr)
    print(f'#{tc} {answer}')
