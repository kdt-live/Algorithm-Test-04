# 퍼펙트 셔플

T = int(input())
cards = int(input())
for t in range(1, T + 1):
    li = input().split()
    shuffle = []
    if cards % 2 == 0:
        list1 = li[0:len(li) // 2]
        list2 = li[len(li) // 2:]

        for i in range(len(list1)):
            shuffle.append(list1[i])
            shuffle.append(list2[i])
    else:
        list1 = li[0:len(li) // 2 + 1]
        list2 = li[len(li) // 2 + 1:]
        list2.append(0)

        for i in range(len(list1)):
            shuffle.append(list1[i])
            shuffle.append(list2[i])
        shuffle.pop()
        

    shuffle_str = " ".join(shuffle)
    print(f"#{t} {shuffle_str}")
    

# 왜 오답이지?