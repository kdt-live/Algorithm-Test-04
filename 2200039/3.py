T = int(input())
for _ in range(T):
    word = input(); recognize = ""; vowel = ["a","e","i","o","u"]
    for i in range(len(word)):
        if word[i] in vowel: pass
        else: recognize += word[i]
    print("#{} {}".format(_+1, recognize))