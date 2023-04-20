TC = int(input())
for t in range(TC): 
    string = input()
    same_list = []
    no_same = []
    for i in string:
        if i in same_list and i not in no_same:
            same_list.remove(i)
            no_same.append(i)
        else :
            same_list.append(i)
    if same_list :
        print(f'#{t+1} No')
    else :
        print(f'#{t+1} Yes')