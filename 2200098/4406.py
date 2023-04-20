# 모음이 보이지 않는 사람
T = int(input())
rmv_alp = 'aeiou'
for t in range(1, T+1):
    word = input()
    answer = ''
    for alp in word:
        if alp not in rmv_alp:
            answer += alp
    print('#' + str(t), answer)