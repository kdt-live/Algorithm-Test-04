# 모음이 보이지 않는 사람

T = int(input())
for t in range(1, T + 1):
    word = input()
    word = word.replace("o","")
    word = word.replace("a","")
    word = word.replace("e","")
    word = word.replace("i","")
    word = word.replace("u","")
    print(f"#{t} {word}")