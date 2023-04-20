T = int(input())
for t in range(1, T+1) :
    word = input()
    tnf = True

    for i in word :
        if word.count(i) != 2 :
            tnf = False
            break


    print(f'#{t}', end = ' ')
    if tnf == True : print('Yes')
    else : print('No')