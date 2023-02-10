import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    result = ''
    N = int(input())
    card = input().split()
    if N % 2 == 0:
        front = card[:int(N/2)]  # int 안 붙이면 안됨. n / 2는 소수형으로 나오기 때문.
        back = card[int(N/2):]
        for n in range(int(N/2)):
            result += front[n] + ' ' + back[n] + ' '
    else:
        a = N//2 + 1
        front = card[:a]
        back = card[a:]
        for n in range(int(N//2)):
            result += front[n] + ' ' + back[n] + ' '
        result += front[-1]
    
    print(f'#{t} {result}')