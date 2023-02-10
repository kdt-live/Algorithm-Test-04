TC = int(input())

for t in range(TC):
    S = input()
    dict_ = {}

    for i in S:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1

    if len(list(dict_.keys())) == 2:
        if dict_[list(dict_.keys())[0]] == dict_[list(dict_.keys())[1]]:
            print(f'#{t+1} Yes')

        else:
            print(f'#{t+1} No')
    else:
        print(f'#{t+1} No')