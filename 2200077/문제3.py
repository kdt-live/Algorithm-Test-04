# 모음이 보이지 않는 사람

T = int(input())
vowel = 'aeiou'
         
for t in range(T):
    S = input()
    for i in vowel:
        S = S.replace(i, "")
    print(f'#{t+1} {S}')


