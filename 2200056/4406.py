# 모음이 보이지 않은 사람
T = int(input())
a = ["a", "e", "i", "o", "u"]
for t in range(1, T+1):
    string = input()
    for i in string:
        if i in a:
            string = string.replace(i,"")
    print(f"#{t} {string}")