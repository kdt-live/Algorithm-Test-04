# 모음이 보이지 않는 사람

aeiou = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for t in range(1, T + 1):
    words = list(input())
    result = []

    for i in words:
        if i not in aeiou:
            result.append(i)

    result2 = "".join(result)
    print(f'#{t} {result2}')            