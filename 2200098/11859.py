# 반반
T = int(input())
for t in range(1, T+1):
    t_case = '#' + str(t)
    word = input()
    word_dict = {}
    answer = 'Yes'
    for alp in word:
        if alp in word_dict.keys():
            word_dict[alp] += 1
        else:
            word_dict[alp] = 1
    if len(word_dict.keys()) != 2:
        answer = 'No'
    elif word_dict[word[0]] != 2:
        answer = 'No'
    print(t_case, answer)