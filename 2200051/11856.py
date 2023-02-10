t=int(input())
word=[]
result=[]
for i in range(t):
    word=input()
    word=list(word)
    word.sort()
    if word[0]==word[1] and word[2]==word[3] and word[0]!=word[2]:
        result.append("Yes")
    else:
        result.append("No")
for i in range(t):
    print(f"#{i+1} {result[i]}")