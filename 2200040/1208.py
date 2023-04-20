import sys
sys.stdin = open('input.txt')

# for t in range(1, 11):
    
for t in range(1, 11):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    for _ in range(n):
        numbers.sort()
        numbers[-1] -= 1
        numbers[0] += 1
        numbers.sort()
        if (max(numbers) - min(numbers)) <= 1:
            print(f'#{t} {max(numbers) - min(numbers)}')
            break

    else:
        print(f'#{t} {max(numbers) - min(numbers)}')