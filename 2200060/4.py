import sys
sys.stdin = open('input.txt','r')

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     cards = list(input().split())
#     for i in range(N):
#         try:
#             if i % 2 == 1:
#                 cards[i] , cards[i+1] = cards[i+1] , cards[i]
#         except:
#             break    
#     print(cards)



# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     cards = list(input().split())
#     a = int(len(cards)/2)
#     cards_1 = cards[:a] # 앞
#     cards_2 = cards[a:] # 뒤
#     result_card = []
#     for i in range(N):
#         if i % 2 == 0:
#             if cards_1 == True:
#                 result_card.append(cards_1[0])
#                 cards_1.pop(0)
#         elif i % 2 != 0:
#             result_card.append(cards_2[0])
#             cards_2.pop(0)



#     print(f'#{t} {result_card}')

    


# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     cards = list(input().split())
#     a = int(len(cards)/2)
#     cards_1 = cards[:a+1] # 앞
#     cards_2 = cards[a+1:] # 뒤
#     result_card = []
#     for i in range(N):
#         if i % 2 == 0:
#             result_card.append(cards_1[0])
#             cards_1.pop(0)
#         else:
#             result_card.append(cards_2[0])
#             cards_2.pop(0)

#     result = ' '.join(result_card)
#     print(f'#{t} {result}')






# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     cards = list(input().split())
#     a = int(len(cards)/2)
#     cards_1 = cards[:a+1] # 앞
#     cards_2 = cards[a+1:] # 뒤
#     result_card = []
#     for i in range(N):
#         try:
#             if i % 2 == 0:
#                 result_card.append(cards_1[0])
#                 cards_1.pop(0)
#             else:
#                 result_card.append(cards_2[0])
#                 cards_2.pop(0)
#         except:
#             if cards_2:
#                 result_card.append(cards_2[0])
        

#     result = ' '.join(result_card)
#     print(f'#{t} {result}')


T = int(input())
for t in range(1,T+1):
    N = int(input())
    cards = list(input().split())
    a = int(len(cards)/2)
    cards_1 = cards[:a] # 앞
    cards_2 = cards[a:] # 뒤
    result_card = []
    for i in range(N):
        try:
            if i % 2 == 0:
                result_card.append(cards_1[0])
                cards_1.pop(0)
            else:
                result_card.append(cards_2[0])
                cards_2.pop(0)
        except:
            if cards_2:
                result_card.append(cards_2[0])
    result = ' '.join(result_card)
    print(f'#{t} {result}')