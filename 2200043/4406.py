# SWEA 4406 모음이 보이지 않는 사람

T = int(input())
# 테스트 케이스 수를 입력받는다.

vowel = ['a', 'e', 'i', 'o', 'u']
# 알파벳 모음을 리스트로 만든다.

for t in range(1, T + 1):
    word = input()
    # 단어를 입력받는다.

    for v in vowel:
        word = word.replace(v, '')
    # 모음 리스트의 한 글자씩 불러오며 단어에 해당 모음이 있으면 없앤다.

    print(f'#{t} {word}')
    # 모음이 모두 제거된 문자열을 출력한다.
