# 모음이 보이지 않는 사람
T = int(input())

for t in range(1,1+T):
    input_str = list(input())
    aeiou = ['a','e','i','o','u']
    for i in aeiou:
        if i in input_str:
            while i in input_str:
                input_str.pop(input_str.index(i))
    print(f'#{t}', " ", *input_str, sep="")