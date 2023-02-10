import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    string=list(input())
    letters=list(set(string))
    check=True
    for i in letters:
        if string.count(i)!=2:
            check=False
    if check:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")