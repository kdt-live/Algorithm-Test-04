# 반반
from sys import stdin
stdin = open("input_11856.txt")
input = stdin.readline

for i in range(int(input())):
    chars = input().strip()
    s = set(chars)
    print(f"#{i + 1}", "YNeos"[all(True if chars.count(i) == 2 else False for i in s)&1==0::2])        