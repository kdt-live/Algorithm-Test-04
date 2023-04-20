# t = int(input())

# for i in range(1,t+1):
#     alp = input()
#     result = []

#     for j in range(len(alp)):
#         if alp[j] in ['a', 'e', 'i', 'o', 'u'] : 
#             continue
#         else:
#             result += alp[j]
#     print([''.join(result)])

t = int(input())

for i in range(1,t+1):
    alp = list(input())
    result = []

    for j in alp:
        if j not in ['a', 'e', 'i', 'o', 'u']:
            result.append(j)
        

    print(f'#{i}',''.join(result))
