# 모음이 보이지 않는 사람

t = int(input())
vowel = 'aeiou'

for i in range(t):
    word = input()
    result = list()

    # 입력받은 단어를 순회하며 문자가 자음인 경우
    # result 리스트에 append한다.
    for letter in word:
        if letter not in vowel:
            result.append(letter)
    
    # join() 메서드를 사용해 result를 출력한다.
    print(f'#{i + 1} {"".join(result)}')