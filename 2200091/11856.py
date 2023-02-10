import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    s = input().strip()

    set_s = set(s)

    if len(set_s) == 2:
        print(f"#{i+1} Yes")
    else:
        print(f"#{i+1} No")