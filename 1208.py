import sys
sys.stdin = open("input.txt", "r")
for t in range(1, 11):    
    move = int(input())
    box = list(map(int, input().split()))

    for _ in range(move):
        # 오름차순으로 정렬해줘
        box = sorted(box)
        #큰수(마지막)에는 - 작은수(첫번째) + 해줘
        box[0] += 1
        box[99] -= 1

    # 마지막은 정렬이 안돼있으니 max, min
    print(f"#{t} {max(box) - min(box)}")