# 모음이 보이지 않는 사람 D3
vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())
for t in range(1, T+1):
    word = input()
    result = []
    for i in word:
        if i not in vowel:
            result.append(i)  # 모음 빼고 result에 append
    print(f'#{t}', end=" ")
    print(*result, sep="")
