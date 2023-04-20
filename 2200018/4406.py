# 모음이 보이지 않는 사람
from sys import stdin
stdin = open("input_4406.txt")
input = stdin.readline

for i in range(int(input())):
    word = input().strip()
    ls = list("aeiou")
    for x in ls:
        word = word.replace(x, "")

    print(f"#{i + 1}", word)