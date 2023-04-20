


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list1 = list(map(str,input().split()))

    list2 = []
    list3 = []

    shuffle = int(N /2 - 0.2) 

    for i in range(N): 
        if i <= shuffle: 
            list2.append(list1[i])
        elif i > shuffle and i < N:  
            list3.append(list1[i])


    result = []
    for i in range(N):
        if i%2 == 0:
            result.append(list2.pop(0))
        elif i%2 == 1:
            result.append(list3.pop(0))


    print("#{}".format(tc), *result)
