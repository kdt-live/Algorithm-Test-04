# N의 카드를 퍼펙트 셔플 -> 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만든다.
# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분

# 인덱스로 절반 나눠서 각각 다른 리스트에 저장한 뒤
# deque. or leftpop()으로 하나씩 꺼낸다.
import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for t in range(1, T+1):
    n = int(input())
    num = input().split()
    if n%2 ==0:
        cut = n//2
    else:
        cut = (n+1)//2

    lis = []
 
    num1 = deque(num[:cut])
    num2 = deque(num[cut:])
    ans = []
    for i in range(n):
        while True:
            if len(num1) == 0:
                break
            else:
                ans.append(num1.popleft())

            if len(num2) == 0:
                break
            else:
                ans.append(num2.popleft())
    res = ' '.join(ans)
    print(f'#{t} {res}')
            
