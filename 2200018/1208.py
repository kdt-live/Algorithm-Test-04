# Flatten
from sys import stdin
stdin = open("input_1208.txt")
input = stdin.readline

for i in range(10):
    dumps = int(input())
    boxes = sorted(map(int, input().split()))
    
    while dumps:
        boxes[0] += 1
        boxes[-1] -= 1
        dumps -= 1
        boxes = sorted(boxes)

    print(f"#{i + 1}", boxes[-1] - boxes[0])
