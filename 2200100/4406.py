T = int(input())
for t in range(T):
    string = input()
    a = ''
    b = ['a','e','i','o','u']
    for i in string:
        if i not in b :
            a += i
    print(f'#{t+1} {a}')