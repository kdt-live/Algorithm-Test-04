T = int(input())

for t in range(1, T+1) :
    s = input()

    for _ in range(5) :
        s = s.replace('a',"")
        s = s.replace('e',"")
        s = s.replace('i',"")
        s = s.replace('o',"")
        s = s.replace('u',"")
    print(f'#{t} {s}')    