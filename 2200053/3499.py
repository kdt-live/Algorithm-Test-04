import sys
sys.stdin = open('2200053/input.txt')

T = int(input())

for t in range(1, T+1):
    n = int(input())
    string = input().split()
    #print(string)

    # 길이를 절반으로 나눔
    med_num = n // 2

    # result 인덱스 추가할 값
    idx = 1

    result = []
    # 짝수인 경우
    if n % 2 == 0:
        for i in range(n):
            if i < med_num:
                # i == 0, 1, 2
                result.append(string[i])
            else:
                # result 인덱스 1, 3, 5 자리에 추가
                result.insert(idx, string[i])
                idx += 2
        #print(result)
    else:
        for i in range(n):
            if i < med_num + 1:
                result.append(string[i])
            else:
                result.insert(idx, string[i])
                idx += 2

    print(f'#{t} {" ".join(result)}')