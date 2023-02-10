# 3499 . 퍼펙트 셔플
# from math import *
# T = int(input())
# for t in range(T):
#     num = int(input())
#     res = []
#     input_list = list(input().split())
#     list_helf = input_list[:ceil(num/2)]
#     list_another = input_list[ceil(num/2):]
#     if num % 2 == 0:
#         for i in range(len(list_helf)):
#             res.append(list_helf[i])
#             res.append(list_another[i])
#     else:
#         for i in range(len(list_another)):
#             res.append(list_helf[i])
#             res.append(list_another[i])
#         res.append(list_helf[-1])
#     print(f'#{t + 1}', end= ' ')
#     print(*res)

#4406. 모음이 보이지 않는 사람
# vowel = ['a', 'e', 'i', 'o', 'u']
# T = int(input())
# for t in range(T):
#     res = []
#     input_list = list(input())
#     for i in input_list:
#         cnt = 0
#         for j in vowel:
#             if i == j:
#                 cnt = 1
#         if cnt == 0:
#             res.append(i)
#     print(f'#{t + 1}', end=' ')
#     print(*res, sep= '')

# 7465. 창용 마을 무리의 개수



# 11856. 반반
from collections import Counter
tc = int(input())
for t in range(tc):
    input_list = list(input())
    cnt = Counter(input_list)
    val = list(cnt.values())
    temp = 0
    for i in val:
        if i == 2:
            temp += 1
    if len(cnt) == 2 and temp == 2:
        print(f'#{t + 1} Yes')
    else:
        print(f'#{t + 1} No')





                        


    
        


