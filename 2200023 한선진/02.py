# 모음이 보이지 않는 사람 

T = int(input())

a = ['a','e','i','o','u']


for t in range(1, T+1):
    string = input()
    result =''
    for i in range(len(string)):
        if string[i] in a:
            continue
        result += string[i]
    print(f'#{t} {result}')