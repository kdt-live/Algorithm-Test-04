import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    s = input().strip()
    ans = ""

    for char in s:
        if char not in "aeiou":
            ans += char

    print(f"#{i+1} {ans}")