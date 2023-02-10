


for tc in range(int(input())):
    list1 = list(map(str,input()))
    list2 = []
    list3 = ['a','e','i','o','u']
    for i in list1:
        if i in list3:
            continue
        else:
            list2.append(i)
    print('#{} {}'.format(tc+1,''.join(list2)))