T = int(input())

for tc in range(1, T+1):
    text = input()
    t1 = []
    t2 = []
    flag = 1

    for i in text:

        if len(t1) == 0 :
            t1.append(i)
        elif i == t1[0]:
            t1.append(i)
        elif len(t2) == 0:
            t2.append(i)
        elif i == t2[0]:
            t2.append(i)
        else:
            flag = 0
        # print(t1)
        # print(t2)
    if len(t1) != 2 or len(t2) != 2:
        flag = 0
    if flag == 1:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))