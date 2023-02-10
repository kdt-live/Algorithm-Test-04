T = int(input())
for t in range(1,T+1):
    A = list(input())
    V = ['a','e','i','o','u']
    new_A = ''
    for i in A:
        if i not in V:
            new_A += i
    print(f'#{t} {new_A}')