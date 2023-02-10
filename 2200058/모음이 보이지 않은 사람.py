words=['a','e','i','o','u']
for i in range(int(input())):
    word=input()
    for j in words:
        word=word.replace(j , "")
    print(f"#{i+1} {word}")