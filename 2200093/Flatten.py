T = 10

for tc in range(1, T + 1):
    move = int(input()) # 상자 이동 가능 횟수
    box = list(map(int, input().split())) # 상자 배열
    
    for i in range(move): # 상자 이동 가능 횟수 동안

        high = box.index(max(box)) # 최댓값 index
        low = box.index(min(box)) # 최소값 index

        box[high] += 1
        box[low] -= 1

    answer = max(box) - min(box)
    print(f'#{tc} {answer}')