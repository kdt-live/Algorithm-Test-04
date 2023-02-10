import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    S = input()
    # 중복 제거
    set_S = set(S)
    yes = 0
    # 개수 비교
    if len(set_S) == 2:
        for n in set_S:
            # 각 카운트 2인가?
            if S.count(n) == 2:
                yes += 1
    
    if yes == 2:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")