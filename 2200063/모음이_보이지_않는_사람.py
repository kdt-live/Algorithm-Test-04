T = int(input())

list_ = ['a', 'e', 'i', 'o', 'u']

for t in range(T):
    S = input()
    result = []

    for s in S:
        if s not in list_:
            result.append(s)

    print(f'#{t+1} ', *result, sep='')