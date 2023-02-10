# SWEA 1208 Flatten

from collections import deque

for t in range(1, 11):
    N = int(input())
    # 덤프 횟수를 입력받는다.
    boxes = deque(sorted(list(map(int, input().split())), reverse=True))
    # 상자들의 높이를 입력받아 리스트로 만들고 내림차순으로 정렬한다.

    for i in range(N):
        max_num = boxes.popleft() - 1
        min_num = boxes.pop() + 1
        boxes.append(max_num)
        boxes.append(min_num)
        boxes = deque(sorted((boxes), reverse=True))
    # 제일 높은 상자 높이에서 1을 빼고 다시 해당 높이를 리스트에 더해준다.
    # 제일 낮은 상자 높이에는 1을 더하고 다시 해당 높이를 리스트에 더해준다.
    # 이 과정을 덤프 횟수만큼 반복한다.

    print(f'#{t} {max(boxes) - min(boxes)}')
    # 최고 높은 상자 높이와 최고 낮은 상자 높이의 차를 출력한다.
