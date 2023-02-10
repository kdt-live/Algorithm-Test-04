T = 10

for tc in range(1, T + 1):
    move = int(input())
    box = list(map(int, input().split()))
    
    for i in range(move):

        high = box.index(max(box))
        low = box.index(min(box))

        box[high] += 1
        box[low] -= 1

    answer = max(box) - min(box)
    print(f'#{tc} {answer}')