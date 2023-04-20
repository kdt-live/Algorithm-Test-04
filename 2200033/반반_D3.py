T = int(input())

for i in range(1, T+1):
    word = input()
    answer_list = []
    cnt = 0

    for j in word:
        answer_list.append(j)
    
    for k in answer_list:
        if answer_list.count(k) != 2:
            cnt += 1
            break
    
    if cnt == 0:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')
    