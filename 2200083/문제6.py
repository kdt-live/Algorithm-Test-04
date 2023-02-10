# Flatten
# 박스의 최고점과 최저점, 두 값의 차이, 평탄화 작업
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        max_idx = box.index(max(box)) # 최고점 박스의 위치
        min_idx = box.index(min(box)) # 최저점 박스의 위치

        box[max_idx] -= 1 # 평탄화 작업
        box[min_idx] += 1

    print(f'#{tc} {max(box)-min(box)}')