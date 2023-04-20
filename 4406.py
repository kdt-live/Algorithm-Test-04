T = int(input())
for t in range(1, T + 1):
    word = input()

    # 모음을 반복해줘
    for n in ["a", "e", "i", "o", "u"]:
        # 단어에 해당 모음이 카운트 된 수만큼 반복해줘
        for __ in range(word.count(n)):
            # 해당 모음이 있다면 없애줘
            word = word.replace(n, "")
    
    print(f"#{t} {word}")