T = int(input())

for _ in range(1,T + 1):
    text = input()
    temp = [i for i in text]
    long = len(set(temp))
    if long == 2:
        if temp.count(set(temp[0])) == temp.count(set(temp[1])):
            print(f'#{_} Yes')
        else:
            print(f'#{_} No')
    else:
        print(f'#{_} No')