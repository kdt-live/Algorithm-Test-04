# 반반 D3
tc = int(input())
for i in range(1, tc+1):
    # set으로 중복을 제거해서
    s = list(set(input()))
    # 리스트 내의 길이가 2인지 아닌지 판단
    if len(s) != 2:
        print(f'#{i} No')
    else:
        print(f'#{i} Yes')
