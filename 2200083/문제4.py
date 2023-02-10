# 퍼펙트 셔플 
# 카드의 수가 짝수일 때와 홀수(N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.)일 때를 구분
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = input().split()
    result = [''] * len(card)
    if n%2: # 카드의 수가 홀수일 경우
        for i in range(n//2+1): 
            result[2*i] = card[i] # 0 1 2 3 
        for i in range(n//2):
            result[2*i+1] = card[i + n//2+1] # 4, 5, 6
    
    else: # 카드의 수가 짝수일 겅우
        for i in range(n//2):
            result[2*i] = card[i]
            result[2*i+1] = card[i+n//2]
    
    print(f'#{tc}', *result)
