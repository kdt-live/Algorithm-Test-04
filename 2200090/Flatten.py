def min_n(): #최소값
    min_1 = 9999 # 리스트에 없는 큰값을 넣어 계속 반복
    min_2 = 0
    for j in range(len(numbers)):
        if numbers[j] < min_1:
            min_1 = numbers[j]
            min_2 = j
    return min_2

def max_n(): # 최대값
    max_1 = 0
    max_2 = 0
    for i in range(len(numbers)):
        if numbers[i] > max_1:
            max_1 = numbers[i]
            max_2 = i
    return max_2

for t in range(1, 11):
    n = int(input())    
    numbers = list(map(int, input().split()))
    
    for k in range(n):
        numbers[max_n()] -= 1 # 평준화를 위해 가장 큰값은 -1
        numbers[min_n()] += 1 # 평준화를 위해 가장 작은 값은 +1
    print(f'#{t} {numbers[max_n()] - numbers[min_n()]}')