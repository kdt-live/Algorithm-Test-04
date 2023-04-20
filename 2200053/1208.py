import sys
sys.stdin = open('2200053/input.txt')

for t in range(1, 11):
    dump = int(input())
    box_height = list(map(int, input().split()))

    for i in range(dump):
        max_height = max(box_height)
        min_height = min(box_height)

        idx_max_height = box_height.index(max_height)
        idx_min_height = box_height.index(min_height)

        box_height[idx_max_height] -= 1
        box_height[idx_min_height] += 1

    print(f'#{t} {max(box_height) - min(box_height)}')

# dump = 2
# box_height = [5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]

# for i in range(dump):
#     max_height = max(box_height)
#     min_height = min(box_height)

#     idx_max_height = box_height.index(max_height)
#     idx_min_height = box_height.index(min_height)

#     box_height[idx_max_height] -= 1
#     box_height[idx_min_height] += 1
# print(max(box_height) - min(box_height))